#include<bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define pb push_back
#define eb emplace_back

typedef long long ll;
typedef pair<int, int> pii;

template<class T>
using min_heap = priority_queue<T, vector<T>, greater<T> >;

const ll inf = 1e17;
const int maxn = 100;

int N, Q, E[maxn], S[maxn], D[maxn][maxn];
ll sumDist[maxn][maxn];

double d2[maxn][maxn];

void precalc()
{
	// for (int i = 0; i < N; i++) {for (int j = 0; j < N; j++) cerr << D[i][j] << " ";cerr << endl;}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			sumDist[i][j] = D[i][j] == -1 ? inf : D[i][j];
		}
	}

	for (int k = 0; k < N; k++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				sumDist[i][j] = min(sumDist[i][j], sumDist[i][k] + sumDist[k][j]);
			}
		}
	}

	// for (int i = 0; i < N; i++) {for (int j = 0; j < N; j++) cerr << sumDist[i][j] << " ";cerr << endl;}
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (sumDist[i][j] <= E[i]) {
				d2[i][j] = 1.0 * sumDist[i][j] / S[i];
			} else {
				d2[i][j] = inf;
			}
			// cerr << d2[i][j] << " ";
		}
		// cerr << endl;
	}

	for (int k = 0; k < N; k++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j]);
			}
		}
	}
}

double calc(int fr, int to)
{
	return d2[fr - 1][to - 1];
}

bool run(int tc)
{
	cin >> N >> Q;
	for (int i = 0; i < N; i++) cin >> E[i] >> S[i];
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> D[i][j];

	precalc();

	cout << "Case #" << tc << ":";
	for (int i = 0; i < Q; i++) {
		int U, V;
		cin >> U >> V;
		cout << " " << calc(U, V);
	}
	cout << endl;
	return true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	(cout << fixed).precision(10);

	int ntc;
	cin >> ntc;
	for (int i = 1; i <= ntc; i++) {
		if (!run(i)) {
			cerr << "Something went wrong" << endl;
		}
	}
	return 0;
}
