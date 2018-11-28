#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <bitset>

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

const int N = 1000;

//#define MY_DEBUG

int solve(string s, int k) {
    
    const int len = s.length();
    
    // init.
    replace(s.begin(), s.end(), '+', '0');
    replace(s.begin(), s.end(), '-', '1');
    
    // プレート上のホットケーキは、bitsetで表現する.
    bitset<N> bs(s);
    bs.flip();  //  sで初期化しない部分は全て'0'となるため、反転させる.
    
    // ホットケーキ返しも、bitsetで表現.
    string s2(k, '1');
    bitset<N> mask(s2);
    
    int cnt = 0;
    
    // solve.
    REP(i, (len - k + 1)) {
        #ifdef MY_DEBUG
        string sss = bs.to_string();
        sss = sss.substr(0, 10);
        printf("i:%2d : %s\n", i, sss.c_str());
        #endif
        
        // 先頭から検査して、0だったらkビット反転させる.
        if ( !bs.test(i) ) {
            bs = bs ^ mask;
            cnt++;
        }
        // マスクを1ビットシフト.
        mask = mask << 1;
    }
    
    return bs.all() ? cnt : -1;
}

#define DIR "/Users/Sugawara/WORK/GCJ2017/GCJ2017/Data/"
#define PROBLEM_NAME "A-large"

int main() {
    int t;
    string s;
    int k;
    
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
    
    cin >> t;
    
    REP(i, t) {
        cin >> s >> k;
//        cout << s << " " << k << endl;
        
        int rc = solve(s, k);
        
        cout << "Case #" << (i+1) << ": ";
        if(rc >= 0) {
            cout << rc << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    
    return 0;
}
