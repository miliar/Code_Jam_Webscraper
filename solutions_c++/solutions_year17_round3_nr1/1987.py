#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cstring>

using namespace std;
typedef long long ll;
class cake{
public:
	ll r;
	ll h;
	cake(){r=0;h=0;};
	cake(ll a,ll b){r = a;h = b;};
	
	/*bool operator < (const cake &b)const{
		if(h!=b.h) return h<b.h;
		else return r<b.r;
	}
	bool operator > (const cake &b)const{
		if(h!=b.h) return h>b.h;
		else return r>b.r;
	}*/
};

bool cmp (cake a,cake b){
	if(a.r!=b.r) return a.r<b.r;
	else return a.h<b.h;
}
bool cmp2 (cake a,cake b){
	if(a.h*a.r!=b.h*b.r) return a.h*a.r<b.h*b.r;
	else return a.r<b.r;
}

cake data[1005];

int n,k;
double pi;
inline ll maxi(ll a,ll b){return a>b?a:b;}
int main(){
	pi = acos(-1);
	int t;
	scanf("%d",&t);
	for(int co=1;co<=t;co++){
		scanf("%d%d",&n,&k);
		//ll ma = 0;
		for(int g=0;g<n;g++){
			scanf("%lld%lld",&data[g].r,&data[g].h);
			//ma = maxi(ma,data[g].r);
		}
		sort(data,data+n,cmp);
		double ans = 0.0;
		double fi_ans = 0.0;
		for(int g=n-1;g>=0;g--){
			ll ttt = (data[g].r*data[g].r);
			ll temp = 0;
			temp += data[g].h * data[g].r;
			//ans += pi*2.0*data[g].h * data[g].r;
			sort(data,data+g,cmp2);
			for(int h=g-1;h>g-k;h--){
				if(h==-1){
					ans = -1.0;
					break;
				}
				temp += data[h].h * data[h].r;
			}
			if(ans>=-0.5){
				ans = (temp * 2 + ttt) * pi;
			}
			if(ans > fi_ans) fi_ans = ans;
			ans = 0.0;
			sort(data,data+n,cmp);
		}
		printf("Case #%d: %.9lf\n",co,fi_ans);
		
		
	}
	
	
}