#include<bits/stdc++.h>
#define IN freopen("in.txt","r",stdin);
#define OUT freopen("out.txt","w",stdout);
using namespace std;
typedef long long ll;
ll n;
int main(){
	IN
	OUT
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++){
		cin>>n;
		ll t = 1e18,v;
		int last =0;
		ll ans = n;
		while(t){
			int now = n/t%10;
			if(now<last){
				//cout<<t<<' '<<v<<endl;
				ans =(n/v-1)*v+v-1;
				break;
			} else if(now>last) v = t;
			last = now;
			t/=10;
		}
		printf("Case #%d: %lld\n",test,ans);
	}
	return 0;
}
