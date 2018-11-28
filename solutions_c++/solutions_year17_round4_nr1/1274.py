#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int n, p;
int x[105],cnt[5];
void input(){
	scanf("%d %d",&n,&p);
	for(int i = 0 ;i < n; i++)scanf("%d",&x[i]);
	for(int i = 0 ;i < 5 ;i++)cnt[i] = 0;
}
void solve(){
	int ans=0,tp=0;
	for(int i = 0 ;i < n ;i++){
		x[i] %= p;
		cnt[ x[i] ] ++;
	}
	ans += cnt[0];
	if( p == 2 ){
		ans += cnt[1]/2 + cnt[1]%2;
	}else if( p == 3 ){
		int tmp = min(cnt[1],cnt[2]);
		ans += tmp;
		tmp = cnt[1]+cnt[2]-tmp*2;
		ans += tmp/3 + (tmp%3 != 0);
	}else{
		ans += cnt[2]/2;
		cnt[2] %= 2;
		int tmp = min(cnt[1],cnt[3]);
		ans += tmp;
		tmp = cnt[1]+cnt[3] - tmp*2;
		if(cnt[2]){
			if(tmp >= 2){
				ans ++;
				tmp -=2;
			}else if(tmp == 0){
				ans ++;
			}
		}
		ans += tmp/4 + (tmp%4 != 0);

	}
	printf("%d\n",ans);

}
int main(){
	int T;
	scanf("%d",&T);
	for(int t = 1 ; t <= T ;t++){
		printf("Case #%d: ",t);
		input();
		solve();
	}
}
