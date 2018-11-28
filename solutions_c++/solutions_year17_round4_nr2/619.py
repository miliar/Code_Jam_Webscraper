#include <vector>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

#define PRINT(x) cout << "DEBUG " << #x << " = " << x <<  endl;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i = 0; i < (n); i++)
#define frr(i, n) for(int i = 0; i < (n); i++)
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long ll;

int N, C, M;
int sum[1100];
int sumCustomer[1100][1100];
int cum[1100];
int cumCustomer[1100][1100];

void read(ifstream &fin) {
    _cl(sum);
    _cl(sumCustomer);
    fin >> N >> C >> M;
    for(int i = 0; i < M; ++i) {
        int c, p;
        fin >> p >> c;
        --p, --c;
        sum[p]++;
        sumCustomer[c][p]++;
    }
}

void proc(ofstream &fout) {
    _cl(cum);
    _cl(cumCustomer);

    frr(i, N) {
        cum[i + 1] = cum[i] + sum[i];
        frr(c, C) {
            cumCustomer[c][i + 1] = cumCustomer[c][i] + sumCustomer[c][i];
        }
    }

    int ans = 0;
    frr(i, N) {
        ans = max(ans, (cum[i + 1] + i) / (i + 1));
        frr(c, C) {
            ans = max(ans, cumCustomer[c][i + 1]);
        }
    }

    int promoted = 0;
    frr(i, N) {
        if(ans >= sum[i]) continue;
        promoted += sum[i] - ans;
    }

    fout << ans << " " << promoted << endl;
}

int main() {
 int i;
 int NT;

 ifstream fin("in");
 ofstream fout("out");
 string ln;

 getline(fin, ln);
 istringstream is(ln);
 is >> NT;

 fr(i, NT)
 {
  read(fin);
  fout << "Case #" << i + 1 << ": ";
  cout << "Case #" << i + 1 << endl;
  proc(fout);
 }

 return 0;
}
