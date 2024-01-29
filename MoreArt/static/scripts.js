window.onclick = function (event)
{
    var popup = document.getElementById("myPopup");
    if (event.target !== popup)
    {
        popup.style.display = "none";
    }
};
