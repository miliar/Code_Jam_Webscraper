#include<cstring>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int n;
char penCake[1000];

string unSolved = "IMPOSSIBLE";

int solve(unsigned int start, unsigned int count) {
	if (penCake[start + n] == NULL) {
		int check = 0, check_ = 0;
		for (int i = 0; i < n; i++) {
			if (penCake[start + i] == '+') check ++;
			if (penCake[start + i] == '-') check_++;
		}
		if (check == n) return count;
		if (check_ == n) return count + 1;
		return -1;
	}
	if (penCake[start] == '-') {
		for (int i = 0; i < n; i++) {
			penCake[start + i] = (penCake[start + i] == '-' ? '+' : '-');
		}
		count++;
	}	
	count = solve(start + 1, count);
	return count;
}

int main() {
	int cases;
	cin >> cases;
	for (int cc = 1; cc <= cases; ++cc) {
		memset(penCake, NULL, sizeof(penCake));
		cin >> penCake >> n;
		int sol = solve(0, 0);
		
		if(sol == -1) cout << "Case #" << cc << ": " << unSolved << endl;
		else cout << "Case #" << cc << ": " << sol << endl;
	}
	system("PAUSE");
	return 0;
}

