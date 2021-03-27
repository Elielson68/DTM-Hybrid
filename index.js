const path = require("path");
const express = require("express");
const app = express();
const server = require("http").Server(app);


app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

console.log("Front-end Node.js: http://localhost:3000\n")
console.log("Back-end Flask: http://localhost:5000")
server.listen(3000);
