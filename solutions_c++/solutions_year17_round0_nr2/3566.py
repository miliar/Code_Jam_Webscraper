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

string run(string N) {
    if (N.length() == 1) {
        return N;
    }
   
    while(1) {
        bool f = false;
        char last = N[0];
        for (int i = 1; i < N.length(); i++) {
            if (!f && last > N[i]) {
                N[i-1] = N[i-1]-1;
                N[i] = '9';
                f = true;
            }else if (f) {
                N[i] = '9';
            }
            last = N[i];
            if (i == N.length()-1 && !f) {
                return N;
            }
        }
    }
    return "";
}

int main(int argc, const char * argv[]) {
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );
	int T = 0;
    
	ifs >> T;
    
    for (int testCase = 0; testCase < T; testCase++) {
        string N;
        ifs >> N;
        
        unsigned long long M = stoull(run(N));
        cout << "Case #" << testCase+1 << ": " << M << endl;
        ofs << "Case #" << testCase+1 << ": " << M << endl;
    }
    
	return 0;
}
