var client;
var request;
var index = 0;
var started = false;

function getMode() {
    return Microsoft.CognitiveServices.SpeechRecognition.SpeechRecognitionMode.shortPhrase;
}

function getKey() {
    return "73a0f2bbad2548428435f980818c4239";
}

function getLanguage() {
    return "en-us";
}


function clearText() {
    document.getElementById("user_answer").innerText = "speak now";
    document.getElementById("output").value = "";
}

function setText(text) {
    document.getElementById("output").value += text;
    var json = JSON.parse(text);
    if (json.length > 0) {
    	document.getElementById("user_answer").innerText = json[0].display;
        socket.emit('send message', json[0].display);
    }
}

function setIssue() {
    document.getElementById("user_answer").innerText = "tap mic to speak";
}

function setNextIssue() {
	index += 1;
	var array = getTexts();
	if (index >= array.length) {
		index = 0;
	}
	setIssue();
}

function stop() {
	started = false;
	document.getElementById("mic_off").className = "";
	document.getElementById("mic_on").className = "no-display";
}

function start() {
	if (started) {
		return;
	}
	started = true;
	document.getElementById("mic_off").className = "no-display";
	document.getElementById("mic_on").className = "";
    var mode = getMode();
    clearText();
    client = Microsoft.CognitiveServices.SpeechRecognition.SpeechRecognitionServiceFactory.createMicrophoneClient(
        mode,
        getLanguage(),
        getKey());
    client.startMicAndRecognition();
    setTimeout(function () {
        client.endMicAndRecognition();
	    stop();
    }, 5000);

    client.onPartialResponseReceived = function (response) {
        setText(response);
    }

    client.onFinalResponseReceived = function (response) {
        setText(JSON.stringify(response));
    }

    client.onIntentReceived = function (response) {
        setText(response);
    };
}

function next() {
	setNextIssue();
}

setIssue();