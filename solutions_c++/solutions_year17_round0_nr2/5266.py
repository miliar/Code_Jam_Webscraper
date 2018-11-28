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

//#define MY_DEBUG

string solve(string s) {

    REP(jjjj, 18) {
        REP(i, s.length()-1){
            if(s[i] > s[i+1]) {
                s[i] = s[i]-1;
                
                int right = s.length() - ( i + 1 );
                s.replace(i+1, right, string(right, '9'));
                break;
            }
        }
        
        // 先頭が'0'だったら削除.
        if( s[0] == '0') {
            s = s.substr(1, s.length()-1);
        }
    }
 
    return s;
}

#define DIR "/Users/Sugawara/WORK/GCJ2017/GCJ2017/Data/"
#define PROBLEM_NAME "B-large"

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
    
//    std::cin.rdbuf(cinbuf);   //reset to standard input
//    std::cout.rdbuf(coutbuf); //reset to standard output again
    /****************************************************/
    
    int t;
    string s;
    
    cin >> t;
    REP(i, t) {
        cin >> s;
        string result = solve(s);
        cout << "Case #" << (i+1) << ": " << result << endl;
    }
    
    return 0;
}
