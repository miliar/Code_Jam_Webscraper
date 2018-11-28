#include <bits/stdc++.h>
#define X first
#define Y second

#define bitAt(a,b) (a & (1<<b))

using namespace std;

typedef long long LL;
typedef pair <int, int> PII;
typedef pair <LL,LL> PLL;

const int Maxn = 100*1000 + 250;
const int Mod = 1000 * 1000 * 1000 + 7;
const int abMax = 1 << 30 ;
const double EPS = 1e-7;
const double PI = acos(-1.0);

ofstream fout ("A-large.out");
ifstream fin ("A-large.in");

#define cin fin
#define cout fout

LL T , D , N , K ,S;
double ans = 0;

int main() {
	ios::sync_with_stdio(0);
	cin >> T;
	for(int ttt = 1; ttt <= T ; ttt++){

        cin >> N >> D;
        cin >> K >> S;
        K = N - K;
        for(int i =  1 ; i < D ; i++){
            LL kk , ss;
            cin >> kk >> ss;
            kk = N - kk;
            if (ss * K < S * kk ){
                K = kk;
                S = ss;
            }
        }
        //cerr << K << ' ' << S << endl ;
        ans = (double)(N * S) / (double)K;
        cout << "Case #" << ttt << ": ";
        cout << fixed << setprecision(6) << ans << endl;

	}
}
