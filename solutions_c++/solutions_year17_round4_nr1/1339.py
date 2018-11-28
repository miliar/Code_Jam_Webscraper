#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define  ll long long int
#define pi pair<ll,ll>
#define f first
#define s second
#define pb push_back
#define pii pair<pi,ll>
#define VI vector<int>
int calc(int P,int rem,int md) {
    rem-=md;
    rem+=3*P;
    rem%=P;
    return rem;
}
bool vis2[2][101][101];
bool vis3[3][101][101][101];
bool vis4[4][101][101][101][101];

int dp2[2][101][101];
int dp3[3][101][101][101];
short dp4[4][101][101][101][101];

int rec4(int rem,int a0,int a1,int a2,int a3) {
    if(a0==0 and a1==0 and a2==0 and a3==0) return 0;
    if(vis4[rem][a0][a1][a2][a3]) {
        return dp4[rem][a0][a1][a2][a3];
    }
    vis4[rem][a0][a1][a2][a3] = 1;
    int  ret = 0;

    if(a0)
        ret = max(ret,rec4(calc(4,rem,0),a0-1,a1,a2,a3)+ (rem==0));

    if(a1)
        ret = max(ret,rec4(calc(4,rem,1),a0,a1-1,a2,a3)+(rem==0));
    if(a2)
        ret = max(ret,rec4(calc(4,rem,2),a0,a1,a2-1,a3 )+(rem==0));

    if(a3)
        ret = max(ret,rec4(calc(4,rem,3),a0,a1,a2,a3-1)+(rem==0));
    return dp4[rem][a0][a1][a2][a3] = ret;
}
int rec3(int rem,int a0,int a1,int a2) {
    if(a0==0 and a1==0 and a2==0) return 0;
    if(vis3[rem][a0][a1][a2]) {
        return dp3[rem][a0][a1][a2];
    }
    vis3[rem][a0][a1][a2] = 1;
    int &ret = dp3[rem][a0][a1][a2];
    ret = 0;
    if(a0)
        ret = max(ret,rec3(calc(3,rem,0),a0-1,a1,a2)+(rem==0));
    if(a1)
        ret = max(ret,rec3(calc(3,rem,1),a0,a1-1,a2)+(rem==0));

    if(a2)
        ret = max(ret,rec3(calc(3,rem,2),a0,a1,a2-1 )+(rem==0));
    return ret;
}


int rec2(int rem,int a0,int a1) {
    if(a0==0 and a1==0 ) return 0;
    if(vis2[rem][a0][a1]) {
        return dp2[rem][a0][a1];
    }
    vis2[rem][a0][a1] = 1;
    int &ret = dp2[rem][a0][a1];
    ret = 0;
    if(a0)
        ret = max(ret,rec2(calc(2,rem,0),a0-1,a1)+(rem==0));
    if(a1)
        ret = max(ret,rec2(calc(2,rem,1),a0,a1-1)+(rem==0));
    return ret;
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    int curt = 1;
    while(T--) {
        int N,P,x;
        cin >> N >> P;
        int f[10]={0};
        rep(i,N) {
            cin >> x;
            f[x%P]++;
        }
        cout << "Case #"<<curt++ <<": ";
        if(P==2) {
            cout << rec2(0,f[0],f[1]) << "\n";
        }
        else if (P==3) {
            cout << rec3(0,f[0],f[1],f[2]) << "\n";
        }
        else{
            cout << rec4(0,f[0],f[1],f[2],f[3]) << "\n";
        }
    }
}
