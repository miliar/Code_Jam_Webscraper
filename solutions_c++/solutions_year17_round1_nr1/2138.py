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
set<char> s;
queue<char> q;

ll exp(ll t,ll x){if(x==0) return 1;if(x==1) return t;if(x%2==1) return (t*exp((t*t)%MOD,x/2))%MOD;if(x%2==0) return exp((t*t)%MOD,x/2);} 
ll gcd(ll x,ll y){return x%y==0?y:gcd(y,x%y);}
ll lcm(ll x,ll y){return x*(y/gcd(x,y));}
bool isprime(ll x){for(ll i=2;i*i<=x;i++){if(x%i==0){return false;}}return true;}

char inpt[100][100];
void dfs(int a,int b,int r,int cl,char c){
    if (a>0&&inpt[a-1][b]=='?')
	{
		inpt[a-1][b]=c;
	        dfs(a-1,b,r,cl,c);
	}
    if (a<r&&inpt[a+1][b]=='?')
        {  
                inpt[a+1][b]=c;
                dfs(a+1,b,r,cl,c);
        }
}
void dfs2(int a,int b,int r,int cl,char c){
     if (b>0&&inpt[a][b-1]=='?')
        {  
                inpt[a][b-1]=c;
                dfs2(a,b-1,r,cl,c);
        }
    if (b<c&&inpt[a][b+1]=='?')
        {  
                inpt[a][b+1]=c;
                dfs2(a,b+1,r,cl,c);
        }
}
int main(){
  freopen("output.out","w",stdout);
  freopen("input.in","r",stdin);
  int n,r,c ;
  scanf("%d",&n);
  rep(t,1,n){
     scanf("%d %d",&r,&c);
     rep(i,0,r-1){
	cin>>inpt[i];
     }
     rep(i,0,r-1){rep(j,0,c-1){
	if (inpt[i][j]!='?')
	   dfs(i,j,r-1,c-1,inpt[i][j]);
	}
     }
     rep(i,0,r-1){rep(j,0,c-1){
        if (inpt[i][j]!='?')
           dfs2(i,j,r-1,c-1,inpt[i][j]);
        }
     }
     printf("Case #%d:\n",t);
     rep(i,0,r-1){
        cout<<inpt[i]<<endl;
     }
  }
  return 0;
}
