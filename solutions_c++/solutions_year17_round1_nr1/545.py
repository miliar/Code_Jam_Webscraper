#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <bitset>
#include <complex>
#include <exception>
#include <initializer_list>
#include <locale>
#include <tuple>
#include <typeinfo>
#include <type_traits>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
const int MAXN = 25, MAXM = 25;
int n_test, n, m;
char a[MAXN + 9][MAXM + 9];

int main() {
    //ifstream cin("a.inp");
    //ofstream cout("a.out");
    std::cin.rdbuf(cin.rdbuf());
    std::cout.rdbuf(cout.rdbuf());
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n_test;
    for(int i_test = 1; i_test <= n_test; i_test++) {
    	cin >> n >> m;
    	for(int i = 1; i <= n; i++) {
    		for(int j = 1; j <= m; j++) {
    			cin >> a[i][j];
    		}
    	}
    	for(int i = 1; i <= n; i++) {
    		for(int j = 2; j <= m; j++) {
    			if(a[i][j] == '?') {
    				a[i][j] = a[i][j - 1];
    			}
    		}
    		for(int j = m - 1; j >= 1; j--) {
    			if(a[i][j] == '?') {
    				a[i][j] = a[i][j + 1];
    			}
    		}
    	}
    	for(int i = 2; i <= n; i++) {
    		if(a[i][1] == '?') {
    			copy(a[i - 1] + 1, a[i - 1] + m + 1, a[i] + 1);
    		}
    	}
    	for(int i = n - 1; i >= 1; i--) {
    		if(a[i][1] == '?') {
    			copy(a[i + 1] + 1, a[i + 1] + m + 1, a[i] + 1);
    		}
    	}
    	cout << "Case #" << i_test << ":\n";
    	for(int i = 1; i <= n; i++) {
    		for(int j = 1; j <= m; j++) {
    			cout << a[i][j];
    		}
    		cout << "\n";
    	}
    }
    return 0;
}
