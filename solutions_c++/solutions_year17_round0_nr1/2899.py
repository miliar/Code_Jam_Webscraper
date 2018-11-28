//
// Created by andy on 3/18/17.
//

#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    int T;
    cin >> T;


    for (int i = 0; i < T; i++) {
        string s;
        int k;
        cin >> s >> k;
        vector<int> m(s.length());

        int flips = 0;
        for (int j = 0; j <= int(s.length()) - k; j++) {
            if ((m[j] % 2) != (s[j] == '-')) {
                flips++;
                for (int l = j; l < j + k; l++) {
                    m[l]++;
                }
            }

           // cout << "pos " << j << endl;
          //  for (int l = 0; l < s.length(); l++) {
          //      cout << m[l];
          //  }
         //   cout << endl;
        }

        bool success = true;
        for (int j = int(s.length()) - k; j < s.length(); j++) {
            if ((m[j] % 2) != (s[j] == '-')) {
                success = false;
                break;
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (success)
            cout << flips << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}