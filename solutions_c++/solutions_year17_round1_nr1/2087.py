// to compile use: g++ -std=c++11 ...
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <iomanip>  // setfill(), setw() for cout
#include <math.h>   // beware some functions like pow() use floats, not accurate
#include <stdlib.h> // abs
#define REP(x,n) for(int x = 0; x < n; ++x)
#define RAN(x,m,n) for(int x = m; x < n; ++x)
#define LL long long int // -9 * 10^18 ~ 9 * 10^18
#define ULL unsigned long long int // 0 ~ 18 * 10^18

using namespace std;
vector<string> split(string, string);

/******************************************/

char data[25][25];
int R, C;

void process() {
    REP (i, R) {
        char curr = '?';
        REP (j, C) {
            if (data[i][j] != '?') {
                curr = data[i][j];
                break;
            }
        }
        if (curr == '?') continue;
        REP (j, C) {
            if (data[i][j] == '?') data[i][j] = curr;
            else if (data[i][j] == curr) continue;
            else curr = data[i][j];
        }
    }
    REP (j, C) {
        char curr = '?';
        REP (i, R) {
            if (data[i][j] != '?') {
                curr = data[i][j];
                break;
            }
        }
        REP (i, R) {
            if (data[i][j] == '?') data[i][j] = curr;
            else if (data[i][j] == curr) continue;
            else curr = data[i][j];
        }
    }
    REP (i, R) {
        cout << endl;
        REP (j, C) cout << data[i][j];
    }
}

int main() {
    int T;  // number of test cases
    cin >> T;
    
    //getline(cin, s); // to clear the new-line symbol left in cin
    for(int CASE = 1; CASE <= T; ++CASE) {
        cin >> R >> C;
        REP (i, R) REP (j, C) cin >> data[i][j];
                
        cout << "Case #" << CASE << ": ";
        process();
        cout << endl;
    }
    
    return 0;
}

/*

*/

vector<string> split(string s, string delim) {
    vector<string> v;
    char* p;
    char* d = (char*) delim.c_str(); // cast c_str()'s const return type to normal pointer
    p = strtok((char*) s.c_str(), d);
    while (p != NULL) {
        v.push_back(string(p));
        p = strtok(NULL, d);         // strtok() will remember the ending pointer+1,
    }                                // & use it as the starting pointer for the next call
    return v;
}
