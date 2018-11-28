#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define  ll long long
#define pi pair<ll,ll>
#define f first
#define s second

int vis[1600][800][3][3];
int dp[1600][800][3][3];
int cur ;
bool P[2000][2];
int rec(int i,int j,int turn,int st) {
//    cout << i << " "<<turn << " " << j << "\n";
    if(i==2*720) {
        if(j==720) {
            if(turn==st) return 0;
            return 1;
        }
        return INT_MAX/2;
    }
    if(vis[i][j][turn][st]==cur) return dp[i][j][cur][st];
    vis[i][j][turn][st] = cur;

    int &ret = dp[i][j][cur][st];
    ret = INT_MAX/2;
    if(i==0) {
        if(!P[0][0]) {
            ret = min(ret,rec(i+1,j+1,0,0));
        }
        if(!P[0][1]) {
            ret = min(ret,rec(i+1,j,1,1));
        }
        return ret;
    }


    int A[2];
    A[0] = j;
    A[1] = i-j;
    if(!P[i][0] and A[0]<720) {
        A[0]++;
        ret = min(ret,rec(i+1,A[0],0,st)+(turn!=0));
        A[0]--;
    }
    if(!P[i][1] and A[1]<720) {
        A[1]++;
        ret = min(ret,rec(i+1,A[0],1,st)+(turn!=1));
        A[1]--;
    }
    return ret;
}
int main() {
    freopen("B-large.in","r",stdin);
    freopen("out0.txt","w",stdout);
    int t;
    cin >> t;
    rep(cc,t) {

        cur = cc+1;
        int Ac,Aj,x,y;
        cin >> Ac >> Aj;
        bool flag = 0;

                    if(flag)

        cout << Ac << " " << Aj << "\n";
        rep(j,2000) {
            P[j][0] = P[j][1] = 0;
        }
        rep(i,Ac) {
            cin >> x >> y;
                        if(flag)

                    cout << x << " " << y << "\n";

            for(int j=x;j<y;j++) {
                P[j][0] = 1;
            }
        }
        rep(i,Aj) {
            cin >> x >> y;
            if(flag)
                    cout << x << " " << y << "\n";

            for(int j=x;j<y;j++) {
                P[j][1] = 1;
            }
        }
        cout << "Case #"<<cc+1<<": ";
        cout << rec(0,0,2,2) << "\n";

    }
}
