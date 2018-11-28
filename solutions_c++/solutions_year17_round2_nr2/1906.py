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

int n;
char names[]={' ','R','O','Y','G','B','V'};
int colors[6];
		        //r     o   y      g    b       v
int relations[][3]={{},{4,3,5},{5},{6,1,5},{1},{2,3,1},{3}};
int places[1005];
int cases;

bool isOneColor(int c){
     return c==1||c==3||c==5;
}
bool isAllowed(int c1,int c2){
     rep(i,0,2)
	if (relations[c1][i]==c2)return true;
     return false;
}
bool fill(int p,int next){
     int c=places[p];
     int nextp=p+next;
     if (nextp==n+1){nextp=1;
	int nextc=places[nextp];
	return isAllowed(c,nextc);
     }

     if (!isOneColor(c)){
	  int newc=relations[c][0];
	  if (colors[newc]<=0)return false;
	  colors[newc]--;
	  places[nextp]=newc;
	  return fill(nextp,next);
     }else{
	  int newc=relations[c][0];
          if (colors[newc]>0){
              colors[newc]--;
              places[nextp]=newc;
              return fill(nextp,next);
	  }else{
	        int c1=relations[c][1];
		int c2=relations[c][2];
		int choice;
	        if (colors[c1]>=colors[c2])
			choice=c1;
		else
			choice=c2;
		if (colors[choice]<=0)return false;
		colors[choice]--;
                places[nextp]=choice;
	        return fill(nextp,next);
	  }
     }
}
int main(){
  freopen("output.txt","w",stdout);
  freopen("input.in","r",stdin);
  scanf("%d",&cases);
  rep(t,1,cases){
	_(places,0);
	scanf("%d %d %d %d %d %d %d",&n,&colors[1],&colors[2],&colors[3]
				,&colors[4],&colors[5],&colors[6]);
        rep(i,1,6)
	   if (colors[i]>0){
		places[1]=i;
		colors[i]--;
		break;
	   }
	printf("Case #%d: ",t);
	bool ans=fill(1,1);
	if (n==1)ans=true;
	if (ans){
  	   rep(i,1,n)cout<<names[places[i]];
	   cout<<endl;
	}else{
	   printf("IMPOSSIBLE\n");
	}
  }
  return 0;
}
