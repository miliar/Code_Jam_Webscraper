#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n,count,done;
  string pancakes;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> pancakes >> n;  // read pancakes and then pancake_rotater size.
    done = 1;
    count = 0;
    for(int j = 0; j <= pancakes.length()-n; j++) {
        if (pancakes[j] == '-') {
            count++;
            for(int k = 0;k<n;k++) {
                pancakes[j+k] = pancakes[j+k]=='-'?'+':'-';
            }            
        }
    }
    for(int k = 1; k <= n ; k++) {
        if (pancakes[pancakes.length()-k] == '-') {
            done = 0;
            break;            
        }
    }
    if (done == 1) {
        cout << "Case #" << i << ": " << count << endl;
    } else {
        cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    }
   }
  return 0;
}