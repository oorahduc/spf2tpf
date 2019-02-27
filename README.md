# spf2tpf

## Problem
Sequel Pro for macos is so unstable it crashes at random, as well as crash 100% of the time if you close a tab. Unfortunately, you have a ton of saved queries saved inside Sequel Pro.

## Solution
Switch to TablePlus, use spf2tpf to import your saved queries. Profit . ¯\_(ツ)_/¯

## Usage
1. Export your favorite queries from Sequel Pro. It will generate a .spf file.
2. Put this file in the same directory as spf2tpf.py and execute the following command given your exported file is called `sequelpro_favorites.sql`:

```bash
$ python3 spf2tpf.py sequelpro_favorites.sql
