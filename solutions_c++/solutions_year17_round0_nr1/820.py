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
		int k, j=0, r=0;
		cin >> s >> k;
		queue<int> q;
		for(int i=0; i < s.size(); i++) {
			if(s[i] == '-')
				s[i] = 0;
			else
				s[i] = 1;
			if(!q.empty() && q.front() == i) {
				j--;
				q.pop();
			}
			if((s[i]+j)%2 == 0) {
				if(i+k > s.size()) {
					r=-1;
					break;
				}
				j++;
				r++;
				q.push(i+k);
			}
		}

		cout << "Case #" << cont << ": ";
		if(r >= 0)
			cout << r;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}

	return 0;
}

