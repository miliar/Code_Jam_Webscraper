#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i < s.size(); i++){
			if (s[i] == '-' && i + k - 1 < s.size()){
				for (int j = i; j < i + k; j++){
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				ans++;
			}
		}
		bool impossible = false;
		for (int i = 0; i < s.size(); i++){
			if (s[i] == '-')
				impossible = true;
		}
		cout << "Case #" << t+1 << ": ";
		if (impossible)
			cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
}