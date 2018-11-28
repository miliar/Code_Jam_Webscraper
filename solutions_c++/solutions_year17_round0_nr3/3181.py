#include<map>
using namespace std;
void solve(){
	long long n,k;
	scanf("%lld %lld",&n,&k);
	map<long long,long long> m;
	m[n]=1;
	while(true){
		pair<long long,long long> x=*m.rbegin();
		m.erase(x.first);
		x.first--;
		long long a=x.first/2;
		long long b=x.first-a;
		if(x.second>=k){	
			printf("%lld %lld\n",max(a,b),min(a,b));
			return;
		}
		k-=x.second;
		m[a]+=x.second;
		m[b]+=x.second;
	}
}
int main(){
	int tc;
	scanf("%d",&tc);
	for(int i=1;i<=tc;i++){
		printf("Case #%d: ",i);
		solve();
	}
}