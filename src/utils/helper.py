import os

# This function is used to check whether a given finename has an valid file extenstion or not.
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# This function is used to save an uploaded file to a specified directory if it has an valid file extension
def save_upload_file(file):
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join('uploads', filename))
        return filename
    else:
        return None