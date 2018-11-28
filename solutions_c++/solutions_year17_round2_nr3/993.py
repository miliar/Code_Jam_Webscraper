#pragma comment(linker, ”/STACK:38777216“
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <time.h>
#include <map>
#include <set>

using namespace std;

const int N = 105;
const int inf = 1000 * 1000 * 1000;
const int mod = 1000 * 1000 * 1000 + 7;

int t,n,q,k;
double s[N],v[N];
double a[N][N];
double dp[N];

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    cout.setf(ios::fixed);
    cout.precision(8);
    cin>>t;
    while(t--){
        k++;
        cin>>n>>q;
        for(int i=1;i<=n;i++)cin>>s[i]>>v[i];
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                cin>>a[i][j];
            }
        }
        int S , E;
        cin>>S>>E;
        dp[S] = 0.0;
        for(int i=2;i<=n;i++){
            dp[i] = -1;
            for(int j=1;j<i;j++){
                double time = 0.0 , sum = 0.0;
                for(int h=j;h<i;h++)sum += a[h][h+1];
                if(s[j] >= sum){
                    if(dp[i] == -1 || dp[j] + sum / v[j] < dp[i])
                        dp[i] = dp[j] + sum / v[j];
                }
            }
        }
        printf("Case #%d: ",k);
        cout<<dp[n]<<endl;
    }
    return 0;
}
