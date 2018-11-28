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
#define _(a,b) memset( a, b, sizeof( a ) )
#define citer(ittype,it,cont) for (ittype::iterator it=cont.begin();it!=cont.end();it++)
#define rciter(ittype,it,cont) for (ittype::reverse_iterator it=cont.rbegin();it!=cont.rend();it++)
#define vint vector<int>
#define pb push_back

/*
struct thing
{
    int a;
    ll b;
    int id;
    bool operator<(const thing &o) const
    {
        return (b<o.b)||(b==o.b&&id<o.id);
    }
};
priority_queue<thing> pq;
*/
ll exp(ll t,ll x){if(x==0) return 1;if(x==1) return t;if(x%2==1) return (t*exp((t*t)%MOD,x/2))%MOD;if(x%2==0) return exp((t*t)%MOD,x/2);} 
ll gcd(ll x,ll y){return x%y==0?y:gcd(y,x%y);}
ll lcm(ll x,ll y){return x*(y/gcd(x,y));}
bool isprime(ll x){for(ll i=2;i*i<=x;i++){if(x%i==0){return false;}}return true;}
void swap(int &a,int &b){
	int t=a;
	a=b;
	b=t;
}
int main(){
  freopen("output.txt","w",stdout);
  freopen("input.in","r",stdin);
  int cases,d,n;
  int ds[1004];
  int vs[1004];
  double ans;
  scanf("%d",&cases);
  rep(t,1,cases){
	scanf("%d %d",&d,&n);
	rep(i,0,n-1)
	     scanf("%d %d",&ds[i],&vs[i]);
	
	rep(i,0,n-2)
	    rep(j,i+1,n-1)
		if (ds[i]<ds[j]){
			swap(ds[i],ds[j]);
			swap(vs[i],vs[j]);
		}
	
	double time=(d-ds[0])/double(vs[0]);
	rep(i,1,n-1){
	      double vn=(d-ds[i])/time;
	      if (vn>vs[i])
		  time=(d-ds[i])/double(vs[i]);
	}
	ans=d/time;
	printf("Case #%d: %.6f\n",t,ans);
  }
  return 0;
}
