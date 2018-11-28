#include <bits/stdc++.h>

using namespace std;

#define all(s) s.begin(), s.end()
#define ms(a, v) memset(a, v, sizeof a)
#define mp make_pair
#define fo() freopen("in.txt", "r", stdin)

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

const int oo = 1 << 30;
const int maxn = 1e5 + 1;
const int mod = 1e9 + 7;

int dr[] = { 0, -1, 0, 1 };
int dc[] = { 1, 0, -1, 0 };

template <class T> inline T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
template <class T> inline T pow(T b, T p) { if (!p) return (T)1; T sq = pow(b, p >> ((T)1)); sq *= sq; if (p & ((T)1)) sq *= b; return sq; }

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	fo();
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int Case = 1; Case <= t; Case++)
	{
		string s;
		int k;

		cin >> s >> k;

		int ans = 0;
		bool f = 0;

		int l = s.size();

		while (1){
			int neg_idx = s.find("-");

			if (neg_idx == -1){
				break;
			}
			else if (neg_idx > l - k){
				f = 1;
				printf("Case #%d: IMPOSSIBLE\n", Case);
				break;
			}
			else{
				for (int i = neg_idx; i < neg_idx + k; i++)
				{
					s[i] = s[i] == '+' ? '-' : '+';
				}
				ans++;
			}
		}

		if (!f){
			printf("Case #%d: %d\n", Case, ans);
		}
	}

	return 0;
}