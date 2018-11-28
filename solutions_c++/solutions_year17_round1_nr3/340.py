#include <bits/stdc++.h>
using namespace std;

int HHD,HD,AD,HK,AK,B,D,t;
bool f[101][101][101][101];
int DP[101][101][101][101];

int solve(int HD,int AD,int HK,int AK,int xx) {
    if (HK <= 0) return 0;
    if (HD <= 0) return 1000000000;
    if (AD >= HK) return 1;
    int res2=1000000000;
    int res=1000000000;
        if (AK >= HD && HHD-AK != HD) {
                    res=min(res,solve(HHD-AK,AD,HK,AK,xx));
                  }
    int x=(HK+AK-1)/AD;
    if (AK) x=min(x,(HD-1)/AK);
      if (x) res2=x-1+solve(HD-x*AK,AD,HK-x*AD,AK,3);
    if (xx==3) {
            return min(res,res2)+1;
    }

    if (B)
        res2=min(res2,solve(HD-AK,AD+B,HK,AK,2));
    if (xx == 2) return min(res,res2)+1;
    if (AK && D)
        res2=min(res2,solve(HD-max(0,AK-D),AD,HK,max(0,AK-D),0));

    return min(res,res2)+1;
}

int main() {
    freopen("C-small-attempt3.in","r",stdin);
    freopen("C-small-attempt3.out","w",stdout);
    cin>>t;
    for (int t1=1;t1<=t;t1++) {
        cin>>HD>>AD>>HK>>AK>>B>>D;
        HHD=HD;
        int ans=solve(HD,AD,HK,AK,0);
        cout<<"Case #"<<t1<<": ";
        if (ans >= 1000000000) cout<<"IMPOSSIBLE"<<endl; else
            cout<<ans<<endl;
    }
}
