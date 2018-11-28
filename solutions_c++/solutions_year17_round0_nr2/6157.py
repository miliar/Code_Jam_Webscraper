#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <unordered_map>
#include <map>
#include <vector>
#include <unordered_set>
#include <set>


using namespace std;

int t;
string n;

int main() {
  cin.sync_with_stdio(0);
  cin >> t;
  for (int test_case = 1; test_case <= t; test_case++) {
    cin >> n;
    reverse(n.begin(), n.end());
    for (int i = 0; i < n.size()-1; i++) {
      if (n[i] < n[i+1]) {
        for (int j = i; j >= 0; j--) {
          n[j] = '9';
        }
        n[i+1]--;
      }
    }
    if (n.back() <= '0') {
      n.pop_back();
      for (int i = 0; i < n.size(); i++) {
        n[i] = '9';
      }
    }
    reverse(n.begin(), n.end());
    cout << "Case " << "#" << test_case << ": ";
    cout << n;
    cout << "\n";
  }
}
