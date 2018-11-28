#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
using namespace std;
const double PI = 3.141592653589793238462643383;
struct XDD{
	double r,h;
	friend bool operator <(XDD a, XDD b){
		return a.h > b.h;
	}
}x[1006];
bool cmp (XDD a, XDD b){
	return a.r < b.r;
}
int n,need;
void input(){
	scanf("%d %d",&n,&need);
	for(int i = 0 ;i < n ;i++){
		scanf("%lf %lf",&x[i].r,&x[i].h);
		x[i].h *= 2.0*x[i].r;
	}
	sort(x,x+n,cmp);
}
void solve(){
	priority_queue<XDD> he;
	double nh = 0,ans = 0;

	for(int i = need-1 ;i < n ;i++){
		double nr = x[i].r;
		sort(x,x+i);
		nh = x[i].h;
		for(int j = 0 ;j < need -1 ;j++){
			nh += x[j].h;
		}
		ans = max((nh+x[i].r*x[i].r)*PI,ans);
	}
	printf("%.10f\n",ans);
}
int main(){
	int T;
	scanf("%d",&T);
	for(int qq = 1 ;qq <= T; qq++){
		printf("Case #%d: ",qq);
		input();
		solve();
	}
}
