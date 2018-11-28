#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define s second
#define f first
#define mp make_pair

using namespace std;
const int maxn = 1e6+123;
const int mod = 1e9+7;


string s;
int k;

int main() {
// 	freopen("in","r",stdin);
 //	freopen("out","w",stdout);
 	int tt;
 	cin >> tt;
 	for (int ii = 1, sz; ii <= tt; ii++) {
 		cin >> s >> k;
 		int ans = 0;
 		for (int i = 0; i < s.size(); i++) {
 			if (s[i] == '-' && i + k - 1 < s.size()) {
 			 	for (int j = i; j <= i + k - 1; j++)
 			 		s[j] = (s[j] == '-' ? '+' : '-');
 			  	ans++;
 		 	}
 		}
 		bool ok = true;
 		for (int i = 0; i < s.size(); i++)
 			if (s[i] == '-') ok = false;
 		if (ok)
 			printf("Case #%d: %d\n", ii, ans);
 		else
 			printf("Case #%d: IMPOSSIBLE\n",ii);
 	}
 	return 0;
}