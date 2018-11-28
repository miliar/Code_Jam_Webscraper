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
        for (int i = 0; i < str.size() - 1; ++i) {
            if (str[i + 1] < str[i]) {
                assert(str[i] != '0');
                --str[i];
                int last = i;
                for (int j = last; j > 0; --j) {
                    if (str[j - 1] > str[j]) {
                        assert(str[j - 1] != '0');
                        --str[j - 1];
                        assert(str[j - 1] <= str[j]);
                        last = j - 1;
                    }
                }
                if (last == 0 && str[0] == '0') {
                    str = string(str.size() - 1, '9');
                }
                else {
                    for (int j = last + 1; j < str.size(); ++j) {
                        str[j] = '9';
                    }
                }
                break;
            }
        }
        cout << "Case #" << t << ": " << str << endl;
        
        
        
    }
    
    
    
    
    
    
    
    
    return 0;
}
