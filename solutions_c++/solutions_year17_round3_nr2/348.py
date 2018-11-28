#include <cstdio>
#include <cstdlib>
#include <queue>
#include <algorithm>
using namespace std;
struct XDD{
	int s,e,w;
	friend bool operator < (XDD a, XDD b){
		return a.s < b.s;
	}
}x[202];
struct QAQ{
	int a,w;
	friend bool operator <(QAQ a, QAQ b){
		return a.a > b.a;
	}
};
int na,nb,ta,tb;
void input(){
	ta = tb = 0;
	scanf("%d %d",&na,&nb);
	for(int i = 0 ;i < na ;i ++){
		scanf("%d %d", &x[i].s, &x[i].e);
		ta += x[i].e-x[i].s;
		x[i].w = 0;
	}
	for(int i = 0 ;i < nb ;i ++){
		scanf("%d %d", &x[i+na].s, &x[i+na].e);
		tb += x[i+na].e-x[i+na].s;
		x[i+na].w = 1;
	}
	sort(x,x+na+nb);
}
void solve(){
	priority_queue<QAQ> he;
	if(na+nb == 2){
		if(x[0].w == x[1].w){

			int tmp = min(x[1].s-x[0].e,
			x[0].s+1440-x[1].e);
			he.push((QAQ){tmp,x[0].w});
		}
	}else{
		for(int i = 0 ;i < na+nb-1 ;i++){
			if(x[i].w == x[i+1].w){
				he.push((QAQ){x[i+1].s-x[i].e,x[i].w });
			}
		}
		if(x[0].w == x[na+nb-1].w)
			he.push( (QAQ){x[0].s+1440-x[na+nb-1].e,x[0].w} );
	}
	while(!he.empty()){
		QAQ now = he.top();he.pop();
		if(now.w == 0){
			if(ta+now.a <= 720){
				na--;
				ta += now.a;
			}
		}else{
			if(tb + now.a <= 720){
				nb--;
				tb += now.a;
			}
		}
	}
	printf("%d\n",max(na,nb)*2);

}
int main(){
	int T;
	scanf("%d",&T);
	for(int qq = 1 ; qq <= T ;qq++){
		printf("Case #%d: ",qq);
		input();
		solve();
	}
}
