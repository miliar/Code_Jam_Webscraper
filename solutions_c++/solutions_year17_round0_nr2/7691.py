#include <bits/stdc++.h>

#define LOCAL 1

#define lli long long int
#define llu unsigned long long int
#define ld long double
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define si(n) scanf("%d",&n)
#define slli(n) scanf("%lld",&n);
#define ss(n) scanf("%s",n);

const long double EPS = 1e-10;
const int MOD = 1000000007ll;
const int mod1 = 1000000009ll;
const int mod2 = 1100000009ll;
int INF = (int)1e9;
lli INFINF = (lli)1e18;
int debug = 0;
long double PI = acos(-1.0);

using namespace std;

int bit_count(lli _x){lli _ret=0;while(_x){if(_x%2==1)_ret++;_x/=2;}return _ret;}
int bit(lli _mask,int _i){return (_mask&(1ll<<_i))==0?0:1;}
int add(int a,int b,int m=MOD){int x=a+b;while(x>=m)x-=m;while(x<0)x+=m;return x;}
int sub(int a,int b,int m=MOD){int x=a-b;while(x<0)x+=m;while(x>=m)x-=m;return x;}
int mul(int a,int b,int m=MOD){lli x=a*1ll*b;x%=m;while(x<0)x+=m;return (int)x;}
int ldtoint(ld x){return (int)(x+0.5);}lli ldtolli(ld x){return (lli)(x+0.5);}
int powermod(lli _a,lli _b,int _m=MOD){lli _r=1;while(_b){if(_b%2==1)_r=mul(_r,_a,_m);_b>>=1;_a=mul(_a,_a,_m);}return _r;}

template<class T1,class T2>ostream&operator<<(ostream& os,const pair<T1,T2>&p){os<<"["<<p.first<<","<<p.second<<"]";return os;}
template<class T>ostream&operator<<(ostream& os,const vector<T>&v){os << "[";bool first=true;for (T it:v){if (!first)os<<", ";first = false;os<<it;}os<<"]";return os;}
template<class T>ostream&operator<<(ostream& os,set<T>&v){os<<"[";bool first=true;for (T it:v){if(!first)os<<", ";first=false;os<<it;}os<<"]";return os;}
template<class T1,class T2>ostream&operator<<(ostream& os,map<T1,T2>&v){os<<"[";bool first=true;for(pair<T1,T2> it:v){if(!first)os<<", ";first=false;os<<"("<<it.F<<","<<it.S<<")";}os<<"]";return os;}
template<class T>void parr(T a[],int s,int e){cout<<"[";for(int i=s;i<e;i++)cout<<a[i]<<", ";cout<<a[e]<<"]\n";}

bool yes(int N){
    vector<int> v;
    while(N){
        v.pb(N%10);
        N /= 10;
    }
    reverse(all(v));
    for(int i=1;i<v.size();i++){
        if(v[i] < v[i-1])
            return false;
    }
    return true;
}

int brute(int N){
    for(int i=N;i>=1;i--)
        if(yes(i))
            return i;
}

lli solve(lli N){
    if(N<=9)
        return N;
    if(yes(N))
        return N;
    vector<int> v;
    while(N){
        v.pb(N%10);
        N /= 10;
    }
    reverse(all(v));
    int last = 0;
    for(int i=1;i<v.size();i++){
        if(v[i] < v[i-1])
            break;
        if(v[i] != v[i-1])
            last = i;
    }
    v[last]--;
    for(int i=last + 1;i<v.size();i++)
        v[i] = 9;
    while(v[0] == 0)
        v.erase(v.begin());
    lli ret = 0;
    for(int i : v)
        ret = ret*10 + i;
    return ret;
}

int main()
{
if(LOCAL){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    debug = 1;
}
    srand (time(NULL));
    //ios::sync_with_stdio(0);cin.tie(0);

    lli T,N;
    cin>>T;
    int t = 1;
    while(T--){
        cin>>N;
        cout<<"Case #"<<t<<": ";
        cout<<solve(N)<<"\n";
        t++;
    }

    return 0;
}
