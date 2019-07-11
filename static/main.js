function onHover() {
    $(".addNoteImg").attr('src', '../static/compose2.png');
}

function offHover() {
    $(".addNoteImg").attr('src', '../static/compose.png');
}

function cardOver(element) {
    element.classList.add("cardHover")
}

function cardOut(element) {
    element.classList.remove("cardHover")
}

document.getElementById("passwordEye").addEventListener("click", function () {
    var x = document.getElementById("showHideIn").getAttribute("type");
    console.log(x);
    if (x === "password") {
        document.getElementById("showHideIn").setAttribute("type", "text");
        document.getElementById("passwordEye").classList.remove("fa-eye")
        document.getElementById("passwordEye").classList.add("fa-eye-slash")
    } else if (x == "text") {
        document.getElementById("showHideIn").setAttribute("type", "password");
        document.getElementById("passwordEye").classList.remove("fa-eye-slash")
        document.getElementById("passwordEye").classList.add("fa-eye")
    }

});

document.getElementById("formSwitch").addEventListener("click", function () {
    let isPrivate = document.getElementById("formSwitch").getAttribute("placeholder");
    if (isPrivate === "yes") {
        document.getElementById("formSwitch").setAttribute("placeholder", "no");
        document.getElementById("showHideIn").value = "";
        document.getElementById("showHideIn").disabled = true;
    } else if (isPrivate === "no") {
        document.getElementById("formSwitch").setAttribute("placeholder", "yes");
        document.getElementById("showHideIn").disabled = false;
    }
});

document.getElementById("search_icon").addEventListener('click', function () {
    let input = document.getElementById("search_input").value;
    document.getElementById("search_icon").setAttribute("href", input);
});

$(document).ready(() => {
   $('#show').on('click',(e) =>{
       $.ajax({
           data:{
               sPassword : $('#privateInputPassword').val(),
               sId : $('#sId').attr("placeholder")
           },
           type: 'POST',
           url: '/passwordcontrol'
       })
           .done((data) => {
               if (data.error){
                   console.log(data.error)
                    $('.wrongPassword').css("display", "block");
               }
               else{
                    $('#privateHeader').text(data.header);
                    $('#privateContent').text(data.note);
                    $('#privateModal').modal('hide');
                    $('#privateDetailModal').modal('show');
                    console.log(data.sPassword)
               }
           })
   });
});


