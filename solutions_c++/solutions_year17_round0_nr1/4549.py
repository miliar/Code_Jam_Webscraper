#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int countUnhappy(char cakes[]);
void main() {
	int t;

	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int caseI = 1; caseI <= t; ++caseI) {
		char cakes[1050];
		int anzahlWenden, countcakes;
		int wendungen = 0;
		cin >> cakes >> anzahlWenden;
		//Anzahl von Cakes im Array
		for (countcakes = 0; cakes[countcakes] == 45 || cakes[countcakes] == 43 ; countcakes++);
		for (int i = 0; i <= countcakes - anzahlWenden+1; i++)
		{
			if (countUnhappy(cakes) == 0)
			{
				break;
			}
			if (cakes[i] == '-')
			{
				wendungen++;
				for (int b = 0; b < anzahlWenden; b++) {
					if (cakes[b + i] == '-') {
						cakes[b + i] = '+';
					}
					else
					{
						cakes[b + i] = '-';
					}
				}
			}

		}
		if (countUnhappy(cakes) != 0) {
			cout << "Case #" << caseI << ":  IMPOSSIBLE"  << endl;
		}
		else
		{
			cout << "Case #" << caseI << ": " << wendungen << endl;
		}
		
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}

int countUnhappy(char cakes[])
{
	int anz = 0;
	for (int i = 0; cakes[i]; i++) {
		if (cakes[i] == '-') {
			anz++;
		}
	}
	return anz;
}