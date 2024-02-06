document.getElementById("likeButton").addEventListener("click", function() {
    var notLiked = document.querySelector(".not-liked");
    var liked = document.querySelector(".liked");

    notLiked.classList.toggle("hidden");
    liked.classList.toggle("hidden");
});