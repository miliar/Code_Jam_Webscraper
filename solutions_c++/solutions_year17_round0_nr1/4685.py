#include <bits/stdc++.h>

#define pb push_back
#define f first
#define s second
#define pii pair<int, int>
#define mp make_pair
 
using namespace std;
 
const string name = "A",
             in_file = name + ".in",
             out_file = name + ".out";
 
ifstream fin(in_file);
ofstream fout(out_file);
 
void flip(char& side) {
	side = (side == '-' ? '+' : '-');	
}

void flip(string& pancakes, int lefty, int righty) {
	while (lefty < righty) {
		flip(pancakes[lefty++]);
	}
}

int solve(string& pancakes, int k) {
	int number_of_flips = 0;
	for (int i = k; i <= (int)pancakes.size(); i++) {
		if (pancakes[i - k] == '-') {
			flip(pancakes, i - k, i);
			number_of_flips++;
		}
	}
	return number_of_flips;
}

bool all_happy(string& pancakes) {
	for (char pancake : pancakes) {
		if (pancake == '-') {
			return false;
		}
	}
	return true;
}

int main() {
	int t, k;
	string pancakes;

	fin >> t;
	for (int test = 1; test <= t; test++) {
		fin >> pancakes >> k;

		int number_of_flips = solve(pancakes, k);

		fout << "Case #" << test << ": " <<  
					(all_happy(pancakes) ? to_string(number_of_flips) : "IMPOSSIBLE") << '\n';
	}

	return 0;
}