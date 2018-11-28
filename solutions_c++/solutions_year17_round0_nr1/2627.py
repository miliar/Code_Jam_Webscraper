#include<bits/stdc++.h>

using namespace std;

const int MAXN = 2e3 + 10;

int n, k, a[MAXN];
string s;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		int ans = 0, cur = 0;;
		cin >> s >> k; n = s.size();
		memset(a, 0, sizeof(a));
		for (int i = 0; i < n; i++){
			cur -= a[i];
			int x = (s[i]=='+'?0:1);
			x ^= (cur&1);

			if (x){
				if (i + k > n){
					ans = -1;
					break;
				}
				
				ans++;
				cur++;
				a[i + k]++;
			}
		}

		if (ans == -1)
			cout << "Case #" << w << ": " << "IMPOSSIBLE" << "\n";
		else
			cout << "Case #" << w << ": " << ans << "\n";
	}
	return 0;
}
