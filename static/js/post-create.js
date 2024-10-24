$('#postSave').click(function (){
    let formData = new FormData();
    formData.append('text', $('#postText').val());
    formData.append('image', document.getElementById('postImage').files[0]);
    $.ajax('/post-create', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': formData,
        'processData': false,
        'contentTypes': false,
        'success': function (response){
               let posts = document.getElementById('posts')
            posts.innerHTML += `<h3>${$('#postText').val()}</h3>` + posts.innerHTML;
            $('#postText').val('');
            const postModel = new bootstrap.Modal('#postModal')
            postModal.hide();
        }
    });
});
