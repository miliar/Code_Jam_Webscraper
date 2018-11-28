#include <bits/stdc++.h>

using namespace std;
#define INF 10000007
int dp[102][202][102][102];
int Hd,Ad,Hk,Ak,B,D;
int solve(int hd,int ad, int hk, int ak) {
    // cout<<hd<<" "<<ad<<" "<<hk<<" "<<ak<<endl;
  if(hk<=0 ){
    return 0;
  }
  if (hd<=0) {
    return INF;
  }

  // if(ak==0 && ad!=0) {
  //   if(dp[hd][ad][hk][ak]==-1) {
  //     // cout<<hd<<" "<<ad<<" "<<hk<<" "<<ak<<endl;
  //     dp[hd][ad][hk][ak]= INF;
  //   dp[hd][ad][hk][ak] = ceil(hk/ad);
  //     // if(ad<hk){
  //       dp[hd][ad][hk][ak] = min(dp[hd][ad][hk][ak],solve(hd-ak,ad+B,hk,ak)+1);
  //     }
  //   }
  // } else {
// return ceil(hk/ad);
//   }
    if(dp[hd][ad][hk][ak]==-1) {
      // cout<<hd<<" "<<ad<<" "<<hk<<" "<<ak<<endl;
      dp[hd][ad][hk][ak]= INF;
    dp[hd][ad][hk][ak] = min(solve(hd-ak,ad,hk-ad,ak),
                min(solve(Hd-ak,ad,hk,ak),
                solve(hd-max((ak-D),0),ad,hk,max(ak-D,0))))+1;
      if(ad+B<201){
        dp[hd][ad][hk][ak] = min(dp[hd][ad][hk][ak],solve(hd-ak,ad+B,hk,ak)+1);
      }
    }
  // }

  return dp[hd][ad][hk][ak];
}

void reset() {
  for(int i=0;i<102;i++){
    for(int j=0;j<202;j++) {
      for(int k=0;k<102;k++) {
        for(int l=0;l<102;l++){
          dp[i][j][k][l]=-1;
        }
      }
    }
  }
}
int main(){

  freopen("inc-s-f.in","r",stdin);
  freopen("outc-small-out.in","w",stdout);

  reset();
  int t;cin>>t;
  for(int test=1;test<=t;test++){
    reset();
    cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
    int soln = solve(Hd,Ad,Hk,Ak);
    if(soln>=INF) {
      cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
    } else {
      cout<<"Case #"<<test<<": "<<soln<<endl;
    }
  }

}
