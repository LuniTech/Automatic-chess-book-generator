Chess Puzzle Book Generator - README
Overview

This Python script processes PGN (Portable Game Notation) chess files to create a structured puzzle book in Microsoft Word (.docx) format. It extracts chess positions from PGN files, generates visual diagrams, and organizes them into a printable document with solutions.
Key Features

    Processes multiple PGN files from a specified folder

    Cleans PGN content by removing comments, variations, and unwanted headers

    Generates visual chess diagrams from each puzzle position

    Organizes puzzles into "Days" (10 puzzles per day)

    Creates a solutions section with full PGN notation

    Outputs a professional-looking Word document

Requirements

    Python 3.x

    Required packages:

        python-chess (chess library)

        python-docx (Word document creation)

        cairosvg (SVG to PNG conversion)

        natsort (natural sorting of filenames)

Usage

    Place your PGN files in the specified folder (pgn_folder in the script)

    Run the script: python puzzle_book_creator.py

    The script will generate a Word document named chess_puzzles.docx

File Structure

    The main document contains:

        Title page

        Puzzles organized in groups of 10 ("Day 1", "Day 2", etc.)

        Each puzzle shows the position with indication of whose turn it is

        Solutions section with complete PGN notation

Customization

You can modify:

    The input folder path (change pgn_folder variable)

    Output filename (change output_doc parameter)

    Puzzle grouping (modify the 10 in the day calculation)

    Diagram size (change width=Inches(3.0))

    Unwanted headers (edit unwanted_headers list)

Notes

    The script skips invalid or empty PGN files

    Only the mainline moves are processed (variations are removed)

    The document includes page breaks between solutions for clean printing
