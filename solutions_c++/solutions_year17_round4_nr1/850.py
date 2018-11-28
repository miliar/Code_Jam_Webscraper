#include <bits/stdc++.h>

using namespace std;

int dp3[128][128];
int dp4[128][128][128];

void solve(int caseNumber) {
    int n, p;
    cin >> n >> p;
    vector<int> vec(p,0);
    for(int i=0;i<n;i++) {
        int a;
        cin >> a;
        vec[a%p]++;
    }
    int res = vec[0];
    if(p == 2) {
        res += (vec[1]+1)/2;
    } else if(p == 3) {
        memset(dp3,0,sizeof(dp3));
        for(int i1=0;i1<100;i1++) {
            for(int i2=0;i2<100;i2++) {
                if(i1>=1 && i2>=1) {
                    dp3[i1][i2] = max(dp3[i1][i2],dp3[i1-1][i2-1]+1);
                }
                if(i1>=3) {
                    dp3[i1][i2] = max(dp3[i1][i2],dp3[i1-3][i2]+1);
                }
                if(i2>=3) {
                    dp3[i1][i2] = max(dp3[i1][i2],dp3[i1][i2-3]+1);
                }
            }
        }
        res += dp3[vec[1]][vec[2]];
        if((vec[1]+2*vec[2])%3!=0) {
            res++;
        }
    } else {
        memset(dp4,0,sizeof(dp4));
        for(int i1=0;i1<100;i1++) {
            for(int i2=0;i2<100;i2++) {
                for(int i3=0;i3<100;i3++) {
                    if(i1>=4) {
                        dp4[i1][i2][i3] = max(dp4[i1][i2][i3],dp4[i1-4][i2][i3]+1);
                    }
                    if(i2>=2) {
                        dp4[i1][i2][i3] = max(dp4[i1][i2][i3],dp4[i1][i2-2][i3]+1);
                    }
                    if(i3>=4) {
                        dp4[i1][i2][i3] = max(dp4[i1][i2][i3],dp4[i1][i2][i3-4]+1);
                    }
                    if(i1>=2 && i2>=1) {
                        dp4[i1][i2][i3] = max(dp4[i1][i2][i3],dp4[i1-2][i2-1][i3]+1);
                    }
                    if(i1>=1 && i3>=1) {
                        dp4[i1][i2][i3] = max(dp4[i1][i2][i3],dp4[i1-1][i2][i3-1]+1);
                    }
                    if(i2>=1 && i3>=2) {
                        dp4[i1][i2][i3] = max(dp4[i1][i2][i3],dp4[i1][i2-1][i3-2]+1);
                    }
                }
            }
        }
        res += dp4[vec[1]][vec[2]][vec[3]];
        if((vec[1]+2*vec[2]+3*vec[3])%4!=0) {
            res++;
        }
    }
    printf("Case #%d: %d\n",caseNumber,res);
}

int main() {
    int casos;
    cin >> casos;
    for(int i=1;i<=casos;i++) {
        solve(i);
    }
}