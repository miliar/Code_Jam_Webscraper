//                                                  In The Name Of God
//                                              programmer:Mohammad Dehghan
#include <iostream>
using namespace std;

#include <vector>
#include <set>
#include <string>
#include <string.h>
#include <math.h>
#include <map>
#include <iomanip>
#include <queue>
#include <algorithm>
#include <sstream>

typedef long long ll;
typedef unsigned long long ull;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<vii> vvii;
typedef vector<vvii> vvvii;
typedef vector<vector<viii>> vvviii;
typedef vector<vector<iii>> vviii;
typedef set<int> si;
typedef vector<si> vsi;
typedef pair<double, double> dd;
typedef vector<dd> vdd;

#define inf 1000000000
#define eps 1e-9

//
//bool check(string s){
//    for (int i = 0; i < s.size()-1; ++i) {
//        if(s[i]>s[i+1])
//            return 0;
//    }
//    return 1;
//}

int main() {
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; ++i) {
        string s;
        cin >> s;
        for (int j = 0; j < s.size() - 1; ++j) {
            if (s[j] > s[j + 1]) {
                s[j]--;
                int index = j + 1;
                for (int k = j; k > 0; --k) {
                    if (s[k] < s[k - 1]) {
                        s[k - 1] = s[k];
                        index = k;
                    }
                }
                for (int l = index; l < s.size(); ++l) {
                    s[l] = '9';
                }
                break;
            }

        }

//    int a;
//    cin >> a;
//    string s = to_string(a);
//    for(;!check(s); ){
//        a--;
//        s= to_string(a);
//    }
//    cout << s;
        if (s[0] == '0') {
            cout << "Case #"<<i<<": ";
            for (int m = 1; m < s.size(); ++m) {
                cout << s[m];

            }
            cout << endl;
        } else
            cout << "Case #"<<i<<": "<< s << endl;
    }
}

