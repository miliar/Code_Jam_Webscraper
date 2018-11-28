#include<bits/stdc++.h>
#define int long long
#define sqr(x) (x) * (x)
#define ld long double
 using namespace std;


 const int N = 1445,M = 722, K = 4,L=2, inf = 2e8;
 int dp[N][M][K][L],used[3][N],t,tt,i,n,m,l,r,j,k;

 void up(int &a,int b){
    if(b<a)a=b;
 }

 //int
  main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin >> t;
    for(tt=1;tt<=t;++tt){
        cout << "Case #"<<tt<<": ";
        cin >> n >> m;
        for(i = 0; i <= 24 * 60; ++i)
            used[0][i] = used[1][i] = 0;

        for(i = 1; i <= n; ++i){
            cin >> l >> r;
            for(j = l; j < r; ++j)
                used[0][j] = 1;
        }

        for(i = 1; i <= m; ++i){
            cin >> l >> r;
            for(j = l; j < r; ++j)
                used[1][j] = 1;
        }

        for(i = 0; i <= 24 * 60; ++i)
            for(j = 0; j <= 722; ++j)
            for(k = 0; k < 2; ++k)
                for(l = 0; l < 2; ++l)
            dp[i][j][k][l] = inf;

            if(!used[0][0]) dp[0][1][0][0] = 0;
            if(!used[1][0]) dp[0][0][1][1] = 0;

            int mx = 0;
            for(i = 0; i < 24 * 60; ++i)
                for(j = 0; j <= 720; ++j)
                for(k = 0; k < 2; ++k)
                    for(l = 0; l < 2; ++l)
            if(dp[i][j][k][l] < inf){
                if(k == 0){
                if(!used[0][i+1] && j+1<=720)
                    up(dp[i+1][j+1][0][l],dp[i][j][k][l]);
                if(!used[1][i+1])
                    up(dp[i+1][j][1][l],dp[i][j][k][l] + 1);
                }else{
                if(!used[0][i+1] && j+1<=720)
                    up(dp[i+1][j+1][0][l],dp[i][j][k][l] + 1);
                if(!used[1][i+1])
                    up(dp[i+1][j][1][l],dp[i][j][k][l]);

                }
            }

            cout << min({dp[1439][720][0][1] + 1,
                        dp[1439][720][0][0],
                        dp[1439][720][1][1],
                        dp[1439][720][1][0] + 1,
            }) << '\n';

       }

 }
