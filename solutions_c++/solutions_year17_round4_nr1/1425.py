/*
Thank you for your hacking.
Hope you high rating.
*/
#include <bits/stdc++.h>
using namespace std;
#define pr(x) cout << #x << " = " << x << endl;
#define bug cout << "bugbug" << endl;
#define ppr(x, y) printf("(%d, %d)\n", x, y);
#define MST(a,b) memset(a,b,sizeof(a))
#define CLR(a) MST(a,0)
#define SQR(a) ((a)*(a))
#define PCUT puts("\n---------------")

typedef long long ll;
typedef double DBL;
typedef pair<int, int> P;
typedef unsigned int uint;
const int MOD = 1e9 + 7;
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3f;
const int maxn = 1e2 + 4;
const int maxm = 1e3 + 4;
const double pi = acos(-1.0);

int cnt[maxn];
int main(){
	int ik, i, j, k, kase;
	freopen("Alarge.in", "r", stdin);
	freopen("Alargeout.txt", "w", stdout);
	scanf("%d", &kase);
	for (ik = 1; ik <= kase; ++ik){
		int n, m;
		cin >> n >> m;
		memset(cnt, 0, sizeof cnt);
		for (i = 0; i < n; ++i){
			cin >> j;
			cnt[j % m]++;
		}
//		cout << m << endl;
//		for (i = 0; i < m; ++i)
//			cout << cnt[i] << ' ';
//		cout << endl;
		int ans = cnt[0];
		if (m == 2)
			ans += (cnt[1]+1) / 2; 
		else if (m == 3){
			int add = min(cnt[1], cnt[2]);
			cnt[1] -= add;
			cnt[2] -= add;
			ans += add;
			if (cnt[1]){
				ans += cnt[1] / 3;
				cnt[1] %= 3;
			}else if (cnt[2]){
				ans += cnt[2] / 3;
				cnt[2] %= 3;
			}
			if (cnt[1] || cnt[2]) ans++;
		}else if (m == 4){
			ans += cnt[2] / 2;
			cnt[2] %= 2;
			int add = min(cnt[1], cnt[3]);
			cnt[1] -= add;
			cnt[3] -= add;
			ans += add;
			if (cnt[1]){
				ans += cnt[1] / 4;
				cnt[1] %= 4;
				if (cnt[1] >= 2 && cnt[2]){
					ans++;
					cnt[2] = 0;
					cnt[1] -= 2;
				}
			}else if (cnt[3]){
				ans += cnt[3] / 4;
				cnt[3] %= 4;
				if (cnt[3] >= 2 && cnt[2]){
					ans++;
					cnt[2] = 0;
					cnt[3] -= 2;
				}
			}
			if (cnt[1] || cnt[2] || cnt[3]) ans++;
 		}
		cout << "Case #" << ik << ": " << ans << "\n";
//		system("pause");
	} 
	return 0;
}

