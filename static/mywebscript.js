function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            document.getElementById("system_response").innerText =
                this.responseText;
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
        true
    );
    xhttp.send();
}
