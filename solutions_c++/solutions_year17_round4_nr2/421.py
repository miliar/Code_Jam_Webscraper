#include <bits/stdc++.h>
using namespace std;

typedef int flow_type;
const int ESIZE=100000,VSIZE=100000;
const int INF=1000000;

pair<flow_type,flow_type> MCF(vector<vector<int> > &e,vector<vector<flow_type> > &cp,vector<vector<flow_type> > &ct,int s,int t)
{
  int n=e.size();
  flow_type F[ESIZE]={0},CP[ESIZE],CT[ESIZE];
  int K=0;
  vector<vector<int> > fk(n),be(n),bfk(n);
  for(int i=0;i<n;i++){
    for(int j=0;j<e[i].size();j++){
      int k=e[i][j];
      CP[K]=cp[i][j];
      CT[K]=ct[i][j];
      fk[i].push_back(K);
      be[k].push_back(i);
      bfk[k].push_back(K);
      K++;
    }
  }
  flow_type MF=0,MC=0,H[VSIZE]={0};
  while(1){
    flow_type D[VSIZE];
    for(int i=0;i<n;i++){
      D[i]=INF;
    }
    D[s]=0;
    int B[VSIZE],BK[VSIZE],BS[VSIZE];
    priority_queue<pair<flow_type,int> > Q;
    Q.push(make_pair(0ll,s));
    while(!Q.empty()){
      pair<flow_type,int> p=Q.top();
      Q.pop();
      long long d=-p.first;
      int i=p.second;
      if(D[i]<d){
	continue;
      }
      for(int j=0;j<e[i].size();j++){
	int k=e[i][j],K=fk[i][j];
	if(F[K]==CP[K]){
	  continue;
	}
	flow_type nd=d+CT[K]+H[i]-H[k];
	if(D[k]>nd){
	  D[k]=nd;
	  B[k]=i;
	  BK[k]=K;
	  BS[k]=1;
	  Q.push(make_pair(-nd,k));
	}
      }
      for(int j=0;j<be[i].size();j++){
	int k=be[i][j],K=bfk[i][j];
	if(F[K]==0){
	  continue;
	}
	flow_type nd=d-CT[K]+H[i]-H[k];
	if(D[k]>nd){
	  D[k]=nd;
	  B[k]=i;
	  BK[k]=K;
	  BS[k]=-1;
	  Q.push(make_pair(-nd,k));
	}
      }
    }
    if(D[t]==INF){
      break;
    }
    MF++;
    int l=t;
    while(l!=s){
      F[BK[l]]+=BS[l];
      l=B[l];
    }
    for(int i=0;i<n;i++){
      H[i]+=D[i];
    }
    MC+=H[t];
  }
  return make_pair(MF,MC);
}

flow_type MF(vector<vector<int> > &e,vector<vector<flow_type> > &c,int s,int t)
{
  int n=e.size();
  flow_type F[ESIZE]={0},C[ESIZE];
  int K=0;
  vector<vector<int> > fk(n),be(n),bfk(n);
  for(int i=0;i<n;i++){
    for(int j=0;j<e[i].size();j++){
      int k=e[i][j];
      C[K]=c[i][j];
      fk[i].push_back(K);
      be[k].push_back(i);
      bfk[k].push_back(K);
      K++;
    }
  }
  flow_type fl=0ll;
  while(1){
    int dis[VSIZE]={0};
    queue<int> Q;
    Q.push(s);
    dis[s]=1;
    while(!Q.empty()){
      int i=Q.front();
      Q.pop();
      for(int j=0;j<e[i].size();j++){
	if(F[fk[i][j]]==C[fk[i][j]]){
	  continue;
	}
	int k=e[i][j];
	if(!dis[k]){
	  Q.push(k);
	  dis[k]=dis[i]+1;
	}
      }
      for(int j=0;j<be[i].size();j++){
	if(F[bfk[i][j]]==0){
	  continue;
	}
	int k=be[i][j];
	if(!dis[k]){
	  Q.push(k);
	  dis[k]=dis[i]+1;
	}
      }
    }
    if(!dis[t]){
      break;
    }
    while(1){
      int B[VSIZE],FF[VSIZE];
      for(int i=0;i<n;i++){
	B[i]=-1;
      }
      stack<int> Q;
      Q.push(s);
      while(!Q.empty()){
	int i=Q.top();
	Q.pop();
	if(i==t){
	  break;
	}
	for(int j=0;j<e[i].size();j++){
	  int k=e[i][j];
	  if(dis[k]!=dis[i]+1||F[fk[i][j]]==C[fk[i][j]]){
	    continue;
	  }
	  if(B[k]==-1){
	    Q.push(k);
	    B[k]=i;
	    FF[k]=fk[i][j]+1;
	  }
	}
	for(int j=0;j<be[i].size();j++){
	  int k=be[i][j];
	  if(dis[k]!=dis[i]+1||F[bfk[i][j]]==0){
	    continue;
	  }
	  if(B[k]==-1){
	    Q.push(k);
	    B[k]=i;
	    FF[k]=-bfk[i][j]-1;
	  }
	}
      }
      if(B[t]==-1){
	break;
      }
      flow_type M=INF;
      for(int i=t;i!=s;i=B[i]){
	int J=FF[i];
	if(J>0){
	  int j=J-1;
	  M=min(M,C[j]-F[j]);
	}
	else{
	  int j=-J-1;
	  M=min(M,F[j]);
	}
      }
      fl+=M;
      for(int i=t;i!=s;i=B[i]){
	int J=FF[i];
	if(J>0){
	  int j=J-1;
	  F[j]+=M;
	}
	else{
	  int j=-J-1;
	  F[j]-=M;
	}
      }
    }
  }
  return fl;
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int cs=1;cs<=T;cs++){
    int n,c,m;
    scanf("%d%d%d",&n,&c,&m);
    int N=c+2*n+2,s=N-2,t=N-1;
    vector<vector<int> > e(N),cp(N),ct(N);
    for(int x=0;x<m;x++){
      int p,a;
      scanf("%d%d",&p,&a);
      p--,a--;
      e[s].push_back(a);
      cp[s].push_back(1);
      ct[s].push_back(0);
      e[a].push_back(c+p);
      cp[a].push_back(1);
      ct[a].push_back(0);
    }
    for(int i=0;i<n;i++){
      e[c+i].push_back(c+n+i);
      cp[c+i].push_back(INF);
      ct[c+i].push_back(1);
      e[c+n+i].push_back(c+i);
      cp[c+n+i].push_back(INF);
      ct[c+n+i].push_back(0);
      e[c+i].push_back(t);
      cp[c+i].push_back(INF);
      ct[c+i].push_back(0);
    }
    for(int i=0;i<n-1;i++){
      e[c+n+i+1].push_back(c+n+i);
      cp[c+n+i+1].push_back(INF);
      ct[c+n+i+1].push_back(0);
    }
    int l=0,r=m;
    for(int i=0;i<c;i++){
      l=max(l,(int)e[i].size());
    }
    l--;
    while(l+1<r){
      int d=(l+r)/2;
      for(int i=0;i<n;i++){
	cp[c+i][1]=d;
      }
      int f=MF(e,cp,s,t);
      if(f<m){
	l=d;
      }
      else{
	r=d;
      }
    }
    for(int i=0;i<n;i++){
      cp[c+i][1]=r;
    }
    pair<int,int> ans=MCF(e,cp,ct,s,t);
    printf("Case #%d: %d %d\n",cs,r,ans.second);
    fprintf(stderr,"Case #%d: %d %d\n",cs,r,ans.second);
  }
  return 0;
}
