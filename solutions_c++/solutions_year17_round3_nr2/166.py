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

const int inf = 1 << 20;
int a[2][2][1000][1000];
bool occupied[2][2000];

void read(ifstream &fin) {
 _cl(occupied);
 int n[2];
 fin >> n[0] >> n[1];
 frr(k, 2) {
  frr(j, n[k]) {
   int f, t;
   fin >> f >> t;
   for(int i = f; i < t; ++i) {
    occupied[k][i] = true;
   }
  }
 }
}

void proc(ofstream &fout) {
 _cl(a);


 frr(i, 722) {
  frr(s, 2) frr(k, 2) {
   a[s][k][721][i] = inf;
   a[s][k][i][721] = inf;
  }
 }
 a[0][0][720][720] = a[1][1][720][720] = 0;
 a[0][1][720][720] = a[1][0][720][720] = 1;

 for(int i = 720; i >= 0; --i) {
  for(int j = 720; j >= 0; --j) {
   int t = i + j;
   if(t >= 1440) continue;
   frr(s, 2) {
    frr(k, 2) {
     if(occupied[k][t]) {
      a[s][k][i][j] = inf;
     } else {
      if(k == 0) {
       a[s][k][i][j] = min(a[s][k][i + 1][j], a[s][1 - k][i + 1][j] + 1);
      } else {
       a[s][k][i][j] = min(a[s][k][i][j + 1], a[s][1 - k][i][j + 1] + 1);
      }
     }
    }
   }
  }
 }

 fout << min(a[0][0][0][0], a[1][1][0][0]) << endl;
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
