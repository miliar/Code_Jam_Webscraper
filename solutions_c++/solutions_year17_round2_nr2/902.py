#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>      // std::setprecision

using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define endl '\n'

using dvojice = pair<long long int, long long int>;




int main() {
	std::ios::sync_with_stdio(false);


	int t, n, red,orange, yellow, green, blue, violet, number, actblue,actred,actyellow;
	string colors;
	

	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n >> red >> orange >> yellow >> green >> blue >> violet;
		colors.resize(n);


		if (orange == blue && yellow + red + green + violet == 0) {
			for (int o = 0; o < n; o++)
			{
				if (o % 2 == 0) {
					colors[o] = 'O';
				}
				else
					colors[o] = 'B';
			}
			cout << "Case #" << i << ": " << colors << endl;
			continue;
		}

		if (yellow == violet && orange + red + green + blue == 0) {
			for (int o = 0; o < n; o++)
			{
				if (o % 2 == 0) {
					colors[o] = 'Y';
				}
				else
					colors[o] = 'V';
			}
			cout << "Case #" << i << ": " << colors << endl;
			continue;
		}

		if (red == green && yellow + blue + orange + violet == 0) {
			for (int o = 0; o < n; o++)
			{
				if (o % 2 == 0) {
					colors[o] = 'R';
				}
				else
					colors[o] = 'G';
			}
			cout << "Case #" << i << ": " << colors << endl;
			continue;
		}


		if (orange > blue - 1 && orange>0) {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}

		if (green > red - 1 && green > 0) {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}

		if (violet > yellow - 1 && violet>0) {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}

		actblue = blue - orange;
		actred = red - green;
		actyellow = yellow - violet;

		if (actblue + actyellow < actred || actred + actyellow < actblue || actblue + actred < actyellow) {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}

		

		bool jearange = orange > 0;
		bool jegreen = green > 0;
		bool jeviolet = violet > 0;

		char last;

		if (max(actblue, max(actred, actyellow)) == actred)
			last = 'R';
		else
			if(max(actblue,actyellow)==actyellow)
			last = 'Y';
			else
			{
				last = 'B';
			}

		char first = last;

		int position = 0;
		while (position < n) {
			switch (last)
			{
			case 'B':
				if (jearange) {
					for (int o = 0; o < orange; o++)
					{
						colors[position + 2 * o] = 'B';
						colors[position + 1 + 2 * o] = 'O';
					}
					colors[position + 2 * orange] = 'B';
					position += 2 * orange + 1;
					jearange = false;
				}
				else
					colors[position++] = 'B';
				actblue--;

				if (last != first && actred == actyellow)
				{
					last = first;
					continue;
				}
				if (max(actred, actyellow) == actred)
					last = 'R';
				else
					last = 'Y';

				break;

			case 'R':
				if (jegreen) {
					for (int o = 0; o < green; o++)
					{
						colors[position + 2 * o] = 'R';
						colors[position + 1 + 2 * o] = 'G';
					}
					colors[position + 2 * green] = 'R';
					position += 2 * green + 1;
					jegreen = false;
				}
				else
					colors[position++] = 'R';
				actred--;
				if (last != first && actblue == actyellow)
				{
					last = first;
					continue;
				}


				if (max(actblue, actyellow) == actblue)
					last = 'B';
				else
					last = 'Y';

				break;

			case 'Y':
				if (jeviolet) {
					for (int o = 0; o < violet; o++)
					{
						colors[position + 2 * o] = 'Y';
						colors[position + 1 + 2 * o] = 'V';
					}
					colors[position + 2 * violet] = 'Y';
					position += 2 * violet + 1;
					jeviolet = false;
				}
				else
					colors[position++] = 'Y';
				actyellow--;

				if (last != first && actblue == actred)
				{
					last = first;
					continue;
				}

				if (max(actblue, actred) == actblue)
					last = 'B';
				else
					last = 'R';

				break;
			default:
				break;
			}

		}


		


		cout << "Case #" << i << ": " << colors<< endl;
	}

}