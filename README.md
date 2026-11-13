## What Should I Listen To?

# Project Description

What Should I Listen To? is a music recommendation website created using Python and the Drafter library for my CS1 final project.

The website helps users discover songs based on their mood, current activity, and preferred music genre.

# Features

Choose a mood: Happy, Sad, Relaxing, or Energetic.

Choose an activity: Studying, Cleaning, Driving, or Working Out.

Choose a genre: Pop, R&B, KPop, or Rap.

Receive a randomized song recommendation based on those preferences.

Get another matching recommendation.

Discover a completely random song using Surprise Me.

Browse the full collection of 320 song entries.

Add your own songs to the collection during the current app session.

View About and Help pages.

# Technologies Used

Python

Drafter

Python dataclasses

Python random library

# How It Works

The website stores song information in a list of Song objects. Each song has a title, artist, mood, activity, and genre.

When a user selects preferences, the program loops through the song collection, finds matching songs, and randomizes the recommendations.

# Project Files

This repository includes the application code, brainstorming and design worksheets, and records of AI conversations used during development.

# Live Website

Add the deployed website URL here after publishing.

# Notes

Songs added through the website are stored in the current application state and are not permanently saved to a database.
