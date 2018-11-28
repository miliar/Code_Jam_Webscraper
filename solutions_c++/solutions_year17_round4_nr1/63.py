#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
#define all(x) (x).begin(), (x).end()

void read();
void kill();

const int M = 103;
const int inf = 1e6;

int d3[M][M], d4[M][M][M];

void uax(int &x, int y) {
    x = max(x, y);
}

void pre3() {
    for (int i = 0; i < M; ++i)
        for (int j = 0; j < M; ++j)
            d3[i][j] = -inf;

    d3[0][0] = 0;

    for (int i = 0; i + 1 < M; ++i)
        for (int j = 0; j + 1 < M; ++j) {
            int rem = (i + 2 * j) % 3;
            int cur = d3[i][j];
            if (cur < 0)
                continue;
            {
                uax(d3[i + 1][j], cur + (rem == 0 ? 1 : 0));
            }

            {
                uax(d3[i][j + 1], cur + (rem == 0 ? 1 : 0));
            }
        }

    cerr << "p3 don.\n";
}

void pre4() {
    for (int i = 0; i < M; ++i)
        for (int j = 0; j < M; ++j)
            for (int k = 0; k < M; ++k)
                d4[i][j][k] = -inf;

    d4[0][0][0] = 0;

    for (int i = 0; i + 1 < M; ++i)
        for (int j = 0; j + 1 < M; ++j)
            for (int k = 0; k + 1 < M; ++k) {
                int rem = (i + 2 * j + 3 * k) % 4;
                int cur = d4[i][j][k];
                if (cur < 0)
                    continue;
                {
                    uax(d4[i + 1][j][k], cur + (rem == 0 ? 1 : 0));
                }

                {
                    uax(d4[i][j + 1][k], cur + (rem == 0 ? 1 : 0));
                }

                {
                    uax(d4[i][j][k + 1], cur + (rem == 0 ? 1 : 0));
                }
            }
    cerr << "p4 done.\n";
}

int p;
int n;
int sum;
vector<int> cnt;

void read() {
    cin >> n >> p;
    cnt = vector<int>(p, 0);
    sum = 0;

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        cnt[x % p]++;
        sum = (sum + x) % p;
    }
}

void kill() {
    int ans = cnt[0];
    if (p == 2) {
        ans += (cnt[1] + 1) / 2;
    } else if (p == 3) {
        ans += d3[cnt[1]][cnt[2]];
    } else if (p == 4) {
        ans += d4[cnt[1]][cnt[2]][cnt[3]];
    } else {
        assert(!"bad p");
    }
    
    cout << ans << endl;
}

int main() {
  pre3();
  pre4();
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    kill();
    cerr << "Case #" << i << " done.\n";
  }
  return 0;
}
