#include<bits/stdc++.h>
using namespace std;
#define sl(n) scanf("%lld",&n)
#define debug(n) printf("%lld\n",n)
typedef long long int ll;
//#define INPUT
#define mp make_pair
#define f first
#define s second
int main(){
	#ifdef INPUT
       freopen("input.cpp", "r", stdin);
       freopen("output.cpp", "w", stdout);
   	#endif
   	ll z;sl(z);
   	for(ll t=1;t<=z;t++){
   		ll n,k;
   		sl(n);sl(k);
   		map<ll,ll> m;
   		m[n]=1;
   		ll max=n;
   		set<ll> s;
   		s.insert(n-n);
   		ll j;
   		ll ans1=0,ans2=0;
   		priority_queue<ll> q;
   		q.push(n);
   		for(j=k;j>=1;){
   			max=q.top();q.pop();
   			ll p = m[max];
   			if(p>=j){
   				if(max%2==0){
   					ans1=max/2;
   					ans2=(max/2)-1;
   				}else{
   					ans1=ans2=max/2;
   				}
   				break;
   			}else{
   				j-=p;
   				if(max%2==0){
   					if(m.find((max/2)-1)!=m.end()){
   						m[(max/2)-1]=m[(max/2)-1]+p;
   					}else{
   						q.push((max/2)-1);
   						m[(max/2)-1]=p;
   					}
   					if(m.find(max/2)!=m.end()){
   						m[max/2]=m[max/2]+p;
   					}else{
   						q.push(max/2);
   						m[max/2]=p;
   					}
   					
   				}else{
   					if(m.find(max/2)!=m.end()){
   						m[max/2]=m[max/2]+2*p;
   					}else{
   						q.push(max/2);
   						m[max/2]=2*p;
   					}
   				}
   			}	
   		}
   		printf("Case #%lld: %lld %lld\n",t,ans1,ans2);
   	}
}
