#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pl;
typedef vector<pl> vpl;

bool cmp(const pl& p1, const pl& p2){
	return (p1.first*p1.second > p2.first*p2.second);
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t){
		int K, N;
		scanf("%d %d", &N, &K);
		vpl p(N);
		for (int i = 0; i < N; ++i){
			scanf("%lld %lld", &p[i].first, &p[i].second);
		}
		sort(p.begin(), p.end());
		reverse(p.begin(), p.end());
		long double area, mx;
		for (int i = 0; i <= N - K; ++i){
			area = p[i].first*(p[i].first + 2*p[i].second);
			vpl q = p;
			sort(q.begin() + i + 1, q.end(), cmp);
			for (int j = i + 1; j < i + 1 + K - 1; ++j)
				area += 2*q[j].first*q[j].second;
			if (i == 0) mx = area;
			else mx = max(mx, area);
		}
		printf("Case #%d: %.10Lf\n", t, M_PI*mx);
	}
	return 0;
}
