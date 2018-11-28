#include <bits/stdc++.h>
using namespace std;

int T, k;
string s;
bool b[10000];

int main(){
	cin >> T;
	for (int q = 1; q<=T; q++){
		cout << "Case #" << q << ": ";

		cin >> s; 
		cin >> k;

		int n = s.length();

		for(int i = 0; i < n; i++){
			if (s[i] == '-') b[i] = false;
			else if (s[i] == '+') b[i] = true;
			else cout << "LOLWHAT" << endl;
		}
		int moves = 0;
		for(int i = 0; i+k <= n; i++){
			if (!b[i]){
				moves++;
				for (int j = i; j<i+k; j++) b[j] = !b[j];
			}
		}
		bool possible = true;
		for (int i = 0; i<n; i++) possible = possible && b[i];
		

		if (!possible) cout << "IMPOSSIBLE" << endl;
		else cout << moves << endl;
	}
}