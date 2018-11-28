#include<bits/stdc++.h>
using namespace std;
int stall[10000000];
int main(){
freopen("input.in","r",stdin);
freopen("output.out","w",stdout);
  int q;
  cin >>q;
  for(int x=1;x<=q;x++){
   memset(stall,0,sizeof(stall));
   int n,k,temp,ls,rs;
  cin >> n >> k;
  int p1=0,p2=(n+1);
  stall[p1]=1;
  stall[p2]=1;
  pair<int,int>maxi;
  for(int i=1;i <=k;i++)
  {
    int x1=0,x2=n+1;
    maxi=make_pair(x1,x1);
    for(int j=1;j<=n+1;j++){
        if(stall[j]==1){
            if((j-x1)>((maxi.second - maxi.first)))
                maxi = make_pair(x1,j);
            x1=j;
        }
    }
    temp= maxi.first + (( ((maxi.second - maxi.first -1)%2) ==0 )?((maxi.second - maxi.first -1)/2) : (((maxi.second - maxi.first -1)/2 )+ 1));
    stall[temp] = 1;
    ls = temp - maxi.first - 1;
    rs = maxi.second - temp - 1;
   }

  cout<<"Case #"<<x<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
  }
}
