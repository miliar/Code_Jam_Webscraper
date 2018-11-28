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


void process(string s) {
    int l = s.length();
    int i1 = 0, i2 = 1;
    for (; i2 < l;) {
        if (s[i1] < s[i2]) {++i1; ++i2;}
        else if (s[i1] == s[i2]) ++i2;
        else break;
    }
    if (i2 < l) {
        s[i1] -= 1;
        RAN (i, i1 + 1, l) s[i] = '9';
    }
    s.erase(0, s.find_first_not_of('0'));
    cout << s;
}

int main() {
    int T;  // number of test cases
    cin >> T;
    
    //getline(cin, s); // to clear the new-line symbol left in cin
    for(int CASE = 1; CASE <= T; ++CASE) {
        string s;
        cin >> s;
        cout << "Case #" << CASE << ": ";
        process(s);
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
