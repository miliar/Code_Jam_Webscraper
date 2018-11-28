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
#define LL long long int // -9 * 10^18 ~ 9 * 10^18; int: -2 * 10^9 ~ 2 * 10^9
#define ULL unsigned long long int // 0 ~ 18 * 10^18

using namespace std;
vector<string> split(string, string);

/******************************************/

double D;
double K[1000], S[1000];
int N;

void process() {
    double time = 0.0;
    double tmp;
    REP (i, N) {
        tmp = (D - K[i]) / S[i];
        if (tmp > time) time = tmp;
    }
    double rlt = D / time;
    cout << fixed << setprecision(6) << rlt;
}

int main() {
    int T;  // number of test cases
    cin >> T;
    
    //getline(cin, s); // to clear the end-of-line character left in cin
    for(int CASE = 1; CASE <= T; ++CASE) {
        cin >> D >> N;
        REP (i, N) cin >> K[i] >> S[i];
        
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
    char* d = (char*) delim.c_str(); // c_str() returns const type, cast it
    p = strtok((char*) s.c_str(), d);
    while (p != NULL) {
        v.push_back(string(p));
        p = strtok(NULL, d); // strtok() will remember the ending pointer+1, &
    }                        // use it as the starting pointer for the next call
    return v;
}
