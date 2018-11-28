#include <iostream>
#include <string>
using namespace std;

int main() {
  int tests, curr;
  string form;
  bool found = false;

  cin >> tests;
  //for each test case
  for (int i = 1; i < tests+1; i++) {
    cin >> curr;
    found = false; 
    while (!found) {
      form = to_string(curr);

      found = true;
      auto it2 = form.begin();
      auto it = it2++;
      while(it2 != form.end()) {
        if (*it > *it2) {
          found = false;
          curr--;
          break;
        }
        it++;
        it2++;
      }
    }
    cout << "Case #" << i << ": " << curr << endl;
  }
return 0;
}
