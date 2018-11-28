#include <iostream>
#include <string>
using namespace std;
int main() {
  int tests, flips, required;
  string pancakes;
  cin >> tests; //retrieves num tests
  for (int i = 1; i < tests+1; i++) {
    //for each test
    cin >> pancakes;
    cin >> flips;
    
    int count = 0;
    required = 0;
    int max = pancakes.size();
    auto it = pancakes.begin();    
    while (it != pancakes.end()) {
      if (*it == '-') {
        //if need to flip but can't anymore, IMPOSSIBLE
        if ((count + flips) > max) {
          cout << "Case #" << i << ": IMPOSSIBLE" << endl;
          break;
        }
        //if need to flip and CAN,
        //flip all - to + in flip range
        //increment count
        //increment it2 flip times, but it only ONCE
        //because second char could require flipping again
        else {
            auto it2 = it;
          for (int j = 0; j < flips; j++) {
            if (*it2 == '-') { 
              *it2 = '+';
            }
            else { 
              *it2 = '-'; 
            }
            it2++;
          }
          required++;
        }
      }
      //if we encounter +, simply move to next
        it++;
        count++;
    }
    if (it == pancakes.end()) {
    cout << "Case #" << i << ": " << required << endl;
    }
 }

return 0;
}
