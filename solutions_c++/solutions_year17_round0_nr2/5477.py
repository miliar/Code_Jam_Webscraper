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
        string inp;
        cin >> inp;
        for(int i = 1; i < inp.size(); ++i) {
            if(inp[i] < inp[i - 1]) {
                while(i > 0 && inp[i] < inp[i - 1]) {
                    inp[i] = '9';
                    inp[i - 1] = ((inp[i - 1] - '0') - 1) + '0';
                    i--;
                }
                for(int j = i + 1; j < inp.size(); ++j) inp[j] = '9';
                //cout << "inp: " << inp << '\n';
            }
        }
        stringstream ss(inp);
        long long a;
        ss >> a;
        cout << "Case #" << t << ": " << a << '\n';
    }
}