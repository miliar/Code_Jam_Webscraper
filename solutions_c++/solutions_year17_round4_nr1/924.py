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

ll t,i,j,ans,r,y,b,o,g,c,R,C,s,m,n,k,u,v;
double p,q,res,mx,d;
ll a[110];

int main(){
	boost
	fileio
	cin>>t;
    // list<char> s;
    // list<char>:: iterator it,it2;
	f1(u,1,t){
		cin>>n>>m;
        f(i,0,n){
            cin>>a[i];
        }
        if(m==2){
            b=0;c=0;
            f(i,0,n){
                if(a[i]%2)
                    b++;
                else c++; 
            }
            cout<<"Case #"<<u<<": "<<c+(b+1)/2<<endl; 
        }
        else if(m==3){
            b=0;c=0;g=0;
            f(i,0,n){
                if(a[i]%3==1){
                    c++;
                }
                else if(a[i]%3==2)
                    g++;
                else
                    b++;
            }
            k=c;v=g;
            ans=0;
            ans+=b;
            ans+=min(c,g);
            c-=min(k,v);
            g-=min(k,v);
            ans+=int(ceil(double(c+g)/3.0));
            cout<<"Case #"<<u<<": "<<ans<<endl;             
        }
        else{
            b=0;c=0;g=0;o=0;
            f(i,0,n){
                if(a[i]%4==0){
                    b++;
                }
                else if(a[i]%4==1)
                    c++;
                else if(a[i]%4==2)
                    g++;
                else
                    o++;
            }
            k=c;v=g;s=o;
            ans=0;
            ans+=b;
            ans+=g/2;
            g=g%2;
            ans+=min(c,o);
            c-=min(c,o);
            o-=min(k,s);
            if(g==1){
                if(c==0 && o>=2){
                    ans+=1;
                    o-=2;
                    g--;
                }
                else if(c>=2){
                    ans+=1;
                    c-=2;
                    g--;
                }
            }
            if(g==0){
                ans+=int(ceil(double(c+o)/4.0));
            }
            else{
                ans++;
            }
            cout<<"Case #"<<u<<": "<<ans<<endl;             
        }
    }
	return 0;
}