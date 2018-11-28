#include <bits/stdc++.h>

using namespace std;

#define all(s) s.begin(), s.end()
#define ms(a, v) memset(a, v, sizeof a)
#define mp make_pair
#define fo_read() freopen("in.txt", "r", stdin)
#define fo_write() freopen("out.txt", "w", stdout)

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

bool isTidy(int n){
	string s = to_string(n);

	for (size_t i = 0; i < s.size() - 1; i++)
	{
		if (s[i] > s[i + 1]){
			return 0;
		}
	}

	return 1;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	fo_read();
	fo_write();

	int t;
	cin >> t;

	for (int Case = 1; Case <= t; Case++)
	{
		int n;
		cin >> n;

		for (int i = n; i >= 1; i--)
		{
			if (isTidy(i)){
				printf("Case #%d: %d\n", Case, i);
				break;
			}
		}
	}

	return 0;
}