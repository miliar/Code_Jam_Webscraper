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

int N, P;
int R[5];

void read(ifstream &fin) {
    fin >> N >> P;
    for (int i = 0; i < P; ++i) {
        R[i] = 0;
    }
    for (int i = 0; i < N; ++i) {
        int x;
        fin >> x;
        R[x % P]++;
    }
}

void proc(ofstream &fout) {
    int ans = R[0];
    if(P == 2) {
        ans += (R[1] + 1) / 2;
    } else if(P == 3) {
        ans += min(R[1], R[2]);
        ans += (max(R[1], R[2]) - min(R[1], R[2]) + 2) / 3;
    } else {
        int m = min(R[1], R[3]);
        ans += m;
        R[1] -= m;
        R[3] -= m;
        ans += R[2] / 2;
        ans += (R[1] + R[3] + (R[2] % 2) + 3) / 4;
    }

    fout << ans << endl;
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
