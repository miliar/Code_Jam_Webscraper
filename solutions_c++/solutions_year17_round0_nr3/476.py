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

#define int64 unsigned long long

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
        
        int64 n, k;
        cin >> n >> k;
        int64 x1 = 1;
        while(true) {
             if (x1 - 1 < k && k <= (x1 * 2 - 1)) {
                int64 l = (n - (x1 - 1)) / x1;
                int64 m = (n - (x1 - 1)) % x1;

                if (k <= x1 - 1 + m) {
                    ++l;
                }
                int64 res1 = (l - 1) / 2;
                int64 res2 = (l - 1) / 2 + (l - 1) % 2;
                cout << "Case #" << t << ": " << res2 << ' ' << res1 << endl;
                break;
            }
            x1 *= 2;
        }
    }
    
    
    
    
    
    
    
    
    return 0;
}
