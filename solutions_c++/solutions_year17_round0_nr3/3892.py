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



void process1(ULL N, ULL K) {
    vector<ULL> vn{N};
    vector<ULL>::iterator maxI;
    ULL max, l, r;
    while (K > 0) {
        maxI = max_element(vn.begin(), vn.end());
        max = *maxI;
        vn.erase(maxI);
        l = (max + 1) / 2 - 1;
        r = max - l - 1;
        vn.push_back(l);
        vn.push_back(r);
        --K;
    }
    cout << r << ' ' << l;
}

void process(ULL N, ULL K) {
    ULL settled = 1, tmp = 1;
    while (K > settled) {
        tmp *= 2;
        settled += tmp;
    }
    settled -= tmp;
    ULL q, r;
    N -= settled;
    K -= settled;
    q = N / tmp;
    r = N % tmp;
    if (K <= r) ++q;
    ULL L, R;
    L = (q + 1) / 2 - 1;
    R = q - L - 1;
    cout << R << ' ' << L;
}

int main() {
    int T;  // number of test cases
    cin >> T;
    
    //getline(cin, s); // to clear the new-line symbol left in cin
    for(int CASE = 1; CASE <= T; ++CASE) {
        ULL N, K;
        cin >> N >> K;
        
        cout << "Case #" << CASE << ": ";
        process(N, K);
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
