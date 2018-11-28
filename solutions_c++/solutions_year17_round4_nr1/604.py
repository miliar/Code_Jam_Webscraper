//{{{
#include <bits/stdc++.h>
using namespace std;
//types
typedef long long ll;
typedef pair<int,int> pii;
//input
bool SR(int &_x){return scanf("%d",&_x)==1;}bool SR(ll &_x){return scanf("%lld",&_x)==1;}
bool SR(double &_x){return scanf("%lf",&_x)==1;}bool SR(char *_s){return scanf("%s",_s)==1;}
bool RI(){return true;}
template<typename I,typename... T>bool RI(I &_x,T&... _tail){return SR(_x) && RI(_tail...);}
//output
void SP(const int _x){printf("%d",_x);}void SP(const ll _x){printf("%lld",_x);}
void SP(const double _x){printf("%.16lf",_x);}void SP(const char *s){printf("%s",s);}
void PL(){puts("");}
template<typename I,typename... T>void PL(const I _x,const T... _tail)
{SP(_x);if(sizeof...(_tail)) putchar(' ');PL(_tail...);}
//macro
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define REP(i,n) for(int i=0;i<int(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=int(b);i++)
#define pb push_back
#define mkp make_pair
#define F first
#define S second
//debug
#ifdef darry140
template<typename A,typename B>
ostream& operator <<(ostream&_s, const pair<A,B> &_p){return _s<<"("<<_p.F<<","<<_p.S<<")";}
template<typename It>
ostream& _OUTC(ostream &_s,It _b,It _e)//container
{
    _s<<"{";
    for(auto _it=_b;_it!=_e;_it++) _s<<(_it==_b?"":" ")<<*_it;
    _s<<"}";
    return _s;
}
template<typename A,typename B>
ostream& operator <<(ostream&_s, const map<A,B> &_c){return _OUTC(_s,ALL(_c));}
template<typename T>
ostream& operator <<(ostream&_s, const set<T> &_c){return _OUTC(_s,ALL(_c));}
template<typename T>
ostream& operator <<(ostream&_s, const vector<T> &_c){return _OUTC(_s,ALL(_c));}
template<typename I>
void _DOING(const char *_s,I&& _x){cerr<<_s<<"="<<_x<<endl;}//without ','
template<typename I,typename... T>
void _DOING(const char *_s,I&& _x,T&&... _tail)//with ','
{
    int _c=0;
    static const char _bra[]="({[";
    static const char _ket[]=")}]";
    while(*_s!=',' || _c!=0)//eg. mkp(a,b)
    {
        if(strchr(_bra,*_s)) _c++;
        if(strchr(_ket,*_s)) _c--;
        cerr<<*_s++;
    }
    cerr<<"="<<_x<<", ";
    _DOING(_s+1,_tail...);
}
#define debug(...) do{\
    fprintf(stderr,"%s:%d - ",__PRETTY_FUNCTION__,__LINE__);\
    _DOING(#__VA_ARGS__,__VA_ARGS__);\
}while(0)
#else
#define debug(...)
#endif
//}}}
const int maxn=1e2+2;
int n,p;
int g[maxn];
void read()
{
    RI(n,p);
    REP1(i,1,n) RI(g[i]);
}
int c[maxn];
void build()
{
    REP(i,p) c[i]=0;
    REP1(i,1,n) c[g[i]%p]++;
}
map<vector<int>,int> mp;
int f(vector<int> v)//[cnts]
{
    if(mp.count(v)) return mp[v];
    if(v==vector<int>(p,0)) return mp[v]=0;

    int rem=0;
    REP(i,p) rem+=i*v[i];
    rem%=p;

    int ans=0;
    REP(i,p) if(v[i]>0)
    {
        v[i]--;
        ans=max(ans,f(v)+(i==rem));
        v[i]++;
    }

    return mp[v]=ans;
}
void sol()
{
    mp.clear();
    int sh=c[0];c[0]=0;
    PL(sh+f(vector<int>(c,c+p)));
}
int main(int argc,char* argv[])
{
    int t;RI(t);
    vector<int> casid(t+1);iota(ALL(casid),0);
#if 1
    int casl=-1e9,casr=1e9;
    if(argc>1)
    {
        mt19937 _g;
        REP(_,10) REP1(i,1,t) swap(casid[i],casid[_g()%i+1]);
        int cc;sscanf(argv[1],"%d",&cc);
        casl=cc*t/8+1,casr=(cc+1)*t/8;
        debug(argc,cc,casl,casr); 
    }
#endif
    REP1(i,1,t)
    {
        if(!(casl<=casid[i] && casid[i]<=casr)){read();continue;}

        read();
        build();
        printf("Case #%d: ",i);
        sol();
    }
    return 0;
}




































/*End Of File*/




