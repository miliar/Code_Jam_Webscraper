/*
Date: 2017/05/13 21:25:41 Saturday
*/
#include<bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define rep(i,a,n) for(int i=(a);i<=(n);++i)
#define dep(i,a,n) for(int i=(a);i>=(n);--i)
#define eps 1e-8
#define pi 3.1415926535897
#define sqr(x) ((x)*(x))
#define MAX(a,b) a=max(a,b)
#define MIN(a,b) a=min(a,b)
#define SZ(x) ((int)(x).size())
#define CPY(a,b) memcpy(a,b,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define POSIN(x,y) (1<=(x)&&(x)<=n&&1<=(y)&&(y)<=m)
#define all(x) (x).begin(),(x).end()
#define COUT(S,x) cout<<fixed<<setprecision(x)<<S<<endl
#define buli(x) (__builtin_popcountll(x))
#define bur0(x) (__builtin_ctzll(x))
#define bul2(x) (63-__builtin_clzll(x))
#define pw(x) ((ll(1))<<(x))
#define upmo(a,b) (((a)=((a)+(b))%mo)<0?(a)+=mo:(a))
#define mmo(a,b) (((a)=1ll*(a)*(b)%mo)<0?(a)+=mo:(a))
#define y0 y0z
#define y1 y1z
#define yn ynz
#define j0 j0z
#define j1 j1z
#define jn jnz
#define tm tmz
#ifdef LOCAL
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define debug(...) 
#endif
typedef long long ll;
typedef double lf;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<lf,lf> pff;
typedef complex<double> CD;
const int inf=0x3f3f3f3f;
const int mo=1000000007;
inline void gn(long long&x){
	int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');c=='-'?(sg=-1,x=0):(x=c-'0');
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';x*=sg;
}
inline void gn(int&x){long long t;gn(t);x=t;}
inline void gn(unsigned long long&x){long long t;gn(t);x=t;}
inline void gn(double&x){double t;scanf("%lf",&t);x=t;}
inline void gn(long double&x){double t;scanf("%lf",&t);x=t;}
template<class T1,class T2>inline void gn(T1&r,T2&s){gn(r),gn(s);}
template<class T1,class T2,class T3>inline void gn(T1&r,T2&s,T3&t){gn(r),gn(s),gn(t);}
template<class T1,class T2,class T3,class T4>inline void gn(T1&r,T2&s,T3&t,T4&u){gn(r),gn(s),gn(t),gn(u);}
inline void gs(char *s){scanf("%s",s);}
inline void gc(char &c){while((c=getchar())>126 || c<33);}
inline void pc(char c){putchar(c);}
const int DX[]={1,0,-1,0},DY[]={0,1,0,-1};
ll powmod(ll a,ll b) {ll res=1;a%=mo;for(;b;b>>=1){if(b&1)res=res*a%mo;a=a*a%mo;}return res;}
ll powmod(ll a,ll b,ll mo) {ll res=1;a%=mo;for(;b;b>>=1){if(b&1)res=res*a%mo;a=a*a%mo;}return res;}
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}
//*******************************************
namespace SAT{

#define clr(a) memset(a, 0, sizeof a)
#define pb push_back
#define uint unsigned int

char B[1<<26],*S=B;int F(){for(;*S<'-';S++);register int x=*S++-'0';for(;*S>='0';x=(x<<3)+(x<<1)+*S++-'0');return x;}
char U[1<<26],*O=U,Stk[20];
void pr(register int x, char c){if(!x)*O++='0';else{register int i=0;for(;x;Stk[++i]=x%10+'0',x/=10);for(;i;*O++=Stk[i--]);};*O++=c;}
const int MaxN = 600010, MaxM = 1000010;

class Graph {
public:
    int en[MaxN], next[MaxM], to[MaxM], tot, deg[MaxN];
    void add_edge(int x, int y) {
        next[++tot] = en[x];
        en[x] = tot;
        to[tot] = y;
        ++deg[y];
    }
    void init() {
        tot = 0;
        clr(en);
        clr(deg);
    }
}    G, T, anti;

int n;

int low[MaxN], dfn[MaxN], dfn_tot, stk[MaxN], stot, scc[MaxN], scc_tot;
bool mark[MaxN];
vector <int> vertex[MaxN];

void failed() {
    puts("No");
    exit(0);
}

bool instk[MaxN];
void dfs(int now) {
    dfn[now] = low[now] = ++dfn_tot;
    stk[++stot] = now;
    instk[now] = 1;
    for (int i = G.en[now]; i; i = G.next[i])
        if (!dfn[G.to[i]]) {
            dfs(G.to[i]);
            low[now] = min(low[now], low[G.to[i]]);
        } else     if (instk[G.to[i]])
            low[now] = min(low[now], dfn[G.to[i]]);

    if (dfn[now] == low[now]) {
        int x;
        ++scc_tot;
        do {
            x = stk[stot--];
            instk[x] = 0;
            scc[x] = scc_tot;
            vertex[scc_tot].pb(x);
        }    while (x != now);
    }
}


bool solvable() {
    clr(dfn);
    clr(low);
    clr(scc);
    dfn_tot = stot = scc_tot = 0;
    for (int i = 0; i < n * 2; ++i)
        if (!dfn[i]) dfs(i);
    for (int i = 0; i < n; ++i)
        if (scc[i * 2] == scc[i * 2 + 1]) return 0;
    return 1;
}

bool done[MaxN];

void settle(int x) {
    if (done[x]) return;
    done[x] = 1;
    for (int i = anti.en[x]; i; i = anti.next[i])
        settle(anti.to[i]);
}

void get_ans() {
    T.init();
    anti.init();
    clr(mark);
    clr(done);
    for (int i = 0; i < n * 2; ++i)
        for (int j = G.en[i]; j; j = G.next[j])
            if (scc[i] != scc[G.to[j]]) {
                T.add_edge(scc[i], scc[G.to[j]]);
                anti.add_edge(scc[G.to[j]], scc[i]);
            }
    static int q[MaxN];
    int l = 0, r = 0;
    for (int i = 1; i <= scc_tot; ++i)
        if (T.deg[i] == 0) q[++r] = i;
    while (l != r) {
        int u = q[++l];
        for (int i = T.en[u]; i; i = T.next[i])
            if (--T.deg[T.to[i]] == 0)
                q[++r] = T.to[i];
    }
    for (int i = r; i; --i) {
        int u = q[i];
        if (done[u]) continue;
        done[u] = 1;
        for (uint j = 0; j < vertex[u].size(); ++j) {
            int x = vertex[u][j];
            mark[x >> 1] = x & 1;
            settle(scc[x ^ 1]);
        }
    }
    for (int i = 0; i < n; ++i) pr(mark[i], i == n - 1 ? '\n' : ' ');
}

void add_clause(int x, int xval, int y, int yval) {
    G.add_edge(x * 2 + !xval, y * 2 + yval);
    G.add_edge(y * 2 + !yval, x * 2 + xval);
}

int main() {
    fread(B,1,1<<26,stdin);
    int m;
    n = F(), m = F();
    for (int i = 1; i <= m; ++i) {
        int x, xval, y, yval;
        x = F(), xval = F(), y = F(), yval = F();
        add_clause(x, xval, y, yval);
    }
    if (!solvable()) failed();
    else {
        puts("Yes");
        get_ans();
    }
    fwrite(U,1,O-U,stdout);
    return 0;
}

}

const int N=55,M=111111;
int l,m,n,t,C,n1,n2,nos;
char ch;
int a[N][N],num[N][N];
int ok[N][N][2][N][N],biu[N][N][2],vis[M],res[N][N];
vector<int>V[M];
void adde(int x,int y){
	//printf("%d %d\n",x,y);
	SAT::add_clause((x-1)%(n1+1),x>n1+1?1:0,(y-1)%(n1+1),y>n1+1?1:0);
}
void work(){
	SAT::n=n1+1;
	if(!SAT::solvable())nos=1;
	else{
		SAT::get_ans();
		//printf("ans:");rep(i,1,n1)printf("%d ",SAT::mark[i]);puts("");
	}
}
int main(){
#ifdef LOCAL
	freopen("C.in","r",stdin);freopen("C.out","w",stdout);
#endif
	scanf("%d",&C);rep(_,1,C){
		printf("Case #%d: ",_);
		n1=n2=0;
		SAT::G.init();
		SAT::T.init();
		SAT::anti.init();
		rep(i,0,100)SAT::vertex[i].clear();
		scanf("%d%d",&m,&n);
		rep(i,1,m*n)vis[i]=0;
		rep(i,1,m*n)V[i].clear();
		rep(i,1,m)rep(j,1,n){
			gc(ch);
			if(ch=='.')a[i][j]=0,num[i][j]=++n2;
			if(ch=='#')a[i][j]=1;
			if(ch=='/')a[i][j]=2;
			if(ch=='\\')a[i][j]=3;
			if(ch=='-'||ch=='|')a[i][j]=4,num[i][j]=++n1;
		}
		rep(i,1,m)rep(j,1,n)res[i][j]=a[i][j]==4?-1:a[i][j];
		nos=0;
		rep(x,1,m)rep(y,1,n)if(a[x][y]==4){
			rep(k,0,1){
				rep(i,1,m)rep(j,1,n)ok[x][y][k][i][j]=0;
				biu[x][y][k]=0;
			}
			rep(D,0,3){
				for(int i=x,j=y,d=D,cnt=0;i>=1&&j>=1&&i<=m&&j<=n;i+=DX[d],j+=DY[d],++cnt){
					ok[x][y][D&1][i][j]=1;
					if(cnt==0)continue;
					if(a[i][j]==1)break;
					if(a[i][j]==4){biu[x][y][D&1]=1;break;}
					if(a[i][j]==2)d=d^3;
					if(a[i][j]==3)d=d^1;
				}
			}
			//printf("%d %d %d %d\n",x,y,biu[x][y][0],biu[x][y][1]);
			//rep(i,1,m){rep(j,1,n)printf("%d",ok[x][y][0][i][j]+ok[x][y][1][i][j]*2);puts("");}
			if(biu[x][y][0]&&biu[x][y][1])nos=1;
			if(!biu[x][y][0]){
				rep(i,1,m)rep(j,1,n)if(ok[x][y][0][i][j]&&a[i][j]==0)V[num[i][j]].pb(num[x][y]);
			}
			if(!biu[x][y][1]){
				rep(i,1,m)rep(j,1,n)if(ok[x][y][1][i][j]&&a[i][j]==0)V[num[i][j]].pb(num[x][y]+n1+1);
			}
			if(biu[x][y][0]||biu[x][y][1]){
				int d=biu[x][y][1];
				//rep(i,1,m)rep(j,1,n)if(ok[x][y][d^1][i][j]&&a[i][j]==0)vis[num[i][j]]=1;
				adde(num[x][y]+(!d?n1+1:0),n1+1);
				adde(num[x][y]+(!d?n1+1:0),n1*2+2);
			}
		}
		rep(i,1,n2)if(!vis[i]){
			if(SZ(V[i])==0)nos=1;
			if(SZ(V[i])==1){
				adde(V[i][0],n1+1);
				adde(V[i][0],n1*2+2);
			}
			if(SZ(V[i])==2)adde(V[i][0],V[i][1]);
		}
		work();
		if(nos){puts("IMPOSSIBLE");continue;}
		puts("POSSIBLE");
		//rep(i,0,5)printf("%d ",SAT::mark[i]);puts("");
		rep(i,1,m)rep(j,1,n)if(res[i][j]==-1)res[i][j]=SAT::mark[num[i][j]-1]+10;
		rep(i,1,m){
			rep(j,1,n){
				if(res[i][j]==0)pc('.');
				if(res[i][j]==1)pc('#');
				if(res[i][j]==2)pc('/');
				if(res[i][j]==3)pc('\\');
				if(res[i][j]==10)pc('|');
				if(res[i][j]==11)pc('-');
			}
			puts("");
		}
	}
	return 0;
}
