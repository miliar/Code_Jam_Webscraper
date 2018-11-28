#include <bits/stdc++.h>
#define X first
#define Y second

#define bitAt(a,b) (a & (1<<b))

using namespace std;

typedef long long LL;
typedef pair <int, int> PII;
typedef pair <LL,LL> PLL;

const int Maxn = 1000 + 250;
const int Mod = 1000 * 1000 * 1000 + 7;
const int abMax = 1 << 30 ;
const double EPS = 1e-9;
const double PI = acos(-1.0);

ofstream fout ("A.out");
ifstream fin ("A-small-attempt0.in");

#define cin fin
#define cout fout

int TT , N , K;
pair <double , double> pan[Maxn];
double dp[Maxn][Maxn];

double solve (int n , int k){

    if(dp[n][k] != 0){
        return dp[n][k];
    }
    if(k > n+1){
        return -abMax;
    }
    if(k == 0 || n < 0){
        return 0;
    }

    double ans = solve (n-1,k);
    double tmp = solve (n-1,k-1);
    tmp += pan[n].X * pan[n].Y * PI * 2;
    dp[n][k] = max(ans,tmp);

    return dp[n][k];

}


int main() {
	ios::sync_with_stdio(0);
	cin >> TT;
	for(int ttt = 1 ; ttt <= TT ; ttt++){

        cin >> N >> K;
        for(int i = 0 ; i < N+1 ; i++){
            for(int j = 0 ; j < K+1 ; j++){
                dp[i][j] = 0;
            }
        }
        for(int i = 0 ; i < N ; i++){
            cin >> pan[i].X >> pan[i].Y;
        }

        sort(pan,pan+N);

        solve(N-1,K);

        double ans = -1;
        for(int i = K-1; i < N; i++){
            double tmp = pan[i].X * pan[i].X * PI;
            tmp += 2 * PI * pan[i].X * pan[i].Y;
            ans = max (ans , dp[i-1][K-1] +  tmp );
        }
        cout << "Case #" << ttt << ": ";
        cout << fixed << setprecision(9) << ans << endl;

	}
}
