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

int a[100];
int N;

void read(ifstream &fin) {
 string S;
 fin >> S;
 N = sz(S);
 frr(i, N) {
  a[N - i - 1] = S[i] - '0';
 }
}

void proc(ofstream &fout) {
 frr(i, N - 1) {
  if(a[i] < a[i + 1]) {
   a[i + 1]--;
   for(int j = i; j >= 0; --j) a[j] = 9;
  }
 }

 for(; N > 0; --N) {
  if(a[N - 1] > 0) break;
 }

 for(int i = N - 1; i >= 0; --i) {
  fout << a[i];
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
