#include <iostream>
#include <map>
#include <iterator>
#include <queue>
#include <set>
#include <stack>
#include <iomanip>
#include <math.h>
#include <unordered_map>
#include <sstream>
#include <fstream>

using namespace std;

int main() {
    ifstream cin("/Users/shicheng/Downloads/C-small-2-attempt0.in.txt");
    ofstream cout("/Users/shicheng/Downloads/C-small-2-attempt0.out.txt");
    int t;
    cin >> t;
    for (int num = 0; num < t; ++num) {
        int n, k;
        cin >> n >> k;
        map<int, int, greater<int>> m;
        map<int, int, greater<int>>::iterator iter;
        m[n] = 1;
        --k;
        while (k) {
            iter = m.begin();
            int max_free = iter->first;
            if (iter->second == 1) {
                m.erase(iter);
            }
            else {
                --iter->second;
            }
            if (max_free / 2) {
                ++m[max_free / 2];
            }
            if (max_free - max_free / 2 - 1) {
                ++m[max_free - max_free / 2 - 1];
            }
            --k;
        }
        int max_free = m.begin()->first;
        if (max_free % 2 == 0) {
            cout << "Case #" << num + 1 << ": " << max_free / 2 << " " << max_free / 2 - 1 << endl;
        }
        else {
            cout << "Case #" << num + 1 << ": " << max_free / 2 << " " << max_free / 2 << endl;
        }
    }
}
