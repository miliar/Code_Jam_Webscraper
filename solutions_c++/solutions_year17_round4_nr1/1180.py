#include<fstream>
#include<vector>

using namespace std;
//using namespace __gnu_pbds;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
//typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> ordered_set;

#define FOR(i, a, b) for (int i=a; i<b; i++)
#define F0R(i, a) for (int i=0; i<a; i++)
#define FORd(i,a,b) for (int i = (b)-1; i >= a; i--)
#define F0Rd(i,a) for (int i = (a)-1; i >= 0; i--)

#define mp make_pair
#define pb push_back
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound

const int MOD = 1000000007;

ifstream cin ("Input.txt");
ofstream cout ("Output.txt");
//copy over to xcode

int T,N,P,cur[4], dp[102][102][102][102];

int main() {
    cin >> T;
    FOR(i,1,T+1) {
        cin >> N >> P;
        F0R(j,4) cur[j] = 0;
        F0R(j,N) {
            int x; cin >> x;
            cur[x%P] ++;
        }
        F0R(a,cur[0]+1) F0R(b,cur[1]+1) F0R(c,cur[2]+1) F0R(d,cur[3]+1) dp[a][b][c][d] = 0;
        F0R(a,cur[0]+1) F0R(b,cur[1]+1) F0R(c,cur[2]+1) F0R(d,cur[3]+1) {
            int z = dp[a][b][c][d];
            int csum = b+2*c+3*d;
            if (csum % P == 0) z++;
            dp[a+1][b][c][d] = max(dp[a+1][b][c][d],z);
            dp[a][b+1][c][d] = max(dp[a][b+1][c][d],z);
            dp[a][b][c+1][d] = max(dp[a][b][c+1][d],z);
            dp[a][b][c][d+1] = max(dp[a][b][c][d+1],z);
        }
        cout << "Case #" << i << ": " << dp[cur[0]][cur[1]][cur[2]][cur[3]] << "\n";
    }
}
