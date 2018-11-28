/*input
5
4 2
5 2
6 2
1000 1000
1000 1
*/
#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define sp " "
#define fi first
#define se second
#define MOD 1000000007
#define N 1
#define Mask(x) (1ll<<(x))
#define int long long
#define lnode (node<<1)
#define rnode ((node<<1)+1)
#define mid ((l+r)>>1)
using namespace std;
typedef pair<int, int> ii;
typedef long long ll;

queue<int> q;
map<int, int> cnt;
ii ans; int n, k, t;

void insert(int x, int num){
	cnt[x] += num;
	if(cnt[x] == num) q.push(x);
}

signed main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> t;
	for(int test = 1; test <= t; ++test){
		cin >> n >> k; cnt.clear();
		while(!q.empty()) q.pop(); insert(n, 1);
		while(k){
			int a = q.front(); q.pop();
			if(cnt[a] < k){
				k -= cnt[a];
				insert(a>>1, cnt[a]);
				insert((a-1)>>1, cnt[a]);
				continue;
			}
			ans = mp((a-1)>>1, a>>1);
			break;
		}
		cout << "Case #" << test << ": " << ans.se << sp << ans.fi << endl;
	}
	return 0;
}