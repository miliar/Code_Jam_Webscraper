/**
 * Problem: A
 */
#include <algorithm>
#include <assert.h>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
#include <stdexcept>
#include <typeinfo>

#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
#define TR(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

using namespace std;

typedef long long ll;
typedef vector<vector<int> > vvi;
typedef vector<int> vi;

int K[1050];
int S[1050];

int main(int argc, const char **argv) {
  int cases;
  cin >> cases;
  int D, N;

  long double time, tm;
  F1(caseI, cases) {
    cin >> D >> N;
    tm = 0;
    F0(i, N) {
      cin >> K[i] >> S[i];
      time = (D - K[i])/(double)S[i];
      if (time > tm) tm = time;
    }

    cout << "Case #" << caseI << ": ";
    printf("%Lf\n", D / tm);
  }

  return 0;
}

