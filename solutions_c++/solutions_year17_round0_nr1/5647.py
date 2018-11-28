#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>

using namespace std;

void flipChar(string& pancakes, int pos) {
   pancakes[pos] = pancakes[pos] == '+' ? '-' : '+';
}

int main() {

   int T, K, N=1, flip=0;
   string S, line, happyState;
   vector<string> lastStates;
   unordered_map<string, int> patternMap;
   size_t found;

   cin >> T;
   cin.ignore();

   while (getline(cin, line)) {
      cout << "Case #" << N << ": ";

      stringstream ss(line);

      ss >> S >> K;
      happyState = string(S.length(), '+');

      if (happyState.compare(S) == 0) {
         cout << "0" << endl;
      } else {
         while ((found = S.find('-'))!= string::npos) {
            if ((found + K - 1) >= S.length()) {
               cout << "IMPOSSIBLE" << endl;
               break;
            } else {
               for (int i=0; i<K; i++) {
                  flipChar(S, found+i);
               }
               flip++;
            }

            if (S.compare(happyState) == 0) {
               cout << flip << endl;
               break;
            }
         }
      }

      N++;
      flip = 0;
   }
   
   return 0;
}