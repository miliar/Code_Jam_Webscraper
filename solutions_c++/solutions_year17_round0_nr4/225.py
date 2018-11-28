#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;

vector<int> g[256];
int mt[256];
bool vis[256];
bool match(int x){
	if(vis[x])return false;
	vis[x]=true;
	for(int y:g[x])if(mt[y]<0||match(mt[y])){
		mt[y]=x;
		return true;
	}
	return false;
}
void mm(){
	memset(mt,-1,sizeof(mt));
	fore(i,0,256){
		memset(vis,false,sizeof(vis));
		match(i);
	}
}

bool b0[128][128],b1[128][128];
bool o0[128][128],o1[128][128];
bool hi[256],hj[256];
int n,m;

int main(){
	int tn;
	scanf("%d",&tn);
	fore(tc,1,tn+1){
		printf("Case #%d: ",tc);
		scanf("%d%d",&n,&m);
		memset(o0,false,sizeof(o0));
		memset(o1,false,sizeof(o1));
		while(m--){
			char s[4];int i,j;
			scanf("%s%d%d",s,&i,&j);i--;j--;
			if(s[0]=='+')o0[i][j]=1;
			if(s[0]=='x')o1[i][j]=1;
			if(s[0]=='o')o0[i][j]=o1[i][j]=1;
		}
		memcpy(b0,o0,sizeof(b0));
		memcpy(b1,o1,sizeof(b1));
		memset(hi,false,sizeof(hi));
		memset(hj,false,sizeof(hj));
		fore(i,0,n)fore(j,0,n)if(b1[i][j])hi[i]=true,hj[j]=true;
		fore(i,0,n)fore(j,0,n)if(!hi[i]&&!hj[j])b1[i][j]=true,hi[i]=true,hj[j]=true;
		memset(hi,false,sizeof(hi));
		memset(hj,false,sizeof(hj));
		fore(i,0,n)fore(j,0,n)if(b0[i][j])hi[i+j]=true,hj[i-j+n-1]=true;
		fore(i,0,n)fore(j,0,n)if(!hi[i+j]&&!hj[i-j+n-1])g[i+j].pb(i-j+n-1);
		mm();
		fore(d,0,256)if(mt[d]>=0){
			int s=mt[d];
			int i=(s+d-n+1)/2;
			int j=s-i;
			b0[i][j]=true;
		}
		vector<pair<char,pair<int,int> > > s;int r=0;
		fore(i,0,n)fore(j,0,n){
			r+=b0[i][j];r+=b1[i][j];
			if(b0[i][j]!=o0[i][j]||b1[i][j]!=o1[i][j]){
				assert(b0[i][j]>=o0[i][j]&&b1[i][j]>=o1[i][j]);
				char t;
				if(b0[i][j]&&b1[i][j])t='o';
				else if(b0[i][j])t='+';
				else t='x';
				s.pb(mp(t,mp(i,j)));
			}
		}
		printf("%d %d\n",r,(int)s.size());
		for(auto p:s)printf("%c %d %d\n",p.fst,p.snd.fst+1,p.snd.snd+1);
		fore(i,0,256)g[i].clear();
	}
	return 0;
}

