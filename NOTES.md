# Printing Guides from GameFAQs

- Install Ruby
- Install asciidoctor
- Install asciidoctor-pdf

## 2022-05-25

- Had a dumb fucking bug where one of the font faces was misspelled. Jesus.
  * `bold_italid` instead of `bold_italic`.

## 2020-07-22 12:39:40

- Changed the boss listing in `bof2-gfaqw-cless_alvein_DavidK519.adoc` from a description list to a table with no frame, no grid, and some other attributes.

  ```
  [frame=none,grid=none,stripes=none,cols=">11%s,1%,~"]
  |===
  | HP    | | 
  | Exp   | | 
  | Coins | | 
  | Notes | | 
  |===
  ```

## TODO

- Fixup theme file for printing
- Look at CSS for html output as well
- Create a base file to start with to make conversion easier
- Double check that we're using attributes for urls in the document
  * original_url, original_author, etc
  * and using them in the doc as well
- conditionals to include an image of the header at the top of the document if we're outputting an html file
  * pdfs already have this with :front-cover-image:
- Can you apply styling to all the tables within a document? bof2-idf-shop-dinobotmaximized.adoc has a lot of tables in it with header & stripes options which might be best applied with a single line rather than throughout the whole document.

## Things to grab from the FAQs

- Original copy of the FAQ
  * For faqs that are HTML (there aren't many) then single-file copy all the different pages
- Url for the faq
  * https://gamefaqs.gamespot.com/snes/563530-breath-of-fire-ii/faqs/13663
- Name of the FAQ creator(s), email address listed in FAQ, and the urls to their profiles
  * EX: https://gamefaqs.gamespot.com/snes/563530-breath-of-fire-ii/faqs/13663
  * created by: `Storm`
  * profile url: https://gamefaqs.gamespot.com/community/Storm
- ASCII header
  * We want to preserve these in the original document as a final section, but also turn them into PNGs (see batch file for example of command to do so, it uses ImageMagick)
- Any other significant ASCII art which could include:
  * Section headings
  * Section dividers
  * ASCII maps
