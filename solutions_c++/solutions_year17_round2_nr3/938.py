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

const double inf = 1e20;

int N, Q;
double a[1100][1100];
double hourseDistance[1100], hourseSpeed[1100];
int from[1100], to[1100];

void read(ifstream &fin) {
 fin >> N >> Q;
 frr(i, N) {
  fin >> hourseDistance[i] >> hourseSpeed[i];
 }

 frr(i, N) frr(j, N) {
  fin >> a[i][j];
  if(a[i][j] < 0) a[i][j] = inf;
 }
 frr(i, N) a[i][i] = 0;

 frr(i, Q) {
  fin >> from[i] >> to[i];
  from[i]--;
  to[i]--;
 }
}

void floyd() {
 frr(k, N) frr(i, N) frr(j, N) {
  a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
 }
}

void proc(ofstream &fout) {
 floyd();

 frr(i, N) {
  frr(j, N) {
   if(a[i][j] <= hourseDistance[i]) {
    a[i][j] = a[i][j] / hourseSpeed[i];
   } else {
    a[i][j] = inf;
   }
  }
 }

 frr(i, N) a[i][i] = 0;

 floyd();

 frr(i, Q) {
  if(i > 0) {
   fout << " ";
  }

  fout << setiosflags(ios::fixed) << setprecision(6) << a[from[i]][to[i]];
 }
 fout << endl;
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
