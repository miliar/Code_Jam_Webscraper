#include <bits/stdc++.h>
using namespace std;

const int VSIZE=30000,ESIZE=30000,INF=1000000;

int MF(vector<vector<int> > &e,int s,int t,vector<vector<bool> > &f)
{
  int n=e.size();
  bool F[ESIZE]={0};
  int K=0;
  vector<vector<int> > fk(n),be(n),bfk(n);
  for(int i=0;i<n;i++){
    for(int j=0;j<e[i].size();j++){
      int k=e[i][j];
      fk[i].push_back(K);
      be[k].push_back(i);
      bfk[k].push_back(K);
      K++;
    }
  }
  int fl=0ll;
  while(1){
    int dis[VSIZE]={0};
    queue<int> Q;
    Q.push(s);
    dis[s]=1;
    while(!Q.empty()){
      int i=Q.front();
      Q.pop();
      for(int j=0;j<e[i].size();j++){
	if(F[fk[i][j]]){
	  continue;
	}
	int k=e[i][j];
	if(!dis[k]){
	  Q.push(k);
	  dis[k]=dis[i]+1;
	}
      }
      for(int j=0;j<be[i].size();j++){
	if(!F[bfk[i][j]]){
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
	  if(dis[k]!=dis[i]+1||F[fk[i][j]]){
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
	  if(dis[k]!=dis[i]+1||!F[bfk[i][j]]){
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
      fl+=1;
      for(int i=t;i!=s;i=B[i]){
	int J=FF[i];
	if(J>0){
	  int j=J-1;
	  F[j]=1;
	}
	else{
	  int j=-J-1;
	  F[j]=0;
	}
      }
    }
  }
  f=vector<vector<bool> >(n);
  for(int i=0;i<n;i++){
    f[i]=vector<bool>(e[i].size());
    for(int k=0;k<e[i].size();k++){
      f[i][k]=F[fk[i][k]];
    }
  }
  return fl;
}


int main()
{
  int T;
  scanf("%d",&T);
  for(int cs=1;cs<=T;cs++){
    int n,m;
    scanf("%d%d",&n,&m);
    bool B1[100]={0},B2[100]={0},B3[200]={0},B4[200]={0};
    int M1[100][100]={0},M2[100][100]={0};
    int S=0;
    for(int i=0;i<m;i++){
      char s[2];
      int a,b;
      scanf("%s%d%d",s,&a,&b);
      a--,b--;
      if(s[0]=='+'||s[0]=='o'){
	B3[a+b]=1;
	B4[a-b+n-1]=1;
	S++;
	M2[a][b]=1;
      }
      if(s[0]=='x'||s[0]=='o'){
	B1[a]=1;
	B2[b]=1;
	S++;
	M1[a][b]=1;
      }
    }
    vector<vector<int> > e(2*n+2*(2*n-1)+2);
    int N3=n,N4=N3+n,N5=N4+2*n-1,N6=N5+2*n-1;
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	e[i].push_back(N3+j);
	e[N4+i+j].push_back(N5+i+(n-1-j));
      }
    }
    int s=N6,t=N6+1;
    for(int i=0;i<n;i++){
      if(!B1[i]){
	e[s].push_back(i);
      }
      if(!B2[i]){
	e[N3+i].push_back(t);
      }
    }
    for(int i=0;i<2*n-1;i++){
      if(!B3[i]){
	e[s].push_back(N4+i);
      }
      if(!B4[i]){
	e[N5+i].push_back(t);
      }
    }
    vector<vector<bool> > f;
    S+=MF(e,s,t,f);
    for(int i=0;i<n;i++){
      for(int k=0;k<e[i].size();k++){
	int j=e[i][k]-N3;
	if(f[i][k]){
	  M1[i][j]=2;
	}
      }
    }
    for(int i=0;i<2*n-1;i++){
      for(int k=0;k<e[N4+i].size();k++){
	int j=e[N4+i][k]-N5;
	if(f[N4+i][k]){
	  M2[(i+j-(n-1))/2][(i-j+(n-1))/2]=2;
	}
      }
    }
    int M=0;
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	if(M1[i][j]==2||M2[i][j]==2){
	  M++;
	}
      }
    }
    printf("Case #%d: %d %d\n",cs,S,M);
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	if(M1[i][j]==2||M2[i][j]==2){
	  printf("%c %d %d\n",M1[i][j]?M2[i][j]?'o':'x':'+',i+1,j+1);
	}
      }
    }
  }
  return 0;
}
