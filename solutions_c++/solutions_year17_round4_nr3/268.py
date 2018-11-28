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
template<size_t maxn>
struct Sat
{
    vector<int> edge[2*maxn],re[2*maxn];
    int n;
    void init(int _n)
    {
        n=_n;
        for(int i=0;i<2*n;i++) edge[i].clear(),re[i].clear();
    }
    void add(int p,bool x,int q,bool y)
    {
        //0base
        int u=p<<1|(!x),v=q<<1|(!y);//x<<1 = +x, x<<1|1 = ~x
        edge[u].push_back(v);edge[v^1].push_back(u^1);
        re[v].push_back(u);re[u^1].push_back(v^1);
    }
    bitset<2*maxn> vis;
    void dfs1(int u,vector<int> &rr)
    {
        vis[u]=1;
        for(auto v:edge[u]) if(!vis[v])
            dfs1(v,rr);
        rr.push_back(u);
    }
    int id[2*maxn];
    void dfs2(int u,int p)
    {
        vis[u]=1;id[u]=p;
        for(auto v:re[u]) if(!vis[v])
            dfs2(v,p);
    }
    bitset<2*maxn> ans;
    void zet(int u,bool x)
    {
        vis[u]=1;ans[u]=x;
        for(auto v:re[u]) if(!vis[v] && id[v]==id[u])
            zet(v,x);
    }
    bool ask(int p){return ans[p<<1];}
    void visreset()
    {
        if(n>=(int)maxn/16) vis.reset();
        else for(int i=0;i<2*n;i++) vis[i]=0;
    }
    bool sol()
    {
        vector<int> ret;visreset();
        for(int i=0;i<2*n;i++) if(!vis[i])
            dfs1(i,ret);
        reverse(ret.begin(),ret.end());visreset();
        for(auto u:ret) if(!vis[u])
            dfs2(u,u);
        for(int p=0;p<n;p++) if(id[p<<1]==id[p<<1|1])
            return false;

        visreset();//ans.reset();
        for(auto u:ret) if(id[u]==u && !vis[u])
            zet(u,0),zet(u^1,1);//health
        return true;
    }
};
const int maxn=55;
int r,c;
char mp[maxn][maxn];
void read()
{
    RI(r,c);
    REP1(i,1,r) assert(scanf("%s",mp[i]+1)==1);
}
bool ok[maxn][maxn][2];
bool islazer(char cc){return strchr("-|",cc);}
void build()
{
    REP1(i,0,r+1) REP1(j,0,c+1)
        if(i==0||j==0||i==r+1||j==c+1)
            mp[i][j]='#';

    REP1(i,1,r) REP1(j,1,c) ok[i][j][0]=ok[i][j][1]=true;
    REP1(i,1,r) REP1(j,1,c) if(strchr("-|",mp[i][j]))
    {
        {
            int l=j-1,rr=j+1;
            while(mp[i][l]=='.') l--;
            while(mp[i][rr]=='.') rr++;
            if(mp[i][l]!='#'||mp[i][rr]!='#')
                ok[i][j][0]=0;
        }
        {
            int l=i-1,rr=i+1;
            while(mp[l][j]=='.') l--;
            while(mp[rr][j]=='.') rr++;
            if(mp[l][j]!='#'||mp[rr][j]!='#')
                ok[i][j][1]=0;
        }
    }
}
Sat<maxn*maxn> sat;
void sol()
{
    sat.init(r*c);
    auto id=[&](int i,int j){return (i-1)*c+(j-1);};
    REP1(i,1,r) REP1(j,1,c) if(strchr("-|",mp[i][j]))
    {
        if(!ok[i][j][0]&&!ok[i][j][1]){PL("IMPOSSIBLE");return;}
        if(!ok[i][j][0]) sat.add(id(i,j),0,id(i,j),1);
        if(!ok[i][j][1]) sat.add(id(i,j),1,id(i,j),0);
    }
    REP1(i,1,r) REP1(j,1,c) if(mp[i][j]=='.')
    {
        int jj;//---
        {
            int l=j-1,rr=j+1;
            while(mp[i][l]=='.') l--;
            while(mp[i][rr]=='.') rr++;
            if(mp[i][l]==mp[i][rr]) jj=0;
            else if(islazer(mp[i][l])) jj=l;
            else jj=rr;
        }
        int ii;
        {
            int l=i-1,rr=i+1;
            while(mp[l][j]=='.') l--;
            while(mp[rr][j]=='.') rr++;
            if(mp[l][j]==mp[rr][j]) ii=0;
            else if(islazer(mp[l][j])) ii=l;
            else ii=rr;
        }
        if(jj==0 && ii==0){PL("IMPOSSIBLE");return;}
        else if(jj==0) sat.add(id(ii,j),0,id(ii,j),1);
        else if(ii==0) sat.add(id(i,jj),1,id(i,jj),0);
        else sat.add(id(ii,j),0,id(i,jj),0);
    }
    if(!sat.sol()) PL("IMPOSSIBLE");
    else
    {
        PL("POSSIBLE");
        REP1(i,1,r) REP1(j,1,c)
        {
            if(islazer(mp[i][j])) putchar("-|"[sat.ask(id(i,j))]);
            else putchar(mp[i][j]);
            if(j==c) PL();
        }
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




