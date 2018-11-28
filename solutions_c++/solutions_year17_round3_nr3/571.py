#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pp;
typedef pair<ll,ll> pll;
void read(int& x){ scanf("%d",&x); }
void read(ll& x){ scanf("%lld",&x); }
void read(double& x){ scanf("%lf",&x); }
template<typename T,typename... Args>
void read(T& a,Args&... b){ read(a); read(b...); }
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define x first
#define y second

#define CASE "small"

int n, k;
double u, p[52];
void work(){
	read(n, k);
	read(u);
	for(int i=1; i<=n; ++i) read(p[i]);
	sort(p+1, p+n+1);
	p[n+1]=1;
	for(int i=1; i<=n; ++i){
		if(u < i*(p[i+1]-p[i])){
			for(int j=1; j<=i; ++j){
				p[j] += u/i;
			}
			break;
		}
		u -= i*(p[i+1]-p[i]);
		for(int j=1; j<=i; ++j) p[j]=p[i+1];
	}
	double ans=1;
	for(int i=1; i<=n; ++i) ans*=p[i];
	printf("%.10f\n", ans);
}

int main()
{
	freopen(CASE ".in", "r", stdin);
	freopen(CASE ".out", "w", stdout);
	int tc; read(tc);
	for(int i=1; i<=tc; ++i){
		printf("Case #%d: ", i);
		work();
		fprintf(stderr, "Done case %d/%d\n", i, tc);
	}
    return 0;
}
