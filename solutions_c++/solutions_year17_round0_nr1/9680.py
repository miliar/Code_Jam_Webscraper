#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


int main() {
  int T, K, flips = 0;
  string pencakes;
  bool possible;
  cin >> T;  
  for (int i = 1; i <= T; ++i) {
    cin >> pencakes;
    cin >> K; 
    possible = true;
    flips = 0;
    for (int j = 0; j <= pencakes.length() - K; j++){
      if (pencakes[j] == '-'){
        flips++;
        // cout << pencakes[j] << "\n";
        for (int l = j; l < j+K; l++){
          pencakes[l] = ( pencakes[l] == '+'? '-' : '+' );
        }
        // cout << pencakes << endl;
      }
    }
    for (int j = pencakes.length()-K+1; j < pencakes.length(); j++){
      if (pencakes[j] == '-'){
        possible = false;
        cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        break;
      }
    }
    if (possible)
      cout << "Case #" << i << ": " << flips << endl;
  }
	return 0;
}
