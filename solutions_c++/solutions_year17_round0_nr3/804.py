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

typedef struct PAIR {
 long long large;
 long long small;
 long long largeCount;
 long long smallCount;
} PAIR;

long long N, K;

void read(ifstream &fin) {
 fin >> N >> K;
}

PAIR split(long long value, long long count) {
  PAIR r;
  value--;
  r.small = value / 2;
  r.large = value - r.small;
  if(r.large == r.small) {
   r.largeCount = 2 * count;
   r.smallCount = 0;
   r.small--;
  } else {
   r.largeCount = count;
   r.smallCount = count;
  }

  return r;
}

long long calculate() {
 if(K == 1) {
  return N;
 }

 K -= 1;
 PAIR n = split(N, 1);

 while(true) {
  if(n.largeCount >= K) {
   return n.large;
  }
  K -= n.largeCount;
  PAIR large = split(n.large, n.largeCount);

  if(n.smallCount >= K) {
   return n.small;
  }
  K -= n.smallCount;
  PAIR small = split(n.small, n.smallCount);

  if(small.large == large.large) {
   large.largeCount += small.largeCount;
   large.smallCount += small.smallCount;
  } else {
   large.smallCount += small.largeCount;
  }
  n = large;
 }

 return 0LL;
}

void proc(ofstream &fout) {
 long long gap = calculate() - 1;
 long long left = gap / 2;
 fout << gap - left << " " << left << endl;
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
