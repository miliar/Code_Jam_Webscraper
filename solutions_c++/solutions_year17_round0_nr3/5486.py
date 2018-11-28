#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <bitset>
#include <vector>

#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

#define INF INT_MAX/3
#define EPS 1e-14
#define ALL(a) (a).begin(),(a).end()
#define SET(a,c) memset((a),(c),sizeof (a))
#define CLR(a) memset((a),0,sizeof (a))

using namespace std;

//#define MY_DEBUG

pair<long, long> solve(long n, long k) {
    
    vector<long> v;
    v.push_back(n);
    
    long l, r;
    REP(i, k) {
        long a = v.back() - 1;
        v.pop_back();
        
        l = a/2;
        r = (a+1)/2;
        
        if(l != 0)
            v.push_back(l);
        
        if(r != 0)
            v.push_back(r);
        
//        sort(v.end(), v.begin());
        sort(v.begin(), v.end());
    }
    
    return pair<long, long>(max(l, r), min(l, r));
}

#define DIR "/Users/Sugawara/WORK/GCJ2017/GCJ2017/Data/"
#define PROBLEM_NAME "C-small-1-attempt0"

int main() {
    /****************************************************/
#ifdef MY_DEBUG
    cout << ">> " << DIR PROBLEM_NAME ".in.txt" << endl;
    cout << "<< " << DIR PROBLEM_NAME ".out.txt" << endl;
#endif
    
    ifstream in(DIR PROBLEM_NAME ".in.txt");
    streambuf *cinbuf = cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect cin to in.txt!
    
    ofstream out(DIR PROBLEM_NAME ".out.txt");
    streambuf *coutbuf = cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf()); //redirect cout to out.txt!
    
//    std::cin.rdbuf(cinbuf);   //reset to standard input again
//    std::cout.rdbuf(coutbuf); //reset to standard output again
    /****************************************************/
    
    long t;
    cin >> t;
    
    REP(i, t) {
        long n, k;
        cin >> n >> k;
        
        pair<long, long> result = solve(n, k);
        cout << "Case #" << (i+1) << ": " << result.first << " " << result.second << endl;
    }
    
    return 0;
}
