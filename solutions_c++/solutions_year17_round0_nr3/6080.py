#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	//freopen("C-small-2-attempt0.in","r",stdin);
	//freopen("1.txt","w",stdout);
	ll n,k;
	int T,TT=0;
	scanf("%d",&T);
	while(T--){
		scanf("%lld%lld",&n,&k);
		k--;
		printf("Case #%d: ",++TT);
		//cout<<n<<" "<<k+1<<endl;
		priority_queue<ll> q;
		q.push(n);
		ll cnt=1;
		while(k--){
			ll x=q.top();	q.pop();
			if(x&1)
				q.push((x-1)>>1),q.push(((x-1)>>1));
			else
				q.push((x-1)/2+1),q.push(((x-1)>>1));
			/*if(x&1){
				if(cnt<k)
					q.push((x-1)>>1),q.push(((x-1)>>1)),cnt++;
				else
					q.push(((x-1)>>1));
			}
			else{
				if(cnt<k)
					q.push((x-1)/2+1),q.push(((x-1)>>1)),cnt++;
				else
					q.push((x-1)/2+1);
			}*/
		}
		ll x=q.top();	q.pop();
		if(x&1)
			printf("%lld %lld\n",(x-1)>>1,(x-1)>>1);
		else
			printf("%lld %lld\n",(x-1)/2+1,(x-1)>>1);
	}
	return 0;
}
/*
1
999 127

*/
