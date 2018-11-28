#include <iostream>
#include <vector>

using namespace std;

void add_nines(vector<int>& n, int i) {
  while (i < n.size() && n[i] != 9) {
    n[i] = 9;
    i++;
  }
}

vector<int> solve(vector<int> n) {
  if (n.size() == 1) {
    return n;
  }

  int i = n.size() - 1;

  while(i > 0) {
    if (n[i] < n[i - 1]) {
      n[i - 1] -= 1;
      add_nines(n, i);
    }
    i--;
  }

  if (n[0] == 0) {
    n.erase(n.begin());
  }

  return n;
}

int main() {
  int t;

  cin >> t;

  for (int a = 0; a < t; a++) {
    string n;

    cin >> n;

    vector<int> digits;

    for (int i = 0; i < n.size(); i++) {
      digits.push_back(n[i] - '0');
    }

    vector<int> solution = solve(digits);

    cout << "Case #" << a + 1 << ": ";
    for (int i = 0; i < solution.size(); i++) {
      cout << solution[i];
    }
    cout << endl;
  }

  return 0;
}