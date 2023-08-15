$(document).ready(function() {
    $('form').on('submit', function(event) {
        $.ajax({
            data : {
                name : $('#nameInput').val(),
            },
            type : 'POST',
            url : '/process'
        })
        .done(function(data) {
        $('#successResponse').text(data.response).show();
        });
        event.preventDefault();
    });
});