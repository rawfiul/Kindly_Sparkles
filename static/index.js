document.addEventListener("DOMContentLoaded", function() {
    // Change the UTC times in dB to local user times
    let timeElementList = document.querySelectorAll("#postdate");
    for (let element of timeElementList) {
        // Parse the UTC string directly
        var utcDate = new Date(element.innerText);
        // Get the local time zone offset in minutes
        var localTimeZoneOffset = utcDate.getTimezoneOffset();
        // Adjust the date and time to the local time zone
        var localDate = new Date(utcDate.getTime() - (localTimeZoneOffset * 60 * 1000));
        element.innerText = localDate.toLocaleString("en-GB", {day: 'numeric', month: 'short', year: 'numeric', hour: 'numeric', minute: 'numeric', hour12: false});
    };

    // SPAM_ PROTECTION MATH EQUATION HANDLING
    var random_number1 = Math.floor(Math.random() * 9) + 1;
    var random_number2 = Math.floor(Math.random() * 9) + 1;
    var sys_answer = random_number1 + random_number2;
    // Update the hidden input field with the correct answer
    document.getElementById("sysAnswer").value = sys_answer;
    // Display the equation to the user (you can customize this part)
    var equationElement = document.getElementById("userQuestion");
    equationElement.setAttribute("placeholder", `${random_number1} + ${random_number2} ?`);


    // Event delegation - selected the grandparent to catch all clicks
    var postsContainer = document.querySelector('#container');
    // Handles likes, reports
    var likeToggleState = false;
    var reportToggleState = false;
    postsContainer.addEventListener('click', function(event) {
        var target = event.target;
        if (target.classList.contains('like-btn') && !likeToggleState) { // first click
            sendAction('like', target.getAttribute('value'));
            likeValue = target.firstElementChild;
            likeValue.innerText = parseInt(likeValue.innerText) + 1;
            likeToggleState = true;
            target.style.setProperty("background-color", "var(--liked)")
            target.style.setProperty("color", "white")
        } else if (target.classList.contains('like-btn') && likeToggleState) { // second click
            sendAction('dislike', target.getAttribute('value'));
            likeValue = target.firstElementChild;
            likeValue.innerText = parseInt(likeValue.innerText) - 1;
            likeToggleState = false;
            target.style.setProperty("background-color", "")
            target.style.setProperty("color", "black")
        } else if (target.classList.contains('report-btn') && !reportToggleState) {
            sendAction('report', target.getAttribute('value'));
            reportToggleState = true;
            target.style.setProperty("background-color", "var(--reported)")
            target.innerText = "Reported"
            target.style.setProperty("color", "white")
        } else if (target.classList.contains('report-btn') && reportToggleState) {
            sendAction('unreport', target.getAttribute('value'));
            reportToggleState = false;
            target.style.setProperty("background-color", "")
            target.innerText = "Report"
            target.style.setProperty("color", "black")
        }
    });

    // If user likes or reports a post, info is sent to server for db update
    function sendAction(actionType, postId) {
        const data = {
            "action": actionType,
            "id": postId
        };
        fetch("/action", {
            method: 'POST',
            headers: {
            'Content-Type': "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => response.text())
        .then(data => console.log('Fetch Response Data:', data))
        .catch(error => console.error('Fetch Error:', error));
    }

    console.log("Didnt i ask you not to waste your time checking the console? Getting to the easter egg is simpler than you think!");

});