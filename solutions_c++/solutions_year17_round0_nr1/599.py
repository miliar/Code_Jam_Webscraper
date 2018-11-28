/*
Will Long
Google Code Jam 2017
Qualification - Problem 1

April 7, 2017
*/

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <deque>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, const char *argv[])
{
    string fname = argv[1];
    freopen((fname+".in").c_str(), "r", stdin);
    freopen((fname+".out").c_str(), "w", stdout);

    int num_cases;
    cin >> num_cases;

    for (int tc = 1; tc <= num_cases; tc++) {
        string pancakes;
        int k;
        cin >> pancakes >> k;
        // determine number of flips
        int flips = 0;
        for (int i = 0; i <= pancakes.length()-k; i++) {
            if (pancakes[i] == '+') {
                continue;
            }
            flips++;
            for (int j = i; j < i + k; j++) {
                pancakes[j] = pancakes[j] == '-' ? '+' : '-';
            }
        }
        // check if worked
        bool is_possible = true;
        for (int i = pancakes.length()-k+1; i < pancakes.length(); i++) {
            if (pancakes[i] == '-') {
                is_possible = false;
                break;
            }
        }
        if (!is_possible) {
            cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
        }
        else {
            cout << "Case #" << tc << ": " << flips << endl;
        }
    }
    return 0;
}
