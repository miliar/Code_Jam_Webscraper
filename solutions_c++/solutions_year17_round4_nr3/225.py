#include <bits/stdc++.h>
using namespace std;

#define fru(j,n) for(int j=0; j<(n); ++j)
#define tr(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
//#define tr(it,v) for(auto it=(v).begin(); it!=(v).end(); ++it)
#define x first
#define y second
#define pb push_back
#define ALL(G) (G).begin(),(G).end()

#if 0
#define DEB printf
#else
#define DEB(...)
#endif

typedef long long ll;
typedef long long LL;
typedef double D;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int inft = 1000000009;
const int mod = 1000000007;
const int MAXN = 1000006;
namespace SCC{
	const int MAXN = 1000006; //USTAW, potem init !!
	int tin[MAXN],ct,n;
	vi V [MAXN],Q;
	int scc[MAXN],SCC;//out: 0<=scc[u]<SCC  - numer scc w ktorej jest u

	void przetworz(vi &R){ //zrob cos z ta SCC
		tr(it,R) scc[*it]=SCC;
		//	printf("w scc o nr %d sa wierzcholki:\n",SCC);
		//	tr(it,R) printf("%d\n",*it);
		++SCC;
	}

	int dfs(int u){
		tin[u]=ct++;
		Q.pb(u);
		int m=tin[u];
		tr(it,V[u]) if(scc[*it]==-1)  {
			if(tin[*it]!=-1) m=min(m,tin[*it]);
			else m=min(m,dfs(*it));
		}
		if(m==tin[u])  {
			vi R;
			do{
				R.pb(Q.back());
				Q.pop_back();
			}while(R.back()!=u);
			przetworz(R);
		}
		return m;
	}
	void init(int _n) //to na poczatku
	{
		n=_n;
		fru(i,n) V[i].clear();
		fru(i,n) scc[i]=tin[i]=-1;
		SCC=0;
		ct=0;
	}
	void edge(int mod,int a,int b){//0<=a,b<n
		DEB("kr %d-->%d\n",a,b);
		V[a].push_back(b);
		if(mod==0)return;
		if(a%2)a--;else a++;
		if(b%2)b--;else b++;
		swap(a,b);
		DEB("kr %d-->%d\n",a,b);
		V[a].push_back(b);
	}
	void go(){
		fru(i,n) if(tin[i]==-1) dfs(i);
	}
	/*
2SAT:
gdy mamy graf implikacji to istnieje wartosciowanie zmiennych
wtw gdy dla kazdej zm. z, z i ~z sa w roznych scc
konstrukcja:
bierzemy ten literal o mniejszym numerze scc
	 */
}

char s[100][100];
const pair<pii,int> T=make_pair(pii(-1,-1),-1);
int n,m;
int dx[]={0,1,0,-1},dy[]={1,0,-1,0};

pair<pii,int> go(int i,int j,int h,bool fir=1){
//	printf("go %d %d %d %d\n",i,j,h,fir);
	if(i<0 || j<0 || i==n || j==m)return T;
	if(s[i][j]=='#')return T;
	if(!fir)if(s[i][j]=='-' || s[i][j]=='|')return make_pair(pii(i,j),h);
	if(s[i][j]=='\\'){
		if(h<2)h=1-h;else h=5-h;
	}
	if(s[i][j]=='/'){
		if(h!=3 && h!=0)h=3-h;else h=3-h;
	}

	return go(i+dx[h],j+dy[h],h,0);	
}
void solve() {
	scanf("%d%d",&n,&m);
	int NN=2*n*m+10;
	SCC::init(NN);
	fru(i,n)scanf("%s",s[i]);
	fru(i,n)fru(j,m)if(s[i][j]!='#' && s[i][j]!='/' && s[i][j]!='\\'){
		pair<pii,int> ret[2];
		ret[0]=ret[1]=T;
		fru(h,4){
			pair<pii,int> u=go(i,j,h);
			if(u==T)continue;
			if(ret[h%2]==T)ret[h%2]=u;
			else ret[h%2]=T;
		//	DEB("dla %d %d %d ---> %d %d %d\n",i,j,h,u.x.x,u.x.y,u.y);
		}
		//printf("mam %d %d\n",i,j);
		if(s[i][j]=='.'){
			if(ret[0]==T)SCC::edge(0,2*(i*m+j),2*(i*m+j)+1);
			else SCC::edge(1,2*(i*m+j),2*(ret[0].x.x*m+ret[0].x.y)+ret[0].y%2);
			if(ret[1]==T)SCC::edge(0,2*(i*m+j)+1,2*(i*m+j)+0);
			else SCC::edge(1,2*(i*m+j)+1,2*(ret[1].x.x*m+ret[1].x.y)+ret[1].y%2);
		}else if(s[i][j]=='-' || s[i][j]=='|'){
			if(ret[0]!=T)SCC::edge(0,2*(i*m+j),2*(i*m+j)+1);
			if(ret[1]!=T)SCC::edge(0,2*(i*m+j)+1,2*(i*m+j)+0);
		}
	}
	SCC::go();
	bool ok=1;
	fru(i,n)fru(j,m)if(s[i][j]!='#'){
		if(SCC::scc[2*(i*m+j)]==SCC::scc[2*(i*m+j)+1]){
	//		printf("zle dla %d %d\n",i,j);
			ok=0;
		}
		if(SCC::scc[2*(i*m+j)]<SCC::scc[2*(i*m+j)+1])DEB("%d %d na true\n",i,j);
		if(s[i][j]=='-' || s[i][j]=='|'){
			if(SCC::scc[2*(i*m+j)]<SCC::scc[2*(i*m+j)+1])s[i][j]='-';
			else s[i][j]='|';
		}
	}
	if(!ok)puts("IMPOSSIBLE");
	else{
		puts("POSSIBLE");
		fru(i,n)printf("%s\n",s[i]);
	}
}

int main() {
	int te = 1;
	scanf("%d",&te);
	fru(ti,te) {
		printf("Case #%d: ",ti+1);
		solve();
	}
	return 0;
}
