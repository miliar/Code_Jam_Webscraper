#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
const int mx=5e6+10;
int f[mx][4];
int g[123][123][123][3];
vector<vector<int> >all;
int idx(vector<int>k){
  return lower_bound(all.begin(),all.end(),k)-all.begin();
}
int main(){
  freopen("al.in","r",stdin);
  freopen("al.out","w",stdout);
  
  for(int q0=0;q0<=100;q0++)
  for(int q1=0;q1<=100;q1++)if(q0+q1<=100)
  for(int q2=0;q2<=100;q2++)if(q0+q1+q2<=100)
  for(int q3=0;q3<=100;q3++)if(q0+q1+q2+q3<=100){
    all.push_back({q0,q1,q2,q3});
  }
  for(int q0=0;q0<=100;q0++)
  for(int q1=0;q1<=100;q1++)if(q0+q1<=100)
  for(int q2=0;q2<=100;q2++)if(q0+q1+q2<=100)
  for(int q3=0;q3<=100;q3++)if(q0+q1+q2+q3<=100){
    vector<int>q={q0,q1,q2,q3};
    int at=idx(q);
    for(int rem=0;rem<4;rem++){
      for(int it=0;it<4;it++)if(q[it]!=0){
        int nrem=(rem-it+4)%4;
        q[it]--;
        f[at][rem]=max(f[at][rem], f[idx(q)][nrem]+(rem==0));
        q[it]++;
      }
    }
  }
  
  cerr<<"okf"<<endl;
  for(int q0=0;q0<=100;q0++)
  for(int q1=0;q1<=100;q1++)if(q0+q1<=100)
  for(int q2=0;q2<=100;q2++)if(q0+q1+q2<=100){
    for(int rem=0;rem<3;rem++){
      if(q0>0)g[q0][q1][q2][rem]=max(g[q0][q1][q2][rem],g[q0-1][q1][q2][(rem-0+3)%3]+(rem==0));
      if(q1>0)g[q0][q1][q2][rem]=max(g[q0][q1][q2][rem],g[q0][q1-1][q2][(rem-1+3)%3]+(rem==0));
      if(q2>0)g[q0][q1][q2][rem]=max(g[q0][q1][q2][rem],g[q0][q1][q2-1][(rem-2+3)%3]+(rem==0));
    }
  }
  cerr<<"okg"<<endl;
  int t;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    int n,p;
    scanf("%d %d",&n,&p);
    vector<int>q(p,0);
    for(int i=0;i<n;i++){
      int x;
      scanf("%d",&x);
      q[x%p]++;
    }
    int ans=0;
    if(p==2)ans=q[0]+(q[1]+1)/2;
    else if(p==3){
      ans=g[q[0]][q[1]][q[2]][0];
    }
    else ans=f[idx(q)][0];
    printf("Case #%d: %d\n",tt,ans);
  }
  return 0;
}
