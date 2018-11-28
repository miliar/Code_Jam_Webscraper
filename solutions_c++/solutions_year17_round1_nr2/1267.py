#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;
const double EPS = 1e-9;
double need[55];
double have[55][55];
int n, p;
struct XDD{
	int m,M,wh;
	friend bool operator < (XDD a, XDD b){return a.M > b.M;}
}rh[55][55],now[55];
bool cmp(XDD a, XDD b){
	return a.m < b.m;
}
void input(){
	scanf("%d %d",&n,&p);
	for(int i = 0 ;i < n ; i++){
		scanf("%lf",&need[i]);
	}
	for(int i = 0 ; i < n ;i++){
		for(int  j = 0 ;j < p ; j++){
			scanf("%lf",&have[i][j]);
		}
	}
}
void solve(){
	for(int i = 0 ;i < n ;i++){
		for(int j = 0 ;j < p ;j++){
			double M=have[i][j]/0.9 , m = have[i][j]/1.1,tmp;
			rh[i][j].M = floor(have[i][j]/0.9/need[i]);
			tmp = rh[i][j].M*need[i];
			if(!(m <= tmp+EPS && tmp <= M+EPS)){
				tmp--;
				if(m <= tmp+EPS && tmp <= M+EPS){
					rh[i][j].M=tmp;
				}else{
					rh[i][j].M = 0;
				}
			}
			rh[i][j].m = ceil(have[i][j]/1.1/need[i]);
			tmp = rh[i][j].M*need[i];
			if(!(m <= tmp+EPS && tmp <= M+EPS)){
				tmp++;
				if(m <= tmp+EPS && tmp <= M+EPS){
					rh[i][j].m=tmp;
				}else{
					rh[i][j].m = 0;
				}
			}
			rh[i][j].wh=i;
		}
	//	for(int j = 0 ;j < p ;j++){
	//		printf("[%d] %f %d %d\n",i,have[i][j],rh[i][j].m,rh[i][j].M);
	//	}
		sort(rh[i],rh[i]+p,cmp);
	}

	int ans = 0;
	int tp[55];
	fill(tp,tp+55,0);
	for(int i = 0 ;i < n ;i++){
		while(rh[i][tp[i]].m == 0){ 
			tp[i]++;
			if(tp[i] == p) goto end;
		}
		now[i] = rh[i][tp[i]++];
	}
	while(1){
		int l=now[0].m,r=now[0].M;
		int change=0;
		for(int i = 1 ;i < n ;i++){
			 l = max(l, now[i].m);
			 if(now[i].M < r){
				change = i;
			 }
			 r = min(r,now[i].M);
		}
		if(l <= r){
			ans++;
			for(int i = 0 ;i < n ;i++){
				if(tp[i] == p) goto end;
				now [i] = rh[i][tp[i]++];
			}
		}else{
			int i = change;
			if(tp[i] == p) goto end;
			now[i] = rh[i][tp[i]++];
		}
	}
	end:;
	printf("%d\n",ans);
}
int main(){
	int T;
	scanf("%d",&T);
	for(int i = 1 ;i <= T; i++){
		printf("Case #%d: ",i);
		input();
		solve();
	}
}
