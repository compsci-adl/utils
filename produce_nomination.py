'''
INSTRUCTIONS FOR USE: 
Export the response file from Google Sheets. Call it nominations.csv, and save it to the same location as this script. 
In the same folder, create a directory `output'. Download the images from the Google Drive folder and extract them into `output'. 
Run this script.
Open `output/all.html`. Copy each block into the appropriate area in `nominations/index.html'.
Copy the remaining files into `nominations/'
'''

import csv

CARD_TEMPLATE = """<div class="col s12 m3">
  <div class="card">
    <div class="card-image">
      <img src="{0}.jpg">
      <span class="card-title">{1}</span>
    </div>
    <div class="card-content">
      <p>{2}</p>
      </div>
      <div class="card-action">
        <a href="{0}.html">Read my profile</a>
      </div>
    </div>              
  </div>
"""

PAGE_TEMPLATE = """<h2 class="cs-pink center">{0}</h2>
<div class="col s12 m3">
  <div class="card">
    <div class="card-image">
      <img src="{1}.jpg"/>
    </div>
  </div>
  <p>{2}</p>
  <h4 class="cs-blue">Position(s)</h4>
    <ul class="dot-points">
      <li>{3}</li>
    </ul> 
</div>
<div class="col s12 m9">
  <h4 class="cs-blue">What will you bring to the CS Club?</h4>
  <p>{4}</p>
  <h4 class="cs-blue">Why do you want to be on the committee?</h4>
  <p>{5}</p>
  <h4 class="cs-blue">What previous experience do you have that will help you serve the club?</h4>  
  <p>{6}</p>
</div>"""

WHOLE_PAGE_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="canonical" href="https://csclub.org.au/nominations/{0}" />
  <title>CS Club | 2018 Committee Nomination</title>
  <!-- Materialize -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.0/css/materialize.min.css" integrity="sha256-mDRlQYEnF3BuKJadRTD48MaEv4+tX8GVP9dEvjZRv3c=" crossorigin="anonymous" />
  <!-- General stylesheet -->
  <link href="/css/styles.css" rel="stylesheet">
  <!-- Icons -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
  <!-- Favicon -->
  <link rel="icon" type="image/png" href="/images/logo_sm.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
  <link rel="icon" type="image/png" href="/images/favicon-32x32.png" sizes="32x32">
  <link rel="icon" type="image/png" href="/images/favicon-16x16.png" sizes="16x16">
  <link rel="manifest" href="/images/manifest.json">
  <link rel="mask-icon" href="/images/safari-pinned-tab.svg" color="#5bbad5">
  <link rel="shortcut icon" href="/images/favicon.ico">
  <meta name="msapplication-config" content="/images/browserconfig.xml">
  <meta name="theme-color" content="#ffffff">

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->
    </head>

    <body class="nominations">
      <div class="navbar-fixed">
        <nav>
          <div class="container nav-wrapper">
            <img id="logo" src="/images/logo_sm.png" style="height: 100%;" alt="">
            <a href="#" class="brand-logo with-logo">CS Club</a>
            <ul id="nav-mobile" class="right hide-on-med-and-down">
              <li><a href="/">Home</a></li>
              <li><a href="/about">About</a></li>
              <li><a href="/join">Join</a></li>
              <li><a href="/contact">Contact</a></li>
            </ul>
            <a href="#" data-activates="slide-out" class="button-collapse right">
              <i class="material-icons hide-on-large-only">menu</i>
            </a>
          </div>
        </nav>
      </div>
      <ul id="slide-out" class="side-nav">
        <li class="logo">
          <a id="logo-container" href="/" class="brand-logo">
            <img src="/images/logo.png" style="height: 100%;" alt="">
          </a>
        </li>
        <li class="search">
          <div class="search-wrapper card">
            <input class="search" placeholder="Search">
            <i class="material-icons">search</i>
            <div class="search-results"></div>
          </div>
        </li>
        <li><a href="/"><i class="material-icons">home</i>Home</a></li>
        <li><a href="/about"><i class="material-icons">info</i>About</a></li>
        <li><a href="/join"><i class="material-icons">person_add</i>Join</a></li>
        <li><a href="/contact"><i class="material-icons">email</i>Contact</a></li>
      </ul>
      <header>
        <div class="container">
          <div class="row">
            <div class="col s12">
              <h1 class="center">
                2018 Committee Nomination
              </h1>
            </div>
          </div>
        </div>
      </header>
      <main>
        <div class="container">
          <div class="row">
            {1}
          </div>
        </div>
      </main>
      <footer>
        <div class="container">
          <div class="row">
            <div class="col s12 m8">
              <h5>Computer Science Club</h5>
              <p>The University of Adelaide</p>
              <p>
                <a href="/">Home</a> | <a href="/about">About</a> | <a href="/join">Join</a> | <a href="/contact">Contact</a>
              </p>
            </div>
            <div class="col s12 m4">
              <div class="search-wrapper card">
                <input class="search" placeholder="Search">
                <i class="material-icons">search</i>
                <div class="search-results card"></div>
              </div>
              <div>
                Connect with us
                <div class="social-icons">
                  <a href="https://www.facebook.com/compsci.adl/" target="_blank">
                    <i class="fa fa-facebook-official"></i>
                  </a>
                  <a href="https://twitter.com/CompSciAdl" target="_blank">
                    <i class="fa fa-twitter"></i>
                  </a>
                  <a href="https://github.com/compsci-adl" target="_blank">
                    <i class="fa fa-github"></i>
                  </a>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col s12">
                <p>&copy; 2017 Computer Science Club. All rights reserved.</p>
              </div>
            </div>
          </div>
        </div>
      </footer>

      <!-- jQuery -->
      <script src="https://code.jquery.com/jquery-3.1.1.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>
      <!-- JS plugins and individual files -->
      <script src="/js/csclub.materialize-v1.0.js"></script>
      <script src="/js/lunr.min.js"></script>
      <script src="/js/search.js"></script>
      <!-- CS Club js -->
      <script src="/js/csclub.common.js"></script>
      <script src="/js/csclub.about.js"></script>
    </body>

    </html>
"""

class NominationForm:
  def __init__(self, csv_row):
    self.name = csv_row[1]
    self.positions = csv_row[2].split(", ")
    self.biography = csv_row[3]
    self.question1 = csv_row[4]
    self.question2 = csv_row[5]
    self.question3 = csv_row[6]
    self.url = self.name.replace(" ", "")

  def card(self):
    return CARD_TEMPLATE.format(self.url, self.name, self.biography)

  def page(self):
    li_positions = "</li>\n<li>".join(self.positions)
    main = PAGE_TEMPLATE.format(self.name, self.url, self.biography, li_positions, self.question1, self.question2, self.question3)
    return WHOLE_PAGE_TEMPLATE.format(self.url, main)


with open('nominations.csv', 'rt') as csvfile:
  reader = csv.reader(csvfile)
  # Skip the header
  next(reader) 

  for row in reader:
    nomination = NominationForm(row)
    with open("output/" + nomination.url + ".html", 'w') as f:
      f.write(nomination.page())
    with open("output/all.html", 'a') as g:
      g.write(nomination.card())
      g.write("\n\n")