#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


const bool OUTPUT_TO_FILE = true;


int main()
{
	cout.sync_with_stdio(false);
	stringstream output;

	int ans;
	int t;
	string s;
	int k;
	bool pan[1000];
	bool poss;

	cin >> t;
	for (int run = 1; run <= t; run++)
	{
		cin >> s;
		cin >> k;
		ans = 0;
		poss = true;

		for(int i = 0; i < s.size(); i++) {
    		if (s[i] == '+') {
				pan[i] = true;
			}
			else {
				pan[i] = false;
			}
		}

		for(int i = 0; i <= s.size() - k; i++) {
			if (!pan[i]) {
				for (int j = i; j < i + k; j++) {
					pan[j] = !pan[j];
				}

				ans++;
			}
		}

		for (int i = s.size() - k; i < s.size(); i++) {
			if (!pan[i]) {
				poss = false;
				break;
			}
		}

		if (poss) {
			output << "Case #" << run << ": " << ans << "\n";
		}
		else {
			output << "Case #" << run << ": " << "IMPOSSIBLE" << "\n";
		}
//		cout << run << "\n";
	}

	if (OUTPUT_TO_FILE)
	{
		ofstream output_file;
		output_file.open("out.txt");
		output_file << output.rdbuf();
		output_file.close();
	}
	else
	{
		cout << output.rdbuf();
	}
}
