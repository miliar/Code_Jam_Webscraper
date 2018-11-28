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

const int N = 1005;
const int inf = 1000 * 1000 * 1000;
const int mod = 1000 * 1000 * 1000 + 7;

int n,k,t,test;
double eps = 1e-8;
pair <double,double> p[N];
double h[N] , r[N];
double dp[N][N];

double area(pair <double,double> P){
    return acos(-1.0) * P.first * P.first;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cout.setf(ios::fixed);
    cout.precision(8);
    cin>>t;
    while(t--){
        test++;
        cin>>n>>k;
        for(int i=1;i<=n;i++)cin>>p[i].first>>p[i].second;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                dp[i][j] = 0.0;
            }
        }
        sort(p+1,p+n+1);
        for(int i=1;i<=n;i++){
            dp[i][1] = 2.0 * acos(-1.0) * p[i].first * p[i].second;
            dp[i][1] += area(p[i]);
            for(int j=2;j<=min(i,k);j++){
                for(int h=j-1;h<i;h++)
                    dp[i][j] = max(dp[i][j] , dp[h][j-1] + area(p[i]) - area(p[h]));
                dp[i][j] += 2.0 * acos(-1.0) * p[i].first * p[i].second;
            }
        }
        double answ = 0.0;
        for(int i=k;i<=n;i++)answ = max(answ , dp[i][k]);
        printf("Case #%d: ",test);
        cout<<answ<<endl;
    }
    return 0;
}
