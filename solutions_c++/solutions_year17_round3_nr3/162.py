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

int N, K;
double U;
double a[100];

void read(ifstream &fin) {
 fin >> N >> K;
 fin >> U;
 frr(i, N) {
  fin >> a[i];
 }
 sort(a, a + N);
 reverse(a, a + N);
}

void distribute(double v, int i) {
 v = min(v, 1.0);
 for(; i < K; ++i) a[i] = v;
}

void proc(ofstream &fout) {
 double sum = a[K - 1];
 for(int i = K - 2; i >= 0; --i) {
  int n = K - i - 1;
  if(n * a[i] > sum + U) {
   distribute((sum + U) / n, i + 1);
   U = -1;
   break;
  }
  sum += a[i];
 }

 if(U > 0) {
  distribute((sum + U) / K, 0);
 }

 double prob = 1;
 frr(i, K) {
  prob *= a[i];
 }

 fout << setiosflags(ios::fixed) << setprecision(7) << prob << endl;
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
