#include "vector"
#include "string"
#include "set"
#include "map"
#include "sstream"
#include "algorithm"
#include "cmath"
#include "cassert"
#include "iostream"
#include "numeric"
#include "fstream"
#include "queue"
#include <functional>
#include <climits>
#include <cstring>
#include <ctime>
#include <list>
#include <iomanip>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <limits>
#include <complex>

#define int64 long long

#include <iostream>

using namespace std;

/*#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>


using namespace __gnu_pbds;

typedef tree<
int,
null_type,
less<int>,
rb_tree_tag,
tree_order_statistics_node_update
> special_tree;
*/

int main(int argc, const char  * argv[]) {
    std::ios::sync_with_stdio(false);
    int T;
    ifstream cin("/Users/artem/ACMGeneral/ACMGeneral/in.txt");
    ofstream cout("/Users/artem/ACMGeneral/ACMGeneral/out.txt");
    cin >> T;
    
    for (int t = 1; t <= T; ++t) {
        string str;
        cin >> str;
        int k;
        cin >> k;
        int res = 0;
        for (int i = 0; i < int(str.size()) - k + 1; ++i) {
            if (str[i] == '-') {
                ++res;
                for (int j = i; j < i + k; ++j) {
                    assert(j < str.size());
                    if (str[j] == '-') {
                        str[j] = '+';
                    }
                    else {
                        str[j] = '-';
                    }
                }
            }
        }
        bool ok = true;
        for (int i = int(str.size()) - k + 1; i < str.size(); ++i) {
            if (str[i] == '-') {
                cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << "Case #" << t << ": " << res << endl;
        }
    }
    
    
    
    
    
    
    
    
    return 0;
}
