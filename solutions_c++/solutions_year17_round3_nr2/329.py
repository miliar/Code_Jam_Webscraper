#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

int dp[24*60+1][24*60+1][2][2];
bool ac0[25*60];
bool ac1[25*60];

int solve(int t, int t1, bool cur, bool started) {
    if(t==24*60-1) {
        if(t1!=12*60) return 1000000;
        return int(cur!=started);
    }
    int &ret=dp[t][t1][cur][started];
    if(ret!=-1) return ret;
    ret=1000000;

    if(!ac0[t+1]) ret=min(ret,solve(t+1,t1+1,0,started)+int(cur!=0));
    if(!ac1[t+1]) ret=min(ret,solve(t+1,t1,1,started)+int(cur!=1));
    return ret;
}

void solve(int tc) {
    memset(dp,-1,sizeof(dp));
    memset(ac0,0,sizeof(ac0));
    memset(ac1,0,sizeof(ac1));

    int ac, aj;
    int ci, di, ji, ki;
    cin>>ac>>aj;
    for(int i=0;i<ac;i++) {
        cin>>ci>>di;
        for(int j=ci;j<di;j++) ac0[j]=1;
    }
    for(int i=0;i<aj;i++) {
        cin>>ji>>ki;
        for(int j=ji;j<ki;j++) ac1[j]=1;
    }
    int ret=100000;
    if(!ac0[0]) ret=min(ret,solve(0,1,0,0));
    if(!ac1[0]) ret=min(ret,solve(0,0,1,1));
    cout<<"Case #"<<tc<<": "<<ret<<endl;
}

int main() {
    int cases;
    cin>>cases;
    for(int i=1;i<=cases;i++) solve(i);
}
