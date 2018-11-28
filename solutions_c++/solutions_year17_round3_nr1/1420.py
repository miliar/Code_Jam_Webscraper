#include <bits/stdc++.h>
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

vii p;
int n, k;

double area(int b){
	return acos(-1.0)*p[b].S*p[b].S + acos(-1.0)*2.0*p[b].S*p[b].F;
}

double latArea(int b){
	return acos(-1.0)*2.0*p[b].S*p[b].F;
}

double solve(int a){
	double ans = area(a);
	priority_queue<double> pq;
	for(int i = 0; i < n; i++){
		if(i == a) continue;
		if(p[i].S > p[a].S) continue;
		pq.push(latArea(i));
	}
	if(pq.size() < k-1) return 0;
	for(int i = 1; i < k; i++){
		ans += pq.top(); pq.pop();
	}
	return ans;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int caso = 1; caso <= T; caso++){
		p.clear();
		double ans = 0;
		scanf("%d %d",&n,&k);
		for(int i = 0; i < n; i++){
			ii x;
			scanf("%d %d",&x.S,&x.F);
			p.pb(x);
		}
		for(int i = 0; i < n; i++){
			ans = max(ans, solve(i));
		}
		printf("Case #%d: %.10lf\n",caso,ans);
	}
	return 0;
}
