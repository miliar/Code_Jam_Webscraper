#include <cstdio>
#include <map>
#include <cstdlib>
using namespace std;
typedef long long LL;
long long n, k;
void solve(){
	map< LL,LL > ma;
	ma[n]++;
	auto it = ma.begin();
	while(1){
//		printf("<LL,LL> %lld %lld\n",it->first,it->second);
		if(it->second<k){
			k -= it->second;
			LL tmp = it->first;
			tmp --;
			if(tmp % 2 ){
				ma[tmp/2] += it->second;
				ma[tmp/2+1] += it->second;
			}else{
				ma[tmp/2] += it->second*2;
			}
			it--;
		}else{
			LL tmp = it->first;
			if(tmp % 2){
				tmp = (tmp-1)/2;
				printf("%lld %lld\n",tmp,tmp);
			}else{
				tmp /= 2;
				printf("%lld %lld\n",tmp,tmp-1);
			}
			break;
		}
	}
}
int main(){
	int T;
	scanf("%d",&T);
	for(int i = 1 ;i <= T; i++){
		printf("Case #%d: ",i);
		scanf("%lld %lld",&n, &k);
		solve();
	}
}
