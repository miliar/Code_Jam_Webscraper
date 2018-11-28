#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <iterator>

using namespace std;

void completeCake(vector<string> & cake) {

    for (int i = 0; i < cake.size(); i++) {
        char curr_char = '0';
        for (int j = 0; j < cake.front().size(); j++) {
            if (cake[i][j] != '?') {
                curr_char = cake[i][j];
                int k = j - 1;
                while (k >= 0 && cake[i][k] == '?') {
                    cake[i][k] = curr_char;
                    k--;
                }
            }
            else if (curr_char != '0') {
                cake[i][j] = curr_char;
            }
        }
    }

    string curr_string = "0";
    vector<bool> all_q(cake.size());
    for (int i = 0; i < cake.size(); i++) {
        all_q[i] = true;
        for (int j = 0; j < cake.front().size(); j++) {
            if (cake[i][j] != '?') {
                all_q[i] = false;
            }
        }
        if (all_q[i]) {
            if (curr_string != "0") {
                cake[i] = curr_string; 
            }
        }
        else {
            curr_string = cake[i];
            int k = i - 1;
            while (k >= 0 && all_q[k]) {
                cake[k] = curr_string;
                k--;
            }
        }
    }
}

int main() {
    int n;
    cin >> n;
    vector<vector<string> > cakes;
    for (int i = 0; i < n; i++) {
        int r, c;    
        cin >> r >> c;
        vector<string> cake;
        for (int j = 0; j < r; j++) {
            string s;
            cin >> s;
            cake.push_back(s);
        }
        cakes.push_back(cake);
    }

    for (int i = 0; i < n; i++) {
        cout << "Case #" << (i + 1) << ":" << endl;
        completeCake(cakes[i]);
        for (int j = 0; j < cakes[i].size(); j++) {
            cout << cakes[i][j] << endl;
        }
    }
    return 0;
}
