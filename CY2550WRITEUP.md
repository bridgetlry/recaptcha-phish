# CY 2550 Northeastern reCAPTCHA Phishing Simulation

> Sahithi Gaddam & Bridget Leary

------------------------------

This is a simulated phishing attack using a replica of Northeastern University's sign-in page, with the addition of John Hammond's reCAPTCHA phishing module (see repository this one was forked from).

Users are instructed to enter their username and proceed to the next page where they will enter their password and complete the 'I am not a robot' task. Once they do this and attempt to log-in, the screen will show that the user failed the phishing experiment.

## Execution
Once you navigate to this directory, run `python server.py` in the terminal and go to `localhost:8000` in your browser to get to the simulation.

## Code Details

`index.html` - original page with fake reCAPTCHA, starting point for phishing simulation, this is what was integrated into the Northeastern login page

`server.py` - script that executes the `GET` and `POST` requests to navigate between pages


1.  `username.html` - first page where the user can enter their Northeastern username or email

2. `password.html` - second page where the user can enter their password (or navigate to the 'Forgot Password' screen from the oriiginal Northeastern login page) as well as complete the reCAPTCHA

3. `failed.html` - final page once the user has verified their identity and completed the reCAPTCHA, shows that they failed the phishing experiment 