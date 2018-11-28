#include<iostream>
#include<string>
using namespace std;

int last_tidy(int n) {
  int trail = n/10;
  if (trail == 0) return n;
  int last = n%10;
  int tidy_trail = last_tidy(trail);
  if (tidy_trail != trail) return tidy_trail*10 + 9;
  
}

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    string N;
    cin >> N;
    int last_ascending = 0, first_descending = 1;
    bool found = false;
    while (not found and first_descending < N.size()) {
      if (N[first_descending - 1] < N[first_descending]) {
        last_ascending = first_descending;
        ++first_descending;
      }
      else if (N[first_descending - 1] == N[first_descending]) ++first_descending;
      else found = true;
    }
    if (first_descending < N.size()) {
      N[last_ascending] -= 1;
      for (int i = last_ascending + 1; i < N.size(); ++i) {
        N[i] = '9';
      }
    }
    N.erase(0, N.find_first_not_of("0"));
    cout << "Case #" << cas << ": " << N << endl;
  }
}
