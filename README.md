# KINDLY SPARKLES
A forum-like web application to share uplifting incidents or news to highlight the good in people !

## [Link to the live website](https://kindlysparkles.web.app)

### Screenshots:
**Home Page**

![Home page](/github_assets/KS_Home_Page.png)

**About Page**

![About page](/github_assets/KS_About_Page.png)

**View on smaller Screens**

![View on smaller screens](/github_assets/KS_on_phones.png)


### Video Demo (Clicking below will redirect to youtube):
[![Watch the video demo](https://img.youtube.com/vi/GmKBkA_BBGk/0.jpg)](https://www.youtube.com/watch?v=GmKBkA_BBGk)


### Description:

**Why Kindly Sparkles is made :**
We drift closer towards negativity each passing day. Most of the times only the unfortunate events reach us through social media and news highlight. All the good deeds in the world go unnoticed. Let's highlight the good in people!! Welcome to Kindly Sparkles. Kindness and good deeds are recursive in nature, they echo and multiply; let your posts inspire !

**Examples of Posts appreciated on the app:**
- Incidents about times when others have been kind to us or vice versa.
- Gratitude Journaling - Things or people we are grateful for in our life.
- A great achievement you are very proud of.
- A positive interaction with a family member, a friend or even a stranger.
- Anything that can potentially make a visitor feel better!

**Features for users:**
- The newest post will always be on top to keep things fresh.
- Click on username of any post and the app displays posts made by that username only.
- Add an optional image but pasting a web link of an image in the image field. A good image can add so much to a post.
- Like button is available to show support to the post.
- Report button helps you report a post unaligned with the concept. After a certain number of reports, the post will be filtered out.
- An about page containing some important information.

**Design:**
- A database is created with 1 table using sqlite3. Columns are id, contents of the post, likes, reports and time.
- The database is connected to python. Python uses flask to host the website.
- Userinput in html is sent to server via post and the the database is updated after userinput validations.
- With the help of jinja, data is passed from python to html to render info fetched from database.
- With the help of javascript, some data is sent to server. These are action buttons which doesnt reload the page and changes html data.
- The overall stlying of the html using css is well aligned with the core concept of the app. I believe it looks uplifting.
- The css is also designed to render html differently on different screen sizes.

**Technical Features:**
- Using js, a random question(math equation) is created each time the page is refreshed. Entering the correct answer is compulsory to post data to server. This is a basic human spam protection although technical folks can easily make bots to automate the answering.
- When a post is created, the time of the action is auto generated and saved by the database. When rendering this time data from database, javascript is used to fetch page visitor's timezone and change the rendered time in html accordingly.
- Clicking the link or report button a second time will result in an undo event.
