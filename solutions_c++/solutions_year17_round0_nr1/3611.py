#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;

const static string kProblemSet = "large";

int check(string S, int K) {
    int count = 0;
    for (int i = 0; i < S.length()-K+1; i++) {
        if (S[i] == '-') {
            count++;
            for (int j = 0; j < K; j++) {
                S[i+j] = (S[i+j]=='+')?'-':'+';
            }
        }
    }
    for (int i = S.length()-K; i < S.length(); i++) {
        if (S[i] == '-') {
            return -1;
        }
    }
    return count;
}

int main(int argc, const char * argv[]) {
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );
	int T = 0;
    
	ifs >> T;
    
    for (int testCase = 0; testCase < T; testCase++) {
        string S;
        int K = 0;
        ifs >> S;
        ifs >> K;
        
        int fwd = check(S, K);
        reverse(begin(S), end(S));
        int rev = check(S, K);
        
        fwd = min(fwd, rev);
        
        if (fwd < 0) {
            cout << "Case #" << testCase+1 << ": IMPOSSIBLE" << endl;
            ofs << "Case #" << testCase+1 << ": IMPOSSIBLE" << endl;
        }else {
            cout << "Case #" << testCase+1 << ": " << fwd << endl;
            ofs << "Case #" << testCase+1 << ": " << fwd << endl;
        }
        

    }
    
	return 0;
}
