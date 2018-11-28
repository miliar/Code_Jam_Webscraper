/**
 * Problem: B
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
#include <numeric>
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
#define FV(v) for(auto it = v.begin();it!=v.end();++it)
#define TR(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

using namespace std;

typedef long long ll;
typedef vector<ll> vll;


bool isCorrect(long long n) {
  int prev = 9;
  int k;
  while (n > 0) {
    k = n % 10;
    n = n / 10;
    if (k > prev) {
      return false;
    }
    prev = k;
  }
  return true;
}


void print(int n, int caseI) {
  while (!isCorrect(n)) {
    n--;
  }
  cout << "Case #" << caseI << ": " << n << endl;
}

string lower(string str) {
  int k = 0, a, b;
  int size = SZ(str);
  for (int i = size - 2; i >= 0; i--) {
    a = str[i] - 48;
    b = str[i+1] - 48;
    if (a > b) {
      k = i;
      str[k] = str[k] - 1;
      for (int i = k+1; i <= size; i++) {
        str[i] = '9';
      }
      return lower(str);
    }
  }
  return str;
}


int main(int argc, const char **argv) {
  int cases;
  cin >> cases;
  long long n;
  string str;
  int size;
  int a, b, k, l;
  F1(caseI, cases) {
    cin >> n;
    str = to_string(n);
    size = SZ(str);
    if (isCorrect(n)) {
      cout << "Case #" << caseI << ": " << n << endl;
      continue;
    }
    // Case only one and 0
    if (str[0] == '1') {
      int l = 0;
      while (str[l] == '1') l++;
      if (str[l] == '0') {
        cout << "Case #" << caseI << ": ";
        F0(i, SZ(str) -1) cout << "9";
        cout << endl;
        continue;
      }
    }
    str = lower(str);
    cout << "Case #" << caseI << ": " << str << endl;
  }

  return 0;
}

