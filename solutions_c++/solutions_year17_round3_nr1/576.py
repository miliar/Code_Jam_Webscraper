#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pp;
typedef pair<ll,ll> pll;
void read(int& x){ scanf("%d",&x); }
void read(ll& x){ scanf("%lld",&x); }
template<typename T,typename... Args>
void read(T& a,Args&... b){ read(a); read(b...); }
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define x first
#define y second

int n, k;
pp data[1010];

const double pi = acos(-1);

double c(double x){ return pi*x*x; }
double ar(double r, double h){ return pi*r*h*2; }

void work(){
	read(n, k);
	for(int i=1; i<=n; ++i){
		read(data[i].x, data[i].y);
	}
	double ans = 0;
	for(int i=1; i<=n; ++i){
		priority_queue<double> hs;
		for(int j=1; j<=n; ++j) if(i!=j && data[j].x <= data[i].x){
			hs.emplace(data[j].y*1.0*data[j].x);
		}
		double cur=c(data[i].x) + ar(data[i].x, data[i].y);
		bool no = false;
		for(int i=1; i<k; ++i){
			if(hs.empty()){
				no=1;
				break;
			}
			cur += hs.top()*2*pi; hs.pop();
		}
		if(!no) ans=max(ans, cur);
	}
	printf("%.10f\n", ans);
}

int main()
{
	freopen("in_b", "r", stdin);
	freopen("out_b", "w", stdout);
	int tc; read(tc);
	for(int i=1; i<=tc; ++i){
		printf("Case #%d: ", i);
		work();
	}
    return 0;
}
