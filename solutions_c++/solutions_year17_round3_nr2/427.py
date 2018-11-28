#include <cmath>
#include <climits>
#include <queue>
#include <vector>
#include <map>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>  // istringstream buffer(myString);
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include<bits/stdc++.h>

using namespace std;

#define bit(x,i) 					(x&(1<<i))  		//select the bit of position i of x
#define lowbit(x) 					((x)&((x)^((x)-1))) //get the lowest bit of x
//#define hBit(msb,n) 				asm("bsrl %1,%0" : "=r"(msb) : "r"(n)) //get the highest bit of x, maybe the fastest
#define max(a,b) 					(a<b?b:a)
#define f(i,L,R) 					for (i = L; i < R; i++) //next four are for "for loops"
#define f1(i,L,R) 					for (i = L; i <= R; i++)
#define fd(i,L,R) 					for (i = L; i > R; i--)
#define fd1(i,L,R) 					for (i = L; i >= R; i--)
#define si(a) 						scanf("%d", &a)
#define sl(a) 						scanf("%lld", &a)
#define sc(a) 						scanf("%c", &a)
#define ss(a) 						scanf("%s",a)
#define clr(a,x) 					memset(a,x,sizeof(a)) //set elements of array to some bbue
#define sz(x) 						((int)(x).size())
#define each(i,t) 					for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++) // traverse an STL data structure
#define ALL(c) 						(c).begin(),(c).end() //handy for function like "sort()"
#define PRESENT(c,x) 				((c).find(x) != (c).end())
#define CPRESENT(c,x) 				(find(ALL(c),x) != (c).end())
#define ll 							long long
#define boost 						ios_base::sync_with_stdio(false); //to synchronize the input of cin and scanf
#define fileio 						freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);
#define trace1(x)                	cerr << #x << ": " << x << endl;
#define trace2(x, y)             	cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          	cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;

//for map, pair
#define mp make_pair
#define fi first
#define se second

#define MAXN 	10000
const long long mod=1000000007 ;
#define inf 	0x7fffffff
#define PI 		3.1415926535897932384626

//for vectors
#define pb push_back
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> VI ;
typedef vector<VI> VVI;
typedef pair<ll,ll>  PP;
typedef vector<PP>  VPP ;

// directions
const int fx[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
const int fxx[8][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};

ll powmod(ll a,ll b) {ll res=1;if(a>=mod)a%=mod;for(;b;b>>=1){if(b&1)res=res*a;if(res>=mod)res%=mod;a=a*a;if(a>=mod)a%=mod;}return res;}
int powab(ll a,int b) {ll res=1;for(;b;b>>=1){if(b&1)res=res*a;a=a*a;}return res;}
ll gcd(ll a , ll b){return b==0?a:gcd(b,a%b); }

ll t,i,j,ans,r,c,R,C,m,n,k,u,v;

ll K,w[1500],dp[1500][730][2],s[10010],start;
ll p,c1=1,max1=0,a,b,x,y;

 ll func(ll i,ll bb,ll p)
 {
     if(dp[i][bb][p]!=-1)
     return dp[i][bb][p];
     if(i==1440)
     {
         if(bb!=720)
         {
             return 5000;
         }
         if(p!=start)
         {
             return 1;
         }
         else
         {
             return 0;
         }
     }
     if(bb>720)
     {
         return 50000;
     }
     if(i-bb>720)
     {
         return 50000;
     }
    if(s[i]==0)
    {
        if(p==0)
            dp[i][bb][p]= func(i+1,bb+1,p);
        else
            dp[i][bb][p]= 1+func(i+1,bb+1,1-p);
        return dp[i][bb][p];
    }
    if(s[i]==1)
    {
        if(p==0)
            dp[i][bb][p]= 1+func(i+1,bb,1-p);
        else
            dp[i][bb][p]= func(i+1,bb,p);
        return dp[i][bb][p];
    }
    if(p==0)
    {
        dp[i][bb][p]= min(func(i+1,bb+1,p),1+func(i+1,bb,1-p));
        return dp[i][bb][p];
    }
    else
    {
        dp[i][bb][p]= min(func(i+1,bb,p),1+func(i+1,bb+1,1-p));
        return dp[i][bb][p];
    }

 }


int main(){
	boost
	fileio
	cin>>t;
	f1(u,1,t){

		cin>>n>>m;
        memset(s,-1,sizeof(s));
        for(i=0;i<n;i++)
        {
            cin>>x>>y;
            for(j=x;j<y;j++)
            {
                s[j]=1;
                w[j]=y;
            }
        }
        for(i=0;i<m;i++)
        {
            cin>>x>>y;
            for(j=x;j<y;j++)
            {
                s[j]=0;
                w[j]=y;

            }
        }
        start=0;
        memset(dp,-1,sizeof(dp));
        ll res=func(0,0,0);
        start=1;
        memset(dp,-1,sizeof(dp));
         res=min(func(0,0,1),res);
		cout<<"Case #"<<u<<": "<<res<<endl;
	}
	return 0;
}
