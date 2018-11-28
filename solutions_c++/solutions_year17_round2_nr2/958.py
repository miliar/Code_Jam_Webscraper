#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
int n,r,o,y,g,b,v;    
string rep(string s,int k){
  string ans="";
  while(k--)ans+=s;
  return ans;
}
string solve(){
  if(r==g && r+g==n)return rep("RG",r);
  if(b==o && b+o==n)return rep("BO",b);
  if(y==v && y+v==n)return rep("YV",y);

  if(g>0 && r<g+1)return "IMPOSSIBLE";
  if(o>0 && b<o+1)return "IMPOSSIBLE";
  if(v>0 && y<v+1)return "IMPOSSIBLE";
  vector<string>red(r-g,"R");
  if(g>0)red[0]=rep("RG",g)+"R";
  vector<string>blu(b-o,"B");
  if(o>0)blu[0]=rep("BO",o)+"B";
  vector<string>yel(y-v,"Y");
  if(v>0)yel[0]=rep("YV",v)+"Y";

  if(yel.size()<red.size())swap(yel,red);
  if(yel.size()<blu.size())swap(yel,blu);
  if(blu.size()<red.size())swap(red,blu);
  
//  assert(int(red.size()+blu.size()+yel.size())==n);
  vector<string>yb;
  while(!blu.empty()){
    yb.push_back(blu.back());
    yb.push_back(yel.back());
    blu.pop_back();
    yel.pop_back();
  }
  for(string s:yel)yb.push_back(s);
  string ans="";
  while(!red.empty()){
    ans+=yb.back();
    yb.pop_back();
    ans+=red.back();
    red.pop_back();
  }
  while(!yb.empty()){
    ans+=yb.back();
    yb.pop_back();
  }
  assert((int)ans.size()==n);
  for(int i=0;i<n;i++)if(ans[i]==ans[(i+1)%n])return "IMPOSSIBLE";  
  return ans;
}
int main(){
  freopen("bl.in","r",stdin);
  freopen("bl.out","w",stdout);
  int t;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    cerr<<"tt="<<tt<<endl;
    scanf("%d %d %d %d %d %d %d",&n,&r,&o,&y,&g,&b,&v);
    string ans=solve();
    cout<<"Case #"<<tt<<": "<<ans<<endl;
  }
  return 0;
}
