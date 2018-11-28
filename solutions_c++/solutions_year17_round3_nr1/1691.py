

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


int main(int argc, const char * argv[]) {
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );
	int T = 0;
    
	ifs >> T;
    
    for (int testCase = 0; testCase < T; testCase++) {
        int N, K;
        ifs >> N >> K;
        vector<double> Hs;
        vector<double> Rs;
        for (int i = 0; i < N; i++) {
            int R, H;
            ifs >> R >> H;
            Hs.push_back(H);
            Rs.push_back(R);
        }
        
        vector<size_t> ridx(Rs.size());
        iota(ridx.begin(), ridx.end(), 0);
        
        sort(ridx.begin(), ridx.end(),
             [&Rs, &Hs](size_t i1, size_t i2) {
                 if (Rs[i1] == Rs[i2]) return Hs[i1] < Hs[i2];
                 return Rs[i1] < Rs[i2];});
        
        vector<double> cumH(N);
        for (int i = 0; i < N; i++) {
            auto idx = ridx[i];
            if (i+1 < K) cumH[idx] = 0.0;
            else {
                vector<double> tmp;
                for (int j = 0; j < i; j++) {
                    tmp.push_back(2.0*Hs[ridx[j]]*Rs[ridx[j]]);
                }
                sort(tmp.begin(), tmp.end());
                double c = 0.0;
                
                for (int j = 0; j < K-1; j++) {
                    c += tmp[tmp.size()-1-j];
                }
                
                cumH[idx] = c+1.0*Rs[idx]*Rs[idx]+2.0*Rs[idx]*Hs[idx];
            }
        }
        
        sort(cumH.begin(), cumH.end());
        
        cout << "Case #" << testCase+1 << ": " << fixed << setprecision(9) << cumH[cumH.size()-1]*M_PI << endl;
        ofs << "Case #" << testCase+1 << ": " << fixed << setprecision(9) << cumH[cumH.size()-1]*M_PI << endl;
    }
    
	return 0;
}
