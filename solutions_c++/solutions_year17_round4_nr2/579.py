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
template<typename TF,typename TC,bool maxcost,size_t maxn>
struct Flow//[0,n-1], maxn = max internal node count
{
    struct Edge
    {
        int u,v;TF f;TC c;
        Edge(int _u,int _v,TF _f,TC _c):
            u(_u),v(_v),f(_f),c(_c){}
    };
    int n;
    vector<Edge> edge;
    vector<int> id[maxn];
    void init(int _n){n=_n;edge.clear();REP(i,n) id[i].clear();}
    void add(int u,int v,TF f,TC c)
    {
        if(maxcost) c*=-1;
        id[u].pb(SZ(edge));edge.pb(Edge(u,v,f,c));
        id[v].pb(SZ(edge));edge.pb(Edge(v,u,0,-c));
    }
    pair<bool,TC> spfa()
    {
        static TC dis[maxn];
        static int par[maxn];
        bitset<maxn> isq;
        struct Q
        {
            vector<int> dat;
            int h;
            Q():dat(),h(0){}
            void push(int x){dat.pb(x);}
            void pop(){h++;}
            int front() const{return dat[h];}
            int size() const{return SZ(dat)-h;}
        } q;

        memset(dis,0x3f,sizeof(TC)*n);
        memset(par,-1,sizeof(int)*n);
        dis[0]=0;isq[0]=1;q.push(0);

        while(SZ(q))
        {
            int u=q.front();q.pop();isq[u]=0;
            for(int i:id[u]) if(edge[i].f>0)
            {
                const auto &e=edge[i];
                if(dis[e.v]>dis[u]+e.c)
                {
                    dis[e.v]=dis[u]+e.c;
                    par[e.v]=i;
                    if(!isq[e.v])
                        isq[e.v]=1,q.push(e.v);
                }
            }
        }

        if(par[n-1]==-1) return mkp(false,0);
        for(int u=n-1;u;u=edge[par[u]].u)
            edge[par[u]].f--,edge[par[u]^1].f++;
        if(maxcost) dis[n-1]*=-1;
        return mkp(true,dis[n-1]);
    }
    pair<TF,TC> calc()
    {
        TF cnt=0;
        TC ans=0;
        while(1)
        {
            pair<bool,TC> sub=spfa();
            if(!sub.F) break;
            cnt++;ans+=sub.S;
        }
        return mkp(cnt,ans);
    }
};
const int maxn=1e3+3;
int n,cc,m;
int p[maxn],b[maxn];
void read()
{
    RI(n,cc,m);
    REP1(i,1,m) RI(p[i],b[i]);
}
void build()
{
    vector<int> v(b+1,b+m+1);
    sort(ALL(v));v.erase(unique(ALL(v)),v.end());
    REP1(i,1,m) b[i]=lower_bound(ALL(v),b[i])-v.begin()+1;
    cc=SZ(v);
}
void sol1(){PL(m,0);}
void sol2()
{
    static Flow<int,int,0,1+maxn+1> flow;
    flow.init(1+m+1);
    REP1(i,1,m)
    {
        if(b[i]==1) flow.add(0,i,1,0);
        else flow.add(i,flow.n-1,1,0);
    }
    REP1(i,1,m) REP1(j,1,m) if(b[i]==1 && b[j]==2)
    {
        if(p[i]==p[j])
        {
            if(p[i]!=1) flow.add(i,j,1,1);
        }
        else
        {
            flow.add(i,j,1,0);
        }
    }
    auto ans=flow.calc();
    PL(m-ans.F,ans.S);
}
void sol()
{
    if(cc==1) sol1();
    else if(cc==2) sol2();
    else
    {
        assert(0);
    }
}
int main(int argc,char* argv[])
{
    int t;RI(t);
    vector<int> casid(t+1);iota(ALL(casid),0);
#if 1
    int casl=-1e9,casr=1e9;
    if(argc>1)
    {
        mt19937 g;
        REP(_,10) REP1(i,1,t) swap(casid[i],casid[g()%i+1]);
        int _cc;sscanf(argv[1],"%d",&_cc);
        casl=_cc*t/8+1,casr=(_cc+1)*t/8;
        debug(argc,_cc,casl,casr); 
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
