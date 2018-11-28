#include <sstream>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
using namespace std;
//10 million
#define ATTEMPTS 400000
int ans, k;
bool solve(string input) {
	bool solved = false;
	//cout << input << endl;
	for (int j = 0; j < ATTEMPTS; j++) {
		solved = true;
		for (int c = 0; c < input.size(); c++) if (input[c] == '-') solved = false;
		if (solved) break;
		for (int i = 0; i <= input.size() - k; i++) {
			if (input[i] == '-') {
				//cout << i << " " << k << endl;
				for (int c = i; c < i+k; c++) input[c] = (input[c] == '-') ? '+' : '-';
				ans++;
			}
		}
	}
	return solved;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int cases; cin >> cases >> ws;
	char tmp;
	for (int i = 1; i <= cases; i++) {
		string inputLine;
		ans = 0;
		//read input
		getline(cin, inputLine);
		istringstream iss(inputLine);
		vector<string> tokens{istream_iterator<string>{iss},
                      istream_iterator<string>{}};
		string input = tokens[0];
		k = atoi(tokens[1].c_str());
		//cout << input << " " << k << endl;
		bool solved = solve(input);
		if (solved)
			cout << "Case #" << i << ": " << ans << "\n";
		else 
		    cout << "Case #" << i << ": " << "IMPOSSIBLE\n";
	}
	
	return 0;
}