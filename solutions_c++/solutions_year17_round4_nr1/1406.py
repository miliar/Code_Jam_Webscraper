#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const int MAX=101;

int dp[MAX][MAX][MAX][4];
int n,p;

int solve(int m1, int m2, int m3, int left) {
    if(m1+m2+m3==0) return 0;
    int &ret=dp[m1][m2][m3][left];
    if(ret!=-1) return ret;
    ret=0;
    if(m1>0) {
        int tm1=left;
        tm1-=1;
        if(tm1<0) tm1+=p;
        ret=max(ret,(left==0)+solve(m1-1,m2,m3,tm1));
    }
    if(m2>0&&p>2) {
        int tm2=left;
        tm2-=2;
        if(tm2<0) tm2+=p;
        ret=max(ret,(left==0)+solve(m1,m2-1,m3,tm2));
    }
    if(m3>0&&p>3) {
        int tm3=left;
        tm3-=3;
        if(tm3<0) tm3+=p;
        ret=max(ret,(left==0)+solve(m1,m2,m3-1,tm3));
    }
    return ret;
}

void solve(int tc) {
    memset(dp,-1,sizeof(dp));
    vector<int> vals(4,0);
    
    cin>>n>>p;
    for(int i=0;i<n;i++) {
        int a;
        cin>>a;
        vals[a%p]++;
    }
    int ret=vals[0]+solve(vals[1],vals[2],vals[3],0);
    cout<<"Case #"<<tc<<": "<<ret<<endl;
}

int main() {
    int cases;
    cin>>cases;
    for(int tc=1;tc<=cases;tc++) solve(tc);
}
