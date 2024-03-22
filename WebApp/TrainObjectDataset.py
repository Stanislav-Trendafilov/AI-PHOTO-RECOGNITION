import keras
from keras import layers

# Define the CNN model architecture
model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compile the model with binary crossentropy loss function and Adam optimizer
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Load the training and validation data
train_data = keras.preprocessing.image_dataset_from_directory(
    '/content/drive/MyDrive/DatasetForAI/train',
    batch_size=32,
    image_size=(256, 256),
    validation_split=0.2,
    subset='training',
    seed=123
)

val_data = keras.preprocessing.image_dataset_from_directory(
    '/content/drive/MyDrive/DatasetForAI/test',
    batch_size=32,
    image_size=(256, 256),
    validation_split=0.2,
    subset='validation',
    seed=123
)

# Train the model
model.fit(train_data, validation_data=val_data, epochs=10)

# Save the trained model
model.save('C:/Users/vorod/Downloads/ai_model.h5')