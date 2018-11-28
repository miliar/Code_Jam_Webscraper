/*
Will Long
Google Code Jam 2017
Qualification - Problem 2

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
        string n;
        cin >> n;
        int index = n.length()-1;
        while (index != 0) {
            if (n[index] >= n[index-1]) {
                index--;
                continue;
            }
            else {
                for (int i = index; i < n.length(); i++) {
                    n[i] = '9';
                }
                while(n[--index] == '0') {
                    n[index] = '9';
                }
                n[index]--;
            }
        }
        while(n[index]=='0') {
            index++;
        }
        cout << "Case #" << tc << ": " << n.substr(index, string::npos) << endl;
    }
    return 0;
}
