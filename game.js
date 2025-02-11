function startGame() {
    document.getElementById("start-screen").classList.add("hidden");
    document.getElementById("game-screen").classList.remove("hidden");
}

function getComputerChoice() {
    const choices = ["rock", "paper", "scissors"];
    return choices[Math.floor(Math.random() * choices.length)];
}


function playGame(playerChoice) {
    const computerChoice = getComputerChoice(); // Generate computer choice
    localStorage.setItem("playerChoice", playerChoice); // Store player choice
    localStorage.setItem("computerChoice", computerChoice); // Store computer choice

    console.log("Player choice saved:", playerChoice);
    console.log("Computer choice saved:", computerChoice);

    // Redirect to think.html AFTER storing choices
    window.location.href = "think.html"; 
}

