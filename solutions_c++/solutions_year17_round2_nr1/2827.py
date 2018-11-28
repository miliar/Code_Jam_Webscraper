#include <cstdio>
#include <set>
#include <stack>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <climits>

using namespace std;

typedef long long ll;

typedef pair<int, int> pii;

template <typename A> void print(A x) {
    cout << x << endl;
}

template <typename A, typename B> void print(A x, B y) {
    cout << x << " " <<  y << endl;
}

template <typename A, typename B, typename C> void print(A x, B y, C z) {
    cout << x << " " <<  y << " " << z << endl;
}

template <typename A> void print(vector<A> v) {
    cout << v.size() << ": ";
    for (auto x : v) {
        cout << x << " ";
    }
    cout << endl;
}

template <typename B, typename A> void print(A first, vector<A> v) {
  cout << first << " " << v.size() << ": ";
  for (auto x : v) {
    cout << x << " ";
  }
  cout << endl;
}

#define loop(x,a,b) for(int x = a; x < b; ++x)

#define ALL(x) x.begin(), x.end()

int T;
double D;

double max(double u, double v) {
  if (u >= v) {return u;} else {return v;}
}

int main(int nargs, char **argv) {
    std::ios::sync_with_stdio(false);
    cin >> T;
    loop(i,0,T) {
      int N;
      cin >> D;
      cin >> N;
      double time_last = 0;
      loop(j,0,N) {
        double K, S;
        cin >> K >> S;
        time_last = max(time_last, (D - K) / S);
      }
      double res = D / time_last;
      cout << "Case #" << (i+1) << ": ";
      printf("%f\n", res);
    }

    return 0;
}

