#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define fio ios_base::sync_with_stdio(false)
#define MOD 1000000007
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define range(a, b, c) (a>=b && a<c)
#define stlfor(a, b) for(auto a=b.begin(); a!=b.end(); a++)
#define rstlfor(a, b) for(auto a=b.rbegin(); a!=b.rend(); a++)
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
#define long int64_t
using namespace std;
using namespace __gnu_pbds;
typedef pair<int, int> pii;
typedef priority_queue<pii, vector<pii>, greater<pii>> min_pq;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST;

int main()
{
	int t;
	cin >> t;
	for(int tc=1; tc<=t; tc++)
	{
		int n, p;
		cin >> n >> p;
		vector<int> cnt(p, 0);
		for(int i=0; i<n; i++)
		{
			int a;
			cin >> a;
			cnt[a % p]++;
		}
		int ans = cnt[0];
		if(p == 2)
		{
			ans += (cnt[1] + 1) / 2;
		}
		else if(p == 3)
		{
			int tmp = min(cnt[1], cnt[2]);
			ans += tmp;
			cnt[1] -= tmp;
			cnt[2] -= tmp;
			ans += (cnt[1] + 2) / 3;
			ans += (cnt[2] + 2) / 3;
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
	return 0;
}