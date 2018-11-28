#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
char not(char a) {
	if (a == '-') return '+';
	else return '-';
}


int main() {
	ifstream cin;
	ofstream cout;
	cin.open("A-large.in");
	cout.open("out.txt");
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string S;
		int k;
		cin >> S>>k;
		int n = S.size();
		int cnt = 0;
		for (int i = 0; i < n - k+1; i++) {
			if (S[i] == '-') {
				cnt++;
				for (int j = i; j < i + k; j++) {
					S[j] = not(S[j]);
				}
			}

		}

		for (int i = 0; i < n; i++) if (S[i] == '-') cnt = -999;

		if(cnt ==-999)
		cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		else 
			cout << "Case #" << t << ": " << cnt << endl;

	}



	return 0;
}