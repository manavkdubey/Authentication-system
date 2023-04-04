var users = require('./cred.json');
function login(username, password) {
    for (var i = 0; i < users.users.length; i++) {
      if (users.users[i].username === username && users.users[i].password === password) {
        // Login successful
        return true;
      }
    }
  
    // Login failed
    return false;
  }
  
var loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", function(event) {
  event.preventDefault();

  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  if (login(username, password)) {
    window.location.href = "logged.html";
  } else {
    window.location.href = "invalid.html";

  }
});

  