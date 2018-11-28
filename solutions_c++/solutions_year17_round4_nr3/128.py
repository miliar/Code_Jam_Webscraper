#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;

#define MAXN 8192

namespace SAT {
bool truth[MAXN]; // truth[cmp[i]]=value of variable i (2SAT)
vector<int> g[MAXN];
int nvar;int neg(int x){return MAXN-1-x;} // (2SAT)
int n,lw[MAXN],idx[MAXN],qidx,cmp[MAXN],qcmp;
stack<int> st;
void tjn(int u){
	lw[u]=idx[u]=++qidx;
	st.push(u);cmp[u]=-2;
	for(int v:g[u]){
		if(!idx[v]||cmp[v]==-2){
			if(!idx[v]) tjn(v);
			lw[u]=min(lw[u],lw[v]);
		}
	}
	if(lw[u]==idx[u]){
		int x;
		do{x=st.top();st.pop();cmp[x]=qcmp;}while(x!=u);
		truth[qcmp]=(cmp[neg(u)]<0); // (2SAT)
		qcmp++;
	}
}
void scc(){
	memset(idx,0,sizeof(idx));qidx=0;
	memset(cmp,-1,sizeof(cmp));qcmp=0;
	fore(i,0,n)if(!idx[i])tjn(i);
}
// Only for 2SAT:
void addor(int a, int b){
	//printf("%d %d (%d,%d) (%d,%d)\n",a,b,neg(a),b,neg(b),a);
	g[neg(a)].pb(b);g[neg(b)].pb(a);
}
bool satisf(int _nvar){
	nvar=_nvar;n=MAXN;scc();
	fore(i,0,nvar)if(cmp[i]==cmp[neg(i)])return false;
	//fore(i,0,nvar)printf(" %d %d\n",(int)truth[i],(int)truth[neg(i)]);
	return true;
}
void clear(){
	fore(i,0,MAXN)g[i].clear();
}
};


int di[]={1,0,-1,0};
int dj[]={0,1,0,-1};
int b0[]={3,2,1,0}; // '/'
int b1[]={1,0,3,2}; // '\'

int si[4096],sj[4096];
int ns;

char b[64][64];
int n,m;
int qv[64][64],qh[64][64];

bool val(int i, int j){
	return i>=0&&i<n&&j>=0&&j<m&&b[i][j]!='#';
}

void go(int i, int j, int d, set<pair<int,int> >& w){
	while(1){
		int ii=i+di[d];
		int jj=j+dj[d];
		if(!val(ii,jj))break;
		i=ii;j=jj;
		w.insert(mp(i,j));
		if(b[i][j]=='-'||b[i][j]=='|')break;
		else if(b[i][j]=='/')d=b0[d];
		else if(b[i][j]=='\\')d=b1[d];
	}
}


int main(){
	int tn;

	scanf("%d",&tn);
	fore(tc,1,tn+1){
		printf("Case #%d: ",tc);
		scanf("%d%d",&n,&m);
		fore(i,0,n)scanf("%s",b[i]);
		memset(qv,-1,sizeof(qv));
		memset(qh,-1,sizeof(qh));
		bool can=true;
		SAT::clear();
		fore(i,0,n)fore(j,0,m)if(b[i][j]=='-'||b[i][j]=='|'){
			qv[i][j]=qh[i][j]=ns;
			si[ns]=i;sj[ns++]=j;
			set<pair<int,int> > w;
			go(i,j,0,w);
			go(i,j,2,w);
			bool v0=true;
			for(auto p:w){
				v0=v0&&(b[p.fst][p.snd]!='-'&&b[p.fst][p.snd]!='|');
			}
			if(v0){
				for(auto p:w)if(b[p.fst][p.snd]=='.')qv[p.fst][p.snd]=ns-1;
			}
			w.clear();
			go(i,j,1,w);
			go(i,j,3,w);
			bool v1=true;
			for(auto p:w){
				v1=v1&&(b[p.fst][p.snd]!='-'&&b[p.fst][p.snd]!='|');
			}
			if(v1){
				for(auto p:w)if(b[p.fst][p.snd]=='.')qh[p.fst][p.snd]=ns-1;
			}
			else if(!v0){can=false;break;}
			if(v0&&!v1)SAT::addor(ns-1,ns-1);
			else if(!v0&&v1)SAT::addor(SAT::neg(ns-1),SAT::neg(ns-1));
		}
		if(!can){puts("IMPOSSIBLE");continue;}
		fore(i,0,n)fore(j,0,m)if(b[i][j]=='.'){
			if(qv[i][j]<0&&qh[i][j]<0){can=false;break;}
			if(qv[i][j]<0)SAT::addor(SAT::neg(qh[i][j]),SAT::neg(qh[i][j]));
			else if(qh[i][j]<0)SAT::addor(qv[i][j],qv[i][j]);
			else SAT::addor(qv[i][j],SAT::neg(qh[i][j]));
		}
		if(!can){puts("IMPOSSIBLE");continue;}
		if(!SAT::satisf(ns)){puts("IMPOSSIBLE");continue;}
		puts("POSSIBLE");
		fore(i,0,n){
			fore(j,0,m){
				if(b[i][j]=='-'||b[i][j]=='|'){
					if(SAT::truth[SAT::cmp[qh[i][j]]])putchar('|');
					else putchar('-');
				}
				else putchar(b[i][j]);
			}
			puts("");
		}
	}
	return 0;
}




