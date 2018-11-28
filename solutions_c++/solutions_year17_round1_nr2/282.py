#include<bits/stdc++.h>
using namespace std;
#define int long long
signed main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    int n,p;
    cin>>n>>p;
    int r[n],q[n][p];
    for(int i=0;i<n;i++) cin>>r[i];
    for(int i=0;i<n;i++)
      for(int j=0;j<p;j++)
	cin>>q[i][j];

    for(int i=0;i<n;i++) sort(q[i],q[i]+p);
    int ans=0;

    if(n==1){
      for(int i=0;i<p;i++){
	bool f=0;
	int k=(10*q[0][i])/(11*r[0])-1;
	while(9*r[0]*k<=10*q[0][i]){
	  f|=10*q[0][i]<=11*r[0]*k;
	  if(f) break;
	  k++;
	}
	ans+=f;
      }
      cout<<"Case #"<<t<<": "<<ans<<endl;
      continue;
    }
    
    int L[n][p],R[n][p];
    memset(L,-1,sizeof(L));
    memset(R,-1,sizeof(R));
    
    for(int i=0;i<n;i++){
      for(int j=0;j<p;j++){
	bool f=0;
	int k=max((10*q[i][j])/(11*r[i])-1,1LL);
	while(9*r[i]*k<=10*q[i][j]){
	  f|=10*q[i][j]<=11*r[i]*k;
	  if(f) break;
	  k++;
	}
	if(!f){
	  if(j) R[i][j]=R[i][j-1];
	  continue;
	}
	L[i][j]=k;
	k=(10*q[i][j])/(9*r[i])+10;
	f=0;
	while(10*q[i][j]<=11*r[i]*k){
	  f|=9*r[i]*k<=10*q[i][j];
	  if(f) break;
	  k--;
	}
	R[i][j]=k;
	//if(t==66) cout<<i<<"-"<<j<<":"<<L[i][j]<<"/"<<R[i][j]<<endl;
      }
    }

    bool used[n][p];
    memset(used,0,sizeof(used));
    for(int j=0;j<p;j++){
      if(L[0][j]<0) continue;
      bool visit[n][p];
      memset(visit,0,sizeof(visit));
      for(int x=L[0][j];x<=R[0][j];x++){
	bool f=1;
	for(int i=1;i<n;i++){
	  int y=lower_bound(R[i],R[i]+p,x)-R[i];
	  //if(t==66) cout<<i<<":"<<x<<" "<<y<<endl;
	  while(y<p&&used[i][y]) y++;
	  //if(t==66) cout<<i<<":"<<x<<" "<<y<<endl;
	  
	  if(y==p||x<L[i][y]||x>R[i][y]){
	    f=0;
	    break;
	  }
	  visit[i][y]=1;
	}
	if(f){
	  ans++;
	  for(int i=0;i<n;i++)
	    for(int k=0;k<p;k++)
	      used[i][k]|=visit[i][k];
	  break;
	}
      }
    }
    cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}
