#include<bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define pb push_back
#define mp make_pair
#define eb emplace_back

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

template<class T>
using min_queue = priority_queue<T, vector<T>, greater<T>>;

const int INF = 2147483647; // (1 << 30) - 1 + (1 << 30)
const ll LLINF = (1LL << 62) - 1 + (1LL << 62); // = 9.223.372.036.854.775.807
const double PI = acos(-1.0);

// lambda-expression: [] (args) -> retType { body }

int cnt[4];

int calc2()
{
	return cnt[0] + ((1 + cnt[1]) / 2);
}

int calc3()
{
	int ret = cnt[0];
	ret += min(cnt[1], cnt[2]);
	ret += (abs(cnt[1] - cnt[2]) + 2) / 3;
	return ret;
}

int calc4()
{
	int ret = cnt[0];

}

bool run(int tc)
{
	int N, P;
	cin >> N >> P;
	fill_n(cnt, 4, 0);
	for (int i = 0; i < N; i++) {
		int G;
		cin >> G;
		cnt[G % P]++;
	}
	for (int i = 0; i < P; i++) cerr << i << ": " << cnt[i] << endl;

	int ans;
	if (P == 2) ans = calc2();
	else if (P == 3) ans = calc3();
	else ans = calc4();
	
	cout << "Case #" << tc << ": ";
	cout << ans;
	cout << endl;
	return true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	(cout << fixed).precision(10);	// set floating point precision

	int ntc;
	cin >> ntc;
	for (int i = 1; i <= ntc; i++) {
		if (!run(i)) {
			cerr << "Something went wrong" << endl;
		}
	}
	return 0;
}
