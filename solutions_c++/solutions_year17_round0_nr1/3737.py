#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t=1 ; t <= T ; t++) {
		string row;
		int K;
		cin >> row >> K;

		int sum = 0;
		for(int i=0 ; i <= row.size()-K ; i++) {
			if(row[i] == '-') { // on flip
				sum++;
				for(int k=0 ; k < K ; k++) {
					row[i+k] = row[i+k] == '-' ? '+' : '-';
				}
			}
		}

		cout << "Case #" << t << ": ";
		if( count(begin(row), end(row), '-') == 0 )
			cout << sum;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
}

// https://code.google.com/codejam/contest/3264486/dashboard
