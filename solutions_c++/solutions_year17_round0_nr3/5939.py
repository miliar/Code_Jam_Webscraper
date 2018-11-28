#include<bits/stdc++.h>

using namespace std;

int main() {
  int t, tc = 0; scanf("%d", &t);

  while(t--) {
    int n, k, a, b;
    cin >> n >> k;

    vector<int> V;
    V.push_back(n);

    while(k--) {
      sort(V.rbegin(), V.rend());
      int x = V[0];
      V.erase(V.begin());
      if(x % 2 == 0) {
	a = x / 2; b = (x / 2) - 1;
	V.push_back(a);
	V.push_back(b);
      } else {
	a = x / 2; b = x / 2;
	V.push_back(a);
	V.push_back(b);
      }

      //cout << a << " " << b << endl;
    }

    printf("Case #%d: %d %d\n", ++tc, a, b);
  }

  return 0;
}
