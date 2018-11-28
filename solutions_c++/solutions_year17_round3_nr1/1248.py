#include <bits/stdc++.h>
#define LL long long
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
using namespace std;

typedef pair<LL,LL> ii;
int T;
LL n,m;
ii a[1010];

LL area(LL r, LL h){
	return r*r + r*2ll*h;
}

bool cmp(ii x, ii y){
	if(area(x.fi, x.sc) == area(y.fi, y.sc)) return x.fi > y.fi;
	return area(x.fi, x.sc) > area(y.fi, y.sc);
}

bool cmp2(ii x, ii y){
	return (x.fi*2*x.sc)>(y.fi*2*y.sc);
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%d",&T);
	for(int tc=1;tc<=T;tc++){
		scanf("%lld %lld",&n,&m);
		for(int i=0;i<n;i++) scanf("%lld %lld",&a[i].fi,&a[i].sc);
		
		bool used[1010]={0};
		LL mx = 0;
		vector<ii> v;
		for(int i=0;i<n;i++){
			LL idx = 0;
			v.clear();
			LL sum = a[i].fi*a[i].fi+a[i].fi*2*a[i].sc;
			for(int j=0;j<n;j++) if(j!=i) v.pb(a[j]);
			sort(v.begin(), v.end(), cmp2);
			for(int j=0;j<m-1;j++){
				sum += v[j].fi*2*v[j].sc;
			}
			mx = max(mx, sum);
		}
		
		printf("Case #%d: %.10lf\n", tc, (double)mx*3.14159265358979323846);
	}
	return 0;
}
