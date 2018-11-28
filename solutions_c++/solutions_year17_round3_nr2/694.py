#include<bits/stdc++.h>

#define x first
#define y second
#define y0 hi1
#define y1 hi2
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(a) (a)*(a)
#define ld long double
#define all(a) (a).begin(), (a).end()

using namespace std;

const int inf = 2000000000;
const int N = 1440;
const int M = 720;

int dp[N + 5][M + 5][2][2];
pair<int, int> a[2][N + 10];
int n, m;
int L[2];

bool can(int p, int j){
    int k = (p ? m : n);

    while(L[p] < k && a[p][L[p]].y < j){
        L[p]++;
    }

    if(L[p] < k){
        if(a[p][L[p]].x < j && j <= a[p][L[p]].y){
            return false;
        }
    }
    return true;
}

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    cin >> T;
    for(int _num = 1; _num <= T; _num++){
        cout << "Case #" << _num << ": ";

        cin >> n >> m;

        for(int i = 0; i < n; i++){
            cin >> a[0][i].x >> a[0][i].y;
        }
        sort(a[0], a[0] + n);

        for(int i = 0; i < m; i++){
            cin >> a[1][i].x >> a[1][i].y;
        }
        sort(a[1], a[1] + m);

        L[0] = L[1] = 0;

        for(int i = 0; i <= N; i++){
            for(int sum = 0; sum <= M; sum++){
                for(int j = 0; j < 2; j++){
                    for(int c = 0; c < 2; c++){
                        dp[i][sum][j][c] = inf;
                    }
                }
            }
        }


        dp[0][0][0][0] = 1;
        dp[0][0][1][1] = 1;

        for(int i = 1; i <= N; i++){
            int res = inf;
            for(int sum = 0; sum < min(M, i); sum++){
                for(int c1 = 0; c1 < 2; c1++){
                    for(int c2 = 0; c2 < 2; c2++){
                        if(can(0, i)){
                            int p = sum;
                            if(p + 1 <= M && i - p - 1 <= M){
                                if(dp[i - 1][p][0][c1] <= dp[i - 1][i - p - 1][1][c2] + 1){
                                    dp[i][p + 1][0][c1] = dp[i - 1][p][0][c1];
                                }
                                if(dp[i - 1][p][0][c1] >= dp[i - 1][i - p - 1][1][c2] + 1){
                                    dp[i][p + 1][0][c2] = dp[i - 1][i - p - 1][1][c2] + 1;
                                }
                            }
                        }
                        if(can(1, i)){
                            int p = sum;
                            if(p + 1 <= M && i - p - 1 <= M){
                                if(dp[i - 1][p][1][c1] <= dp[i - 1][i - p - 1][0][c2] + 1){
                                    dp[i][p + 1][1][c1] = dp[i - 1][p][1][c1];
                                }
                                if(dp[i - 1][p][1][c1] >= dp[i - 1][i - p - 1][0][c2] + 1){
                                    dp[i][p + 1][1][c2] = dp[i - 1][i - p - 1][0][c2] + 1;
                                }
                            }
                        }
                    }
                }
            }
        }

        int ans = inf;
        for(int c = 0; c < 2; c++){
            ans = min(ans, min(dp[N][M][0][c] - (c == 0), dp[N][M][1][c] - (c == 1)));
        }
        cout << ans << "\n";
    }
}

