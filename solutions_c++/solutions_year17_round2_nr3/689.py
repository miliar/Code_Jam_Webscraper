#include <bits/stdc++.h>
using namespace std;

const long long INF=10000000000000000ll;

int main()
{
  int T;
  scanf("%d",&T);
  for(int cs=1;cs<=T;cs++){
    int n,q;
    scanf("%d%d",&n,&q);
    long long E[100],S[100];
    for(int i=0;i<n;i++){
      scanf("%lld%lld",E+i,S+i);
    }
    static long long D[100][100];
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	scanf("%lld",D[i]+j);
	if(D[i][j]==-1){
	  D[i][j]=INF;
	}
      }
    }
    for(int k=0;k<n;k++){
      for(int i=0;i<n;i++){
	for(int j=0;j<n;j++){
	  D[i][j]=min(D[i][j],D[i][k]+D[k][j]);
	}
      }
    }
    static double dis[100][100];
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	if(D[i][j]<=E[i]){
	  dis[i][j]=(double)D[i][j]/S[i];
	}
	else{
	  dis[i][j]=INF;
	}
      }
    }
    for(int k=0;k<n;k++){
      for(int i=0;i<n;i++){
	for(int j=0;j<n;j++){
	  dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);
	}
      }
    }
    printf("Case #%d:",cs);
    for(int t=0;t<q;t++){
      int u,v;
      scanf("%d%d",&u,&v);
      u--,v--;
      printf(" %.8lf",dis[u][v]);
    }
    putchar('\n');
  }
  return 0;
}
