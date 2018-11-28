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
#define clr(a,x) 					memset(a,x,sizeof(a)) //set elements of array to some value
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
typedef pair<int,int> pp;
typedef vector<pp> vpp ;
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

ll t,i,j,ans,r,c,R,C,s,m,n,k,u,v;
double p,q,res,mx,d;
vector<pair<double,double> > vv,uu;
bool comp(pair<double,double> a, pair<double,double> b){
    if(a.fi==b.fi)return a.se>b.se;
    return a.fi>b.fi;
}
bool comp2(pair<double,double> a, pair<double,double> b){
    return a.se>b.se;
}
int main(){
	boost
	fileio
	double a[1010],b[1010],c[1010];
	cin>>t;
	f1(u,1,t){

		cin>>n>>k;
        // cin>>a[0]>>b[0];
        mx = 0;
        // mx = d*b[0]/(d-a[0]);
        // cout<<a[0]<<" "<<b[0]<<" "<<mx<<endl;
        vv.clear();
        f(i,0,n){
            cin>>a[i]>>b[i];

            c[i]=2*a[i]*b[i];
            vv.pb(mp(a[i],c[i]));
        }
        sort(vv.begin(),vv.end(),comp);
        d=n;
        vector<pair<double,double> > :: iterator it,it2;
        for(it=vv.begin();it!=vv.end();it++){
            d++;
            if(d<k)
                break;
            res=(it->fi)*(it->fi)+it->se;
            it2=it;
            it2++;
            uu.clear();
            for(;it2!=vv.end();it2++)
                uu.pb(mp(it2->fi,it2->se));
            sort(uu.begin(),uu.end(),comp2);
            for(j=2;j<=k;j++){
                res+=uu[j-2].se;
            }
            if(res>mx)mx=res;
        }
		cout<<"Case #"<<u<<": "<<fixed<<setprecision(9)<<mx*PI<<endl;
	}
	return 0;
}
