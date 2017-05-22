
import cvfy
import evaluate

app = cvfy.register("nongh::641280:5001::54.158.186.33")


@cvfy.crossdomain
@app.listen()
def runner():

    all_image_paths = cvfy.getImageArray()
    input_image = all_image_paths[0]  # /tmp/somepath/somefile.png
    # style transfer
    output_image = evaluate.serve(input_image)
    cvfy.sendImageArray([output_image], mode='file_path')

    return 'OK'

app.run()
