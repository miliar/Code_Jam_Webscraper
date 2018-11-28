/*#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int countGroups(string s) { //O(S)
	char old = 'o';
	int groups = 0;
	for (int i = 0; i < s.length(); i++) {
		if (old != s[i]) {
			groups++;
			old = s[i];
		}
	}
	return groups;
}

int getGroup(string s, int p) {
	int g = 0;
	char old = s[p];
	int c = p;
	while (c < s.length() && s[c] == old) {
		g++;
		c++;
	}
	return g;
}

string flip(string s, int p, int k) {
	string cpy = s;
	for (int i=p; i < p + k; i++) {
		if (cpy[i] == '+') cpy[i] = '-';
		else cpy[i] = '+';
	}
	return cpy;
}

int main() {
	ifstream fin("A-small-attempt1.in");
	ofstream fout("output.txt");

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++) {
		std::cout << t << endl;
		string pancakes;
		int k;
		int moves = 0;
		fin >> pancakes >> k;
		int i = 0;
		bool solved = true;
		while (count(pancakes.begin(), pancakes.end(), '-') != 0) {
			char c = pancakes[i];
			int group = getGroup(pancakes, i);
			if (c == '-' && group % k == 0 && (i == 0 || pancakes[i-1] == '+')) {
				pancakes = flip(pancakes, i, group);
				moves += group / k;
				i = 0;
			}
			else {
				string flipped = flip(pancakes, i, k);
				if (countGroups(flipped) < countGroups(pancakes)) {
					pancakes = flipped;
					moves++;
					i = 0;
				}
				else {
					i++;
					if (i == pancakes.length() - k + 1) {
						solved = false;
						break;
					}
				}
			}
		}
		string answer = solved ? to_string(moves) : "IMPOSSIBLE";
		fout << "Case #" << to_string(t) << ": " << answer << endl;
	}
}*/


#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

string flip(string s, int p, int k) {
	string cpy = s;
	for (int i = p; i < p + k; i++) {
		if (cpy[i] == '+') cpy[i] = '-';
		else cpy[i] = '+';
	}
	return cpy;
}

int main() {
	ifstream fin("A-large.in");
	ofstream fout("output.txt");

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++) {
		string pancakes;
		int k;
		fin >> pancakes >> k;
		int moves = 0;
		int i = 0;
		bool solved = true;
		while (count(pancakes.begin(), pancakes.end(), '-') > 0) {
			if (i <= pancakes.length() - k) {
				if (pancakes[i] == '-') {
					pancakes = flip(pancakes, i, k);
					moves++;
				}
				i++;
			}
			else {
				solved = false;
				break;
			}
		}

		string answer = solved ? to_string(moves) : "IMPOSSIBLE";
		
		fout << "Case #" << to_string(t) << ": " << answer << endl;
	}
}