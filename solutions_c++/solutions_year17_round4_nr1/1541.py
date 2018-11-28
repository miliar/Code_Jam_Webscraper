#include <iostream>
#include <cstdio>  
#include <iostream>  
#include <string>  
#include <iterator>  
#include <algorithm>  
#include <vector>  
#include <cstring>  
#include <array>  
#include <queue>  
#include <set>  
#include <map>  
using namespace std;

int T, N, P;
int dp[101][101][101][4];

int main()  
{  
    freopen("A-large.in.txt", "r", stdin);  
    //freopen("in.txt", "r",stdin);  
    freopen("out.txt", "w", stdout);  
    scanf("%d", &T);  
    for (int i = 1; i<= T; i++)  
    {  
        cin>>N>>P;
        int c[4] = {0};
        memset(c, 0, sizeof(c));
        memset(dp, 0, sizeof(dp));
        int people;
        for(int l=0;l<N;l++) {
            cin>>people;
            c[people % P]++;
        }
        dp[c[1]][c[2]][c[3]][0] = c[0];

        for(int j=c[1];j>=0;j--) {
            for(int k=c[2];k>=0;k--) {
                for(int l=c[3];l>=0;l--) {
                    for(int m=P-1;m>=0;m--) {
                        if(j>0)
                            dp[j-1][k][l][(m-1+P)%P] = max(dp[j][k][l][m] + int(m == 0), dp[j-1][k][l][(m-1+P)%P]);
                        if(k>0)
                            dp[j][k-1][l][(m-2+P)%P] = max(dp[j][k][l][m] + int(m == 0), dp[j][k-1][l][(m-2+P)%P]);
                        if(l>0)
                            dp[j][k][l-1][(m-3+P)%P] = max(dp[j][k][l][m] + int(m == 0), dp[j][k][l-1][(m-3+P)%P]);
                        // cout<<j<<" "<<k<<" "<<l<<" "<<m<<" "<<dp[j][k][l][m]<<endl;
                    }
                }
            }
        }
        printf("Case #%d: ", i);
        int res = max(max(max(dp[0][0][0][0], dp[0][0][0][1]), dp[0][0][0][2]), dp[0][0][0][3]);
        cout<<res<<endl;
    }  
    return 0;  
}  