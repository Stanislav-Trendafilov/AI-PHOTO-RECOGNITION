var selectedImage = false;

function previewImage(event) {
    var input = event.target;
    var preview = document.getElementById('preview');
    var clearBtn = document.getElementById('clear-btn');
    
    var reader = new FileReader();
    
    reader.onload = function(){
        preview.src = reader.result;
        preview.style.display = 'block';
        clearBtn.style.display = 'block';
        document.getElementById('upload-label').style.display = "none";
        document.getElementById('upload-icon').style.display = "none";
        document.getElementById('upload-btn').style.display = "block";
        document.getElementById('result-message').textContent = "";
        selectedImage = true;
        document.getElementById('line').style.display = "none";
    };
    
    reader.readAsDataURL(input.files[0]);
}

function clearImage() {
    var preview = document.getElementById('preview');
    var clearBtn = document.getElementById('clear-btn');
    var input = document.getElementById('imageInput');

    preview.src = '#';
    preview.style.display = 'none';
    clearBtn.style.display = 'none';
    document.getElementById('upload-label').style.display = "inline";
    document.getElementById('upload-icon').style.display = "block";
    document.getElementById('line').style.display = "inline";
    selectedImage = false;
    document.getElementById('result-message').textContent = "";
    document.getElementById('upload-btn').style.display = "none";
    preview.value = ''; //Tova beshe imageInput.value Clear the input value to allow selecting the same file again
}

function resetDefault(){
    var preview = document.getElementById('preview');
    var clearBtn = document.getElementById('clear-btn');

    if(!selectedImage){
       document.getElementById('result-message').textContent = "Please select an image first!";
       return;
    }

    preview.style.display = 'block';
    clearBtn.style.display = 'block';
    document.getElementById('upload-label').style.display = "none";
    document.getElementById('upload-icon').style.display = "none";
    document.getElementById('line').style.display = "none";
}