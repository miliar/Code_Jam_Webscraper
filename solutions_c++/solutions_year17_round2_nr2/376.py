#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

#define FOR(i, s, n) for (int i = (s); i < (n); ++i)
#define FOR2(i, s, n) for (int i = (s); i <= (n); ++i)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

typedef long long ll;
typedef vector<int> vi;

int N, R, O, Y, G, B, V;

// easy
void easy()
{
    char ch[3] = {'R', 'Y', 'B'};
    int cnt[3];
    cnt[0] = R;
    cnt[1] = Y;
    cnt[2] = B;

    int mm = max(max(R, Y), B);
    if (mm * 2 > N) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    int start = 0;
    int prev = 0;
    if (mm == R) { start = 0; }
    else if (mm == Y) {
        start = 1;
    }
    else {
        start = 2;
    }
    prev = start;
    cout << ch[prev];
    --N;
    --cnt[prev];

    while(N) {
        for (int i = 0; i < 3; ++i) {
            int check = (start + i) % 3;
            int next = (start + i + 1) % 3;

            if (next == prev) next = (start + i + 2) % 3;
            if (check == prev) continue;

            if (cnt[check] >= cnt[next]) {
                //cout << ch[check] << " " << ch[next] << " " << cnt[check] << " " << cnt[next] << endl;
                cout << ch[check];
                prev = check;
                --cnt[prev];
                --N;
                break;
            }
        }
    }

    cout << endl;
}

// hard

void solve()
{
    cin >> N >> R >> O >> Y >> G >> B >> V;
    easy();
}

int main()
{
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}