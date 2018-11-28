#include <string>
#include <iostream>
#include <fstream>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;
void problem() {
  ull n, k;
  cin >> n >> k;


  if (n % 2 == 1) {

  }
  ull l, r;

  ull mx = n/2 + 1;
  vector<ull> v(mx);
  if (k > 1) {

    v[n >> 1] += 1;
    v[(n >> 1) - (n % 2 ? 0 : 1)] += 1;
    k--;
    int i = n >> 1;
    while (k > 0) {

      while(v[i] == 0)
        i--;
      if (i < 1) {
        l = 0;
        r = 0;
        break;
      }
      v[i]--;
      l =  i >> 1;
      r = (i >> 1) - (i % 2 ? 0 : 1);
      v[l]++;
      v[r]++;

      k--;
      //cout << k << endl;
    }
  } else {
    l = n >> 1;
    r = (n >> 1) - (n % 2 ? 0 : 1);
  }
  cout << l << " " << r << endl;

}

//void problem() {
//  ull n, k;
//  cin >> n >> k;
//
//}
int main() {
  ifstream in("../in");
  cin.rdbuf(in.rdbuf());


  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cout << "Case #" << i +1  << ": ";
    problem();
  }

  return 0;
}