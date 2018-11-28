#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int n,k;
const double EPS = 1e-15;
double mon,now[55];
void input(){
	scanf("%d %d",&n,&k);
	scanf("%lf",&mon);
	for(int i = 0 ;i < n; i++){
		scanf("%lf",&now[i]);
	}
	sort(now,now+n);
}
bool check(double c){
	double q = mon;
	for(int i = 0 ;i < n; i++){
		if(c < now[i])return true;
		q -= c-now[i];
		if(q < 0.0) return false;
	}
	return true;
}
void solve(){
	double l = 0, r= 1.0,mid;
	while(r - l > EPS){
//		printf("q %f %f\n",l,r);
		mid = (l+r)/2.0;
		if(check(mid)){
			l=mid;
		}else{
			r=mid;
		}
	}
	double ans = 1;
	for(int i = 0 ;i < n; i++){
		ans *= max(l,now[i]);
	}
	printf("%.10f\n",ans);
}
int main(){
	int T;
	scanf("%d",&T);
	for(int q = 1 ;q <= T ; q++){
		printf("Case #%d: ",q);
		input();
		solve();
	}
}
