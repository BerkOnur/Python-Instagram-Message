Feature: instagram

	Scenario: Login instagram
		Given I visit instagram
		When I see log in form
		Then login with username "******" and password "*******"
		Then I close popup "Accept"
		Then I close popup "Şimdi Degil"
		When I click here "message button"
		Then I click here "third message"
		Then I click here "send message"

