#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
const int mx=333;
vector<int>g[mx];
int matchl[mx],matchr[mx];
bool vis[mx];

bool kuhn(int u){
  if(vis[u])return false;
  vis[u]=true;
  for(int v:g[u]){
    if(matchr[v]==-1 || kuhn(matchr[v])){
      matchl[u]=v;
      matchr[v]=u;
      return true;
    }
  }
  return false;
}
int matching(int nl){
  memset(matchl,-1,sizeof matchl);
  memset(matchr,-1,sizeof matchr);
  bool changed=true;
  while(changed){
    changed=false;
    memset(vis,false,sizeof vis);
    for(int i=0;i<nl;i++)
      if(matchl[i]==-1)
        changed|=kuhn(i);
  }
  int ans=0;
  for(int i=0;i<nl;i++)
    ans+=(matchl[i]!=-1);
  return ans;
}
string board[123];
string ans[123];
int n;
bool canRook(int r,int c){
  for(int i=0;i<n;i++)if(board[i][c]=='x' || board[i][c]=='o' || board[r][i]=='x' || board[r][i]=='o')return false;
  return true;
}
bool canBishop(int r,int c){
  for(int i=r,j=c;i<n && j<n;i++,j++)if(board[i][j]=='+' || board[i][j]=='o')return false;
  for(int i=r,j=c;i>=0 && j>=0;i--,j--)if(board[i][j]=='+' || board[i][j]=='o')return false;
  for(int i=r,j=c;i>=0 && j<n;i--,j++)if(board[i][j]=='+' || board[i][j]=='o')return false;
  for(int i=r,j=c;i<n && j>=0;i++,j--)if(board[i][j]=='+' || board[i][j]=='o')return false;
  return true;
}
int main(){
  freopen("DL.in","r",stdin);
  freopen("DL.out","w",stdout);
  int t,m;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++)
      board[i]=ans[i]=string(n,'.');
    for(int i=0;i<m;i++){
      char buf[3];
      int r,c;
      scanf("%s %d %d",buf,&r,&c);
      --r,--c;
      board[r][c]=ans[r][c]=buf[0];
    }
    for(int i=0;i<n;i++){
      g[i].clear();
      for(int j=0;j<n;j++)
        if(canRook(i,j))
          g[i].push_back(j);              
    }
    matching(n);
    for(int i=0;i<n;i++){
      int j=matchl[i];
      if(j!=-1){
        if(ans[i][j]=='+')ans[i][j]='o';
        else ans[i][j]='x';
      }
    }
    //    cout<<"roocks=>"<<endl;for(int i=0;i<n;i++)cout<<ans[i]<<endl;
    for(int i=0;i<n+n+10;i++)g[i].clear();
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++)
        if(canBishop(i,j))
          g[i+j].push_back(i-j+n-1);
    }
    matching(n+n-1);
    for(int d1=0;d1<n+n-1;d1++){
      int d2=matchl[d1];
      if(d2!=-1){
        d2-=(n-1);      
        int i=(d1+d2)/2;
        int j=d1-i;
        if(ans[i][j]=='x')ans[i][j]='o';
        else ans[i][j]='+';
      }
    }
    //    cout<<"bishops=>"<<endl;for(int i=0;i<n;i++)cout<<ans[i]<<endl;
    vector<tuple<char,int,int> >upd;
    int score=0;
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        if(ans[i][j]=='o')score+=2;
        else if(ans[i][j]=='+' || ans[i][j]=='x')score++;
        if(board[i][j]!=ans[i][j]){
          upd.push_back(make_tuple(ans[i][j],i+1,j+1));
        }
      }
    }
    printf("Case #%d: %d %d\n",tt,score,(int)upd.size());
    for(auto e:upd){
      char ch;
      int i,j;
      tie(ch,i,j)=e;
      printf("%c %d %d\n",ch,i,j);
    }
  }
  return 0;
}
