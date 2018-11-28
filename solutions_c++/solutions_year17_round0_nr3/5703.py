#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <climits>
#include <algorithm>
#include <queue>
#include <set>
#include <sstream>

using namespace std;

int main() {
    int cases;
    std::ios::sync_with_stdio(false);
    scanf("%d", &cases);
    for(int t = 1; t <= cases; ++t) {
        int n, k;
        cin >> n >> k;
        string inp = "O";
        for(int i = 0; i < n; ++i) inp += '.';
        inp += "O";
        int a[2];
        for(int i = 0; i < k; ++i) {
            int len = 0, prev = -1, ret = 0;
            pair <int, int> p;
            for(int j = 0; j < inp.size(); ++j) {
                if(inp[j] == 'O' && prev == -1) {
                    prev = j;
                } else if(inp[j] == 'O') {
                    len = j - prev - 1;
                    if(len > ret) {
                        p.first = prev;
                        p.second = j;
                        ret = len;
                    }
                    prev = j;
                }
            }
            inp[p.first + ((ret + 1) / 2)] = 'O';
            int index = p.first + ((ret + 1) / 2);
            a[0] = index - p.first - 1;
            a[1] = p.second - index - 1;
        }
        sort(a, a + 2);
        cout << "Case #" << t << ": " << a[1] << ' ' << a[0] << '\n';
    }
}