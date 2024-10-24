from flask import Flask, request, render_template, send_from_directory
import os
import numpy as np
import librosa
from moviepy.editor import VideoFileClip
import mediapipe as mp
from scipy.signal import correlate
import random
import a