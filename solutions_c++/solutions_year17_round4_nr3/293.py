#include<bits/stdc++.h>
using namespace std;
#define int long long
int r,c;
string s[55];
bool in(int y,int x){
  return 0<=y&&y<r&&0<=x&&x<c;
}
int px[111],py[111],pd[111],pt[111];
int ax[4]={1,-1,0,0};
int ay[4]={0,0,1,-1};
int cnt=0;
typedef pair<int,int> P;
map<P,int> mp;
int visit[111][111];
bool check(){
  bool res=1;
  for(int i=0;i<r;i++)
    for(int j=0;j<c;j++)
      if(s[i][j]=='.') res&=visit[i][j];
  return res;
}
bool ans;
void dfs(int p){
  if(p==cnt){
    ans|=check();
    return;
  }
  //cout<<p<<" "<<cnt<<endl;
  if(pd[p]){
    if(pt[p]){
      for(int k=2;k<4;k++){
	int ti=py[p]+ay[k],tj=px[p]+ax[k];
	while(in(ti,tj)){
	  if(s[ti][tj]=='#') break;
	  visit[ti][tj]++;
	  ti=ti+ay[k];
	  tj=tj+ax[k];
	}
      }
    }else{
      for(int k=0;k<2;k++){
	int ti=py[p]+ay[k],tj=px[p]+ax[k];
	while(in(ti,tj)){
	  if(s[ti][tj]=='#') break;
	  visit[ti][tj]++;
	  ti=ti+ay[k];
	  tj=tj+ax[k];
	}
      }
    }
    dfs(p+1);
    if(pt[p]){
      for(int k=2;k<4;k++){
	int ti=py[p]+ay[k],tj=px[p]+ax[k];
	while(in(ti,tj)){
	  if(s[ti][tj]=='#') break;
	  visit[ti][tj]--;
	  ti=ti+ay[k];
	  tj=tj+ax[k];
	}
      }
    }else{
      for(int k=0;k<2;k++){
	int ti=py[p]+ay[k],tj=px[p]+ax[k];
	while(in(ti,tj)){
	  if(s[ti][tj]=='#') break;
	  visit[ti][tj]--;
	  ti=ti+ay[k];
	  tj=tj+ax[k];
	}
      }
    }
  }else{
    pt[p]=0;
    s[py[p]][px[p]]='-';
    for(int k=0;k<2;k++){
      int ti=py[p]+ay[k],tj=px[p]+ax[k];
      while(in(ti,tj)){
	if(s[ti][tj]=='#') break;
	visit[ti][tj]++;
	ti=ti+ay[k];
	tj=tj+ax[k];
      }
    }
    dfs(p+1);
    for(int k=0;k<2;k++){
      int ti=py[p]+ay[k],tj=px[p]+ax[k];
      while(in(ti,tj)){
	if(s[ti][tj]=='#') break;
	visit[ti][tj]--;
	ti=ti+ay[k];
	tj=tj+ax[k];
      }
    }
    if(ans) return;
    pt[p]=1;
    s[py[p]][px[p]]='|';
    for(int k=2;k<4;k++){
      int ti=py[p]+ay[k],tj=px[p]+ax[k];
      while(in(ti,tj)){
	if(s[ti][tj]=='#') break;
	visit[ti][tj]++;
	ti=ti+ay[k];
	tj=tj+ax[k];
      }
    }
    dfs(p+1);
    for(int k=2;k<4;k++){
      int ti=py[p]+ay[k],tj=px[p]+ax[k];
      while(in(ti,tj)){
	if(s[ti][tj]=='#') break;
	visit[ti][tj]--;
	ti=ti+ay[k];
	tj=tj+ax[k];
      }
    }
  }
}
signed main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    cin>>r>>c;
    for(int i=0;i<r;i++) cin>>s[i];
    bool flag=0;
    ans=0;
    cnt=0;
    mp.clear();
    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++){
	if(s[i][j]=='-'||s[i][j]=='|'){
	  py[cnt]=i;px[cnt]=j;pd[cnt]=0;pt[cnt]=-1;mp[P(i,j)]=cnt;
	  bool f[4]={};
	  for(int k=0;k<4;k++){
	    int ti=i+ay[k],tj=j+ax[k];
	    while(in(ti,tj)){
	      f[k]|=(s[ti][tj]=='-'||s[ti][tj]=='|');
	      if(s[ti][tj]=='#') break;
	      ti=ti+ay[k];
	      tj=tj+ax[k];
	    }
	  }
	  if((f[0]||f[1])&&(f[2]||f[3])){
	    flag=1;
	    goto END;
	  }
	  if(f[0]||f[1]){
	    pd[cnt]=1;
	    pt[cnt]=1;
	    s[i][j]='|';
	  }
	  if(f[2]||f[3]){
	    pd[cnt]=1;
	    pt[cnt]=0;
	    s[i][j]='-';
	  }
	  cnt++;
	}
      }
    }
    for(int i=0;i<r;i++){
      for(int j=0;j<c;j++){
	if(s[i][j]=='.'){
	  bool f[4]={};
	  int tmp=0,res=-1,ri=-1,rj=-1;
	  for(int k=0;k<4;k++){
	    int ti=i+ay[k],tj=j+ax[k];
	    while(in(ti,tj)){
	      if(s[ti][tj]=='-'||s[ti][tj]=='|'){
		f[k]=1;
		ri=ti,rj=tj;
	      }
	      if(s[ti][tj]=='#') break;
	      ti=ti+ay[k];
	      tj=tj+ax[k];
	    }
	    if(f[k]) tmp++,res=k;
	  }
	  if(f[0]&&f[1]&&f[2]&&f[3]){
	    flag=1;
	    goto END;
	  }
	  if(f[0]&&f[1]&&!f[2]&&!f[3]){
	    flag=1;
	    goto END;
	  }
	  if(!f[0]&&!f[1]&&f[2]&&f[3]){
	    flag=1;
	    goto END;
	  }
	  if(!f[0]&&!f[1]&&!f[2]&&!f[3]){
	    flag=1;
	    goto END;
	  }
	  if(tmp==1){
	    int k=mp[P(ri,rj)];
	    if(res<2){
	      if(pd[k]&&pt[k]==1){
		flag=1;
		goto END;
	      }
	      pd[k]=1;
	      pt[k]=0;
	      s[ri][rj]='-';
	    }else{
	      if(pd[k]&&pt[k]==0){
		flag=1;
		goto END;
	      }
	      pd[k]=1;
	      pt[k]=1;
	      s[ri][rj]='|';
	    }
	  }
	}
      }
    }
  END:
    if(flag){
      cout<<"IMPOSSIBLE"<<endl;
      continue;
    }
    memset(visit,0,sizeof(visit));
    dfs(0);
    if(!ans) cout<<"IMPOSSIBLE"<<endl;
    else{
      cout<<"POSSIBLE"<<endl;
      for(int i=0;i<r;i++) cout<<s[i]<<endl;
    }
  }
  return 0;
}
