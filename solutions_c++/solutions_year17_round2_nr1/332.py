#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}


int N, D;
int K[1010];
int S[1010];

int main(){
    fastStream();
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        printf("Case #%d: ", t);
        // cout << "Case #" << t << ":";
        cin >> D >> N;
        for(int i = 0; i < N; i++){
            cin >> K[i] >> S[i];
        }
        double ans = -(1LL << 60);
        for(int i = 0; i < N; i++){
            double t = 1.0 * (D - K[i]) / S[i];
            ans = max(ans, t);
        }
        printf("%.10f\n", D / ans);
    }
    return 0;
}
