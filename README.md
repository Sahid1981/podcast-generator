# Podcast Generator (linkedin course project (modified))

A GitHub Action that automatically generates a podcast RSS feed from a YAML configuration file.

## Overview

This action converts a `feed.yaml` file into a valid podcast RSS feed (`podcast.xml`) compatible with major podcast directories including Apple Podcasts and Spotify. It's perfect for automating podcast feed generation and keeping your feed updated with new episodes.

## Usage

### As a GitHub Action

Add this to your workflow file (e.g., `.github/workflows/generate-feed.yml`):

```yaml
name: Generate Podcast Feed

on:
  push:
    paths:
      - 'feed.yaml'

jobs:
  generate-feed:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: Sahid1981/podcast-generator@main
        with:
          email: your-email@example.com
```

## Configuration

Create a `feed.yaml` file in your repository with the following structure:

```yaml
title: "Your Podcast Title"
link: "https://yourwebsite.com"
description: "Your podcast description"
language: "en"
author: "Your Name"
image: "https://yourwebsite.com/podcast-image.jpg"
category: "Technology"

item:
  - title: "Episode 1: Introduction"
    description: "First episode of the podcast"
    file: "https://yourwebsite.com/episode1.mp3"
    published: "Mon, 1 Jan 2024 00:00:00 GMT"
    duration: "45:30"
    length: 123456789  # File size in bytes

  - title: "Episode 2: Advanced Topics"
    description: "Second episode covering advanced topics"
    file: "https://yourwebsite.com/episode2.mp3"
    published: "Mon, 8 Jan 2024 00:00:00 GMT"
    duration: "52:15"
    length: 145678901
```

## Output

The action generates a `podcast.xml` file containing:
- Channel metadata (title, description, author, category, etc.)
- iTunes-specific tags for compatibility with Apple Podcasts
- Podcast Index namespace for additional metadata
- Enclosure information for each episode

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `email` | The committer's email address | Yes | `{github.actor}@localhost` |

## How It Works

1. The action checks out your repository
2. Reads the `feed.yaml` file
3. Converts it to an RSS feed using Python's XML libraries
4. Formats the XML for readability
5. Commits and pushes the generated `podcast.xml` back to the repository

## Requirements

- A `feed.yaml` file in your repository
- Valid episode URLs and metadata
- Publishing rights to the repository

## License

See LICENSE file for details.
