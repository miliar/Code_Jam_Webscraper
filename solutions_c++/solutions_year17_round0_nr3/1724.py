#include <bits/stdc++.h>

using namespace std;

#define D(x)
#define REP(i,a,b) for (int i = (a); i < (b); ++i)
#define REPR(i,a,b) for (int i = (b) - 1; i >= (a); --i)
#define mp make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<vector<int> > VII;

ifstream fin ("C-large.in");
ofstream fout ("C-large.out");

int main() {
    ios_base::sync_with_stdio(false);
    cout << setprecision(12) << fixed;

    int T; fin >> T;
    REP(t,1,T+1) {
        ull N, K;
        fin >> N >> K;
        map<ull, ull> pq;
        pq[N] = 1ull;
        while (true) {
            ull len = pq.rbegin()->first;
            ull num = pq.rbegin()->second;
            D(cout << "len: " << len << ", num: " << num << endl;)
            pq.erase(len);
            if (K <= num) {
                fout << "Case #" << t << ": " << (len/2) << " " << ((len-1)/2) << endl;
                break;
            }
            K -= num;
            if (len % 2 == 1) {
                pq[len / 2] += num * 2;
            } else {
                pq[len / 2] += num;
                pq[len / 2 - 1] += num;
            }
        }
    }

	return 0;
}
