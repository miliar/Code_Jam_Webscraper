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

typedef unsigned long long ull;

const static string kProblemSet = "small2";


int main(int argc, const char * argv[]) {
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );
	int T = 0;
    
	ifs >> T;
    
    for (int testCase = 0; testCase < T; testCase++) {
        ull N, K;
        ifs >> N >> K;
        
        int m = floor(log2(K-1));
        ull al = (1ULL << m) - 1;
        
        multiset<ull> st;
        
        
        ull a = (N-al)/(al+1);
        ull b = (N-al)%(al+1);
        for (ull i = 0; i < al+1; i++) {
            if (i < b) {
                st.insert(a+1);
            }else {
                st.insert(a);
            }
        }
        
        K = K - al;
        for (ull i = 0; i < K-1; i++) {
            auto e = st.end();
            ull largest = *(--e);
            st.erase(e);
            if (largest%2 == 0) {
                st.insert(largest/2-1);
                st.insert(largest/2);
            }else {
                st.insert((largest-1)/2);
                st.insert((largest-1)/2);
            }
        }
        auto e = st.end();
        ull largest = *(--e);
        ull mi, ma;
        if (largest%2 == 0) {
            mi = (largest/2-1);
            ma = (largest/2);
        }else {
            mi = ma = (largest-1)/2;
        }
        cout << "Case #" << testCase+1 << ": " << ma << " " << mi << endl;
        ofs << "Case #" << testCase+1 << ": " << ma << " " << mi << endl;
    }
    
	return 0;
}
