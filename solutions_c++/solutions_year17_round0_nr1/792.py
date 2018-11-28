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

int a[11000];
int N, K;

void read(ifstream &fin) {
 string S;
 fin >> S >> K;
 N = sz(S);
 frr(i, N) a[i] = (S[i] == '+');
}

void proc(ofstream &fout) {
 int ans = 0;
 frr(i, N - (K - 1)) {
  if(!a[i]) {
   ans++;
   for(int j = i; j < i + K; ++j) {
    a[j] = !a[j];
   }
  }
 }


 frr(i, N) if(!a[i]) ans = -1;

 if(ans == -1) {
  fout << "IMPOSSIBLE" << endl;
 } else {
  fout << ans << endl;
 }
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
