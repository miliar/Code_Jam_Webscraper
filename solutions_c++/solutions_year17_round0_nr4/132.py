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
#define PER1(i,a,b) for(int i=(a);i>=int(b);i--)
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
template<typename T,size_t maxn>
struct Flow//[0,n-1]
{
    struct Edge
    {
        int u,v;T f;
        Edge(int _u,int _v,T _f):
            u(_u),v(_v),f(_f){}
    };
    int n;
    vector<Edge> edge;
    vector<int> id[maxn];
    vector<int>::iterator arc[maxn];
    void init(int _n){n=_n;edge.clear();REP(i,n) id[i].clear();}
    void add(int u,int v,T f)
    {
        id[u].pb(SZ(edge));edge.pb(Edge(u,v,f));
        id[v].pb(SZ(edge));edge.pb(Edge(v,u,0));
    }
    int dep[maxn];
    bool bfs()
    {
        memset(dep,0,sizeof(int)*n);
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
        q.push(0);dep[0]=1;
        while(SZ(q))
        {
            int u=q.front();q.pop();
            for(auto i:id[u]) if(edge[i].f>0 && !dep[edge[i].v])
            {
                dep[edge[i].v]=dep[u]+1;
                q.push(edge[i].v);
            }
        }
        return dep[n-1];
    }
    T dfs(int u,T w)
    {
        if(u==n-1) return w;
        T ans=0;
        for(auto &it=arc[u];it!=id[u].end();it++)
            if(edge[*it].f>0 && dep[edge[*it].v]==dep[u]+1)
        {
            int i=*it;
            T sub=dfs(edge[i].v,min(w-ans,edge[i].f));
            ans+=sub;
            edge[i].f-=sub;
            edge[i^1].f+=sub;
            if(ans==w) break;
        }
        return ans;
    }
    T calc()
    {
        T ans=0;
        while(bfs())
        {
            REP(i,n) arc[i]=id[i].begin();
            ans+=dfs(0,numeric_limits<T>::max());
        }
        return ans;
    }
};
const int maxn=1e2+2;
const char ms[]=".x+o";
inline int ims(const char &c){return strchr(ms,c)-ms;}
int n,m;
vector<int> type,x,y;
void read()
{
    RI(n,m);
    type.resize(m+1);
    x.resize(m+1);
    y.resize(m+1);
    REP1(i,1,m)
    {
        char c[10];RI(c,x[i],y[i]);
        type[i]=ims(c[0]);
    }
}
Flow<int,1+maxn+maxn+1> flowrc;
Flow<int,1+maxn*2+maxn*2+1> flowdi;
inline int p(const int &i){return x[i]+y[i]-1;}
inline int q(const int &i){return x[i]-y[i]+n;}
bool valid(int i,int j)
{
    int x2=(i+1)+(j-n);
    int y2=(i+1)-(j-n);
    return (x2%2==0 && y2%2==0 && 1<=x2 && x2<=2*n && 1<=y2 && y2<=2*n);
}
void build()
{
    bitset<maxn> hasr,hasc;
    bitset<maxn*2> hasrpc,hasrmc;
    REP1(i,1,m)
    {
        if(type[i]&1)
        {
            assert(!hasr[x[i]] && !hasc[y[i]]);
            hasr[x[i]]=1;hasc[y[i]]=1;
        }
        if(type[i]&2)
        {
            assert(!hasrpc[p(i)] && !hasrmc[q(i)]);
            hasrpc[p(i)]=1;hasrmc[q(i)]=1;
        }
    }

    flowrc.init(1+n+n+1);
    REP1(i,1,n) flowrc.add(0,i,!hasr[i]);
    REP1(i,1,n) flowrc.add(n+i,flowrc.n-1,!hasc[i]);
    REP1(i,1,n) REP1(j,1,n) flowrc.add(i,n+j,1);

    flowdi.init(1+2*n-1+2*n-1+1);
    REP1(i,1,2*n-1) flowdi.add(0,i,!hasrpc[i]);
    REP1(i,1,2*n-1) flowdi.add(2*n-1+i,flowdi.n-1,!hasrmc[i]);
    REP1(i,1,2*n-1) REP1(j,1,2*n-1) if(valid(i,j))
        flowdi.add(i,2*n-1+j,1);
}
void print(const map<pii,int> &mp)
{
    return;
    REP1(i,1,n) REP1(j,1,n)
    {
        auto it=mp.find(mkp(i,j));
        if(it==mp.end()) putchar('.');
        else putchar(ms[it->S]);
        if(j==n) PL();
    }
    PL();
}
void sol()
{
    int score=0;
    REP1(i,1,m) score+=__builtin_popcount(type[i]);
    score+=flowrc.calc()+flowdi.calc();
    map<pii,int> ori;
    REP1(i,1,m) ori[mkp(x[i],y[i])]=type[i];
    map<pii,int> mp=ori;

    {
        int id=n+n;
        REP1(i,1,n) REP1(j,1,n)
        {
            id++;
            if(flowrc.edge[2*id-1].f==1)
            {
                //debug(i,j);
                mp[mkp(i,j)]|=1;
            }
        }
    }
    {
        int id=2*n-1+2*n-1;
        REP1(i,1,2*n-1) REP1(j,1,2*n-1) if(valid(i,j))
        {
            id++;
            if(flowdi.edge[2*id-1].f==1)
            {
                int x2=(i+1)+(j-n);
                int y2=(i+1)-(j-n);
                //debug(x2/2,y2/2);
                mp[mkp(x2/2,y2/2)]|=2;
            }
        }
    }
    
    int dif=0;
    for(auto p:mp) if(ori[p.F]!=p.S)
        dif++;
    printf("%d %d\n",score,dif);
    for(auto p:mp) if(ori[p.F]!=p.S)
        printf("%c %d %d\n",ms[p.S],p.F.F,p.F.S);
    print(ori);
    print(mp);
}
int main()
{
    int t;RI(t);
    REP1(cas,1,t)
    {
        read();
        build();
        printf("Case #%d: ",cas);
        sol();
    }
    return 0;
}




































/*End Of File*/



