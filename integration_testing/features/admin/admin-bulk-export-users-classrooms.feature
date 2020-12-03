Feature: Admin bulk export of users and classrooms
  Admin needs to be able to export users and their classrooms

  Background:
    Given I am signed in to Kolibri as a facility admin user
      And I am on *Facility > Data* page
      And there are learners enrolled in classrooms and coaches assigned to them

  Scenario: Export a CSV file containing all users in the facility
    When The user clicks on *Export* button under *Import and export users* heading
    Then The user sees the loading indicator
      And The user is able to open or save or the file 'users_<date>_<time>.csv'
      # <date> is current date and <time> current time, for example users_20200420_194415.csv
    When The user opens the CSV file
    Then The user sees that it contains only users from my facility, even if there are more facilities in the device
