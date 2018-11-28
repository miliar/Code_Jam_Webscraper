#include <bits/stdc++.h>

using namespace std;

#define int long long

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;
	for(int cont=1; cont <= t; cont++) {
		string s;
		cin >> s;
		for(int i=s.size()-1; i > 0; i--)
			if(s[i] < s[i-1]) {
				s[i-1]--;
				for(int j=i; j < s.size(); j++)
					s[j] = '9';
			}
		int j=0;
		while(j < s.size() && s[j] == '0')
			j++;
		cout << "Case #" << cont << ": ";
		for(int i=j; i < s.size(); i++)
			cout << s[i];
		cout << endl;
	}

	return 0;
}

