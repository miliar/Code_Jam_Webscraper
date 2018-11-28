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
int Count(vector<vector<char>> &data) {
    int n = int(data.size());
    int res = 0;
    for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) {
        if (data[i][j] == 'o') res += 2;
        if (data[i][j] == 'x' || data[i][j] == '+') res += 1;
    }
    return res;
}

int main(int argc, const char  * argv[]) {
    std::ios::sync_with_stdio(false);
    int T;
    ifstream cin("/Users/artem/ACMGeneral/ACMGeneral/in.txt");
    ofstream cout("/Users/artem/ACMGeneral/ACMGeneral/out.txt");
    cin >> T;
    
    for (int t = 1; t <= T; ++t) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> data(n, vector<char>(n, '.'));
        for (int i = 0; i < m; ++i) {
            char c;
            int v1, v2;
            cin >> c >> v1 >> v2;
            --v1;
            --v2;
            assert(v1 == 0);
            data[v1][v2] = c;
        }
        vector<vector<char>> orig = data;
        int oCol = -1;
        for (int i = 0; i < n; ++i) {
            if (data[0][i] == '.') {
                data[0][i] = '+';
            }
            if (data[0][i] == 'o') {
                oCol = i;
            }
            if (data[0][i] == 'x') {
                data[0][i] = 'o';
                oCol = i;
            }
        }
        if (oCol == -1) {
            data[0][0] = 'o';
            oCol = 0;
        }
        int oCol2  = n - 2;
        if (oCol2 == oCol) --oCol2;
        oCol2 = -1;
        
        for (int i = n - 1; i >= 1; --i) {
            if (i == oCol) break;
            if (i != oCol2)
                data[i][i] = 'x';
        }
        int i = 1;
        int j = oCol - 1;
        while (true) {
            if (j < 0) break;
            if (i >= n) break;
            
            if (j != oCol2)
                data[i][j] = 'x';
            ++i;
            --j;
        }
        for (int i = n - 2; i > 0;  --i) {
            if (i != oCol2)
                data[n - 1][i] = '+';
            else
                data[n - 1][i] = 'o';
        }
        
        
        vector<int> v1, v2;
        vector<char> c;
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) {
            if (data[i][j] != orig[i][j]) {
                v1.push_back(i + 1);
                v2.push_back(j + 1);
                c.push_back(data[i][j]);
            }
        }
        
        cout << "Case #" << t << ": " << Count(data) << ' ' << v1.size() << endl;
        for (int i = 0; i < v1.size(); ++i) {
            cout << c[i] << ' ' << v1[i] << ' ' << v2[i] << endl;
        }
        //for (int i = 0; i < n; ++i) {
        //    cout << string(data[i].begin(), data[i].end()) << endl;
        //}
    }
    
    
    
    
    
    
    
    
    return 0;
}
