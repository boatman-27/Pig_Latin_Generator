document.getElementById("submitButton").addEventListener("click", function() {
    // Get the input text
    var inputText = document.getElementById("inputText").value;
    
    // Perform some action (you can customize this part)
    var outputText = "You entered: " + inputText;
    
    // Display the result
    document.getElementById("outputText").textContent = outputText;
});