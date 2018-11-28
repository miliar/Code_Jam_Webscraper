#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <time.h>
#include <string.h>
#include <queue>
#include <stack>
#include <cstring>
using namespace std;
#define MOD 1000000007
#define ll long long int
#define rep(i,a,b) for(int (i) = (a) ; (i) <= (b) ; (i)++)
#define per(i , a , b) for(int (i) = (a) ; (i) >= (b) ; (i)--)

ll exp(ll t,ll x){if(x==0) return 1;if(x==1) return t;if(x%2==1) return (t*exp((t*t)%MOD,x/2))%MOD;if(x%2==0) return exp((t*t)%MOD,x/2);} 
ll gcd(ll x,ll y){return x%y==0?y:gcd(y,x%y);}
ll lcm(ll x,ll y){return x*(y/gcd(x,y));}
bool isprime(ll x){for(ll i=2;i*i<=x;i++){if(x%i==0){return false;}}return true;}

void split(ll num,ll &l,ll &r){
     num-=1;
     l=num/2+num%2;
     r=num/2;
}
ll k,n;
ll getLast(){
    priority_queue<ll> q;
    map<ll,ll> M;
    M[k]=1;
    q.push(k);
    
    ll x,y;
    ll num=q.top();
    q.pop();
    ll c=M[num];
    ll prev=-1;
    while (c<n){
        prev=num;
	n-=c;
	split(num,x,y);
        if (M[x]==0)
	   q.push(x);
        if (M[y]==0)
	   q.push(y);
	M[x]+=c;
	M[y]+=c;
	while (!q.empty()&&num==prev){
	   num=q.top();
	   q.pop();
        }
        c=M[num];
	//printf("%lld %lld %lld\n",num,c,n);
    }
    return num;
}
int main(){
  freopen("output.txt","w",stdout);
  freopen("C.in","r",stdin);
  int cases;
  ll res,x,y;
  scanf("%d",&cases);
  rep(t,1,cases){
	cin>>k>>n;
	res=getLast();
	split(res,x,y);
	printf("Case #%d: ",t);
	cout<<x<<" "<<y<<endl;
  }
  return 0;
}
