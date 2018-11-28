#include <iostream>
#include <string>
#include <vector>

using namespace std;

void flip(vector<bool>& v, size_t p, int k) {
  --k;
  while( !(k < 0)) {
    v[p+k] = !v[p+k];
    --k;
  }
}

int solve(vector<bool>& v, int k) {
  int counter = 0;
  for (size_t i = 0; i < v.size() - k + 1; ++i)
    if (!v[i]) { flip(v, i, k); ++counter; }
  for (size_t i = v.size() - k; i < v.size(); ++i)
    if (!v[i]) return -1; // impossible
  return counter;
}

void read(vector<bool>& v, int& k) {
  char c;
  while (true) {
    cin >> c;
    if (c == '+') v.push_back(true);
    else if (c == '-') v.push_back(false);
    else { cin.putback(c); break; }
  }
  cin >> k;
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    int k;
    vector<bool> v;
    v.reserve(1000);
    read(v, k);
    int result = solve(v, k);
    cout << "Case #" << t+1 << ": ";
    if (result == -1)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << result << endl; 
  }
  return 0;
}
