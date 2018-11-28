#include <bits/stdc++.h>

using namespace std;

typedef long long          	ll;
typedef long long unsigned 	llu;
typedef double             	dl;
typedef pair<int,int>      	pii;
typedef pair<ll,ll>     	pll;
typedef vector<int>        	vi;
typedef vector<ll>        	vl;
typedef map<int,int> 		mii;
typedef map<ll,ll>         	mll;
typedef map<string,int>    	msi;
typedef map<char,int>      	mci;
typedef pair<int ,pii>      piii;
typedef vector<pii>         vpii;
typedef vector<piii>        vpiii;

#define pi                  acos(-1.0)
#define S                   second
#define F                   first
#define pb                  push_back
#define mkp                 make_pair
#define mem(a,b)            memset(a,b,sizeof a)
#define all(v)              v.begin(),v.end()
#define vsort(v)            sort(v.begin(),v.end())
#define IO                  ios_base::sync_with_stdio(false);cin.tie(NULL)
#define gcd(a,b)            __gcd(a,b)
#define FOR(i,a,b)			for(int i=a;i<=b;i++)
#define RFOR(i,a,b)			for(int i=a;i>=b;i--)

#define I(a)                scanf("%d",&a)
#define I2(a,b)             scanf("%d%d",&a,&b)
#define L(a)                scanf("%lld",&a)
#define L2(a,b)             scanf("%lld%lld",&a,&b)
#define D(a)                scanf("%lf",&a)

#define SP                  cout<<" ";
#define PI(a)               printf("%d",a)
#define PL(a)               printf("%lld",a)
#define PD(a)               printf("%lf",a)
#define CHK                 cout<<"MK"<<endl

template <class T> inline T BMOD(T p,T e,T m){T ret=1;while(e){if(e&1) ret=(ret*p)%m;p=(p*p)%m;e>>=1;}return (T)ret;}
template <class T> inline T MODINV(T a,T m){return BMOD(a,m-2,m);}
template <class T> inline T isPrime(T a){for(T i=2;i<=sqrt(double(a));i++){if(a%i==0){return 0;}}return 1;}
template <class T> inline T lcm(T a, T b){return (a/gcd(a,b))*b;}
template <class T> inline T power(T a, T b){return (b==0)?1:a*power(a,b-1);}
template <class T> inline string toString(T t) { stringstream ss; ss<<t; return ss.str();}
template <class T> inline long long toLong(T t) {stringstream ss;ss<<t;long long ret;ss>>ret;return ret;}
template <class T> inline int toInt(T t) {stringstream ss;ss<<t;int ret;ss>>ret;return ret;}
template <class T> inline bool leapYear(T t){if(!(t%(T)400) || (!(t%(T)4) && t%(T)100)) return true; return false;}

//~ cout << fixed << setprecision(20) << Ans << endl;
//~ priority_queue<piii,vpiii, greater<piii> >pq; //for dijkstra
/*                 _                      */
/*____________|\/||_||\||_________________*/

string buffer;
int INT(){
	getline(cin,buffer);
	return toInt(buffer);
}
int LONG(){
	getline(cin,buffer);
	return toLong(buffer);
}

const int MX = 100010;
const ll  MD = 1e9+7;
#define inf 1e9
int ar[MX];
int sv[1500][5][1500];
int st;
int go(int p,int pr,int a)
{
    if(p==1440){
        int b = 1440 - a;
        int ret;
        if(pr!=st) ret = 1;
        else ret = 0;
        if(a==b && a==720){
			return ret;
		}
        return inf;
    }
    int &ret = sv[p][pr][a];
    if(ret!=-1) return ret;
    ret = inf;
    if(ar[p])
    {
        int add = (ar[p]==1)?1:0;
        int cst = ( pr!=0 && pr!=ar[p] )?1:0;
        ret = go(p+1,ar[p],a+add) + cst;
    }
    else{
        int cst = (pr==2 ? 1:0 );
        int x = go(p+1,1,a+1) + cst;
        cst = (pr==1 ? 1:0 );
        int y = go(p+1,2,a)+ cst;
        ret = min(x,y);
    }
    return ret;
}

int main()
{
	IO;
    freopen("B-large.in","r",stdin);
    freopen("Bout2.out","w",stdout);
    int tc,cs=0,a,b,x,y;
    cin>>tc;
	while(tc--){
        cin>>a>>b;
        mem(ar,0);
        for(int i=1;i<=a;i++){
            cin>>x>>y;
            for(int j=x;j<y;j++){
				ar[j] = 1;
			}
        }
        for(int i=1;i<=b;i++){
            cin>>x>>y;
            for(int j=x;j<y;j++){
				ar[j] = 2;
			}
        }
        int Ans = 0;
        mem(sv,-1);

        if(ar[0])
        {
            st = ar[0];
            Ans = go(0,0,0);
        }
        else
        {
            st = 1;
            int ret1 = go(1,1,1);
            Ans = ret1;
            mem(sv,-1);
            st = 2;
            int ret2 = go(1,2,0);
            Ans = min(ret1,ret2);
        }
        cout<<"Case #"<<++cs<<": "<<Ans<<endl;
    }
    return 0;
}


