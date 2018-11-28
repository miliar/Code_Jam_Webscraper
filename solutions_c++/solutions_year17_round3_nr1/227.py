#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); ++i)

#define ld long double

pair<int, int> x[1000];
ld pi = acos(-1.0);

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		printf("Case #%d: ", tc);
		int n, k;
		scanf("%d%d", &n, &k);
		f(i, 0, n)scanf("%d%d", &x[i].first, &x[i].second);
		sort(x, x + n);
		multiset<ld> h;
		ld an = 0.0, H = 0.0;
		f(i, 0, n){
			ld t = (ll)x[i].second * x[i].first * 2 * pi;
			if ((int)h.size() + 1 == k)an = max(an, (ll)x[i].first * x[i].first * pi + H + t);
			h.insert(t);
			H += t;
			if ((int)h.size() == k)H -= *h.begin(), h.erase(h.begin());
		}
		printf("%.7lf\n", (double)an);
	}
}