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
int n, a[6], cnt[3], b[6];
vector<int> v;
char col[maxn] = "ROYGBV";
bool f[6];
void put(int id){
	if (f[id]){
		int jd = (id + 3) % 6;
		for (int i = 0; i < a[jd]; ++i) cout << col[id] << col[jd];
		cout << col[id];
		f[id] = false;
	}else cout << col[id];
}
int main(){
	int ik, i, j, k, kase;
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	cin >> kase;
	for (ik = 1; ik <= kase; ++ik){
		cout << "Case #" << ik << ": "; 
		
		cin >> n;
		for (i = 0; i < 6; ++i) cin >> a[i];
		v.clear();
		for (i = 0; i < 6; ++i)
			if (a[i]) v.push_back(i);
		if (v.size() == 2){
			j = v[0], k = v[1];
			if (a[j] != a[k] || k - j == 1 || k - j == 5) cout << "IMPOSSIBLE" << endl;
			else{
				for (i = 0; i < a[j]; ++i) cout << col[j] << col[k];
				cout << endl;
			}
			continue;
		}
		memset(cnt, 0, sizeof cnt);
		memset(f, true, sizeof f);
		cnt[0] = a[0] + a[1] + a[5];
		cnt[1] = a[2] + a[1] + a[3];
		cnt[2] = a[4] + a[3] + a[5];
		bool ok = true;
		for (i = 0; i < 3; ++i) if (cnt[i] > n/2) ok = false;
		if (a[1] >= a[4]) ok = false;
		if (a[3] >= a[0]) ok = false;
		if (a[5] >= a[2]) ok = false;
		memcpy(b, a, sizeof b);
		b[4] -= b[1];
		b[0] -= b[3];
		b[2] -= b[5];
		int tot = b[0] + b[2] + b[4];
		for (i = 0; i < 6; i += 2)
			if (b[i] > tot / 2) ok = false;
		if (ok == false){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		int id = 0;
		for (i = 0; i < 6; i += 2)
			if (b[i] > b[id]) id = i;
		int C = 0;
		for (i = 0; i < 6; i += 2)
			if (i != id) C += b[i];
		while (b[id]--){
			put(id);
			for (j = 0; j < 6; j += 2)
				if (j != id && b[j]){
					put(j);
					b[j]--;
					C--;
					if (C <= b[id]) break; 
				}
		}
		cout << endl;
	} 
	return 0;
}

