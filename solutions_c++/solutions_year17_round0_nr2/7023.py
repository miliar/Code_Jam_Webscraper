#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;
typedef double ld;

template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }


int main() {
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    //cout.precision(10);
    //cout << fixed;
    
    std::ifstream in("B-large.in");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    std::ofstream out("out.txt");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
	
    int T;
    cin >> T;
    for1(tc, T) {
        cout << "Case #" << tc << ": ";
        long long s;
        cin >> s;
        while(1)
        {
	        long long n = s, factor = 1, no=1;
	        int rem = 0, oldrem = 9, flag=0;
	        //cout<<"check for no."<<n<<endl;
	        while(n>0)
	        {
	 			rem = n%10;
	 			//cout<< rem << "<="<<oldrem;
	 			if (rem <= oldrem)
	 			{
	 				n= n/10;
	 				oldrem = rem;
	 			}
	 			else
	 			{
	 				//cout<<"	"<<no<<endl;
	 				break;
	 			}
	 			if(flag)
	 			{
		 			no = (factor*oldrem) +no;
		 			
	 			}
	 			else
	 			{
				 	flag = 1;
					if(rem)
						no = rem;
				}
				factor *=10;
				//cout<<"	"<<no<<endl;
	        }
	        if(!n)
	        {
	        	cout << s <<'\n';
	        	break;
	        }

	        s=s-no;
    	}
    }

	std::cin.rdbuf(cinbuf);   //reset to standard input again
    std::cout.rdbuf(coutbuf); //reset to standard output again
    
    return 0;
}
