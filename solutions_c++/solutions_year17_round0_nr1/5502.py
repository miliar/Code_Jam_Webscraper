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

using namespace std;

int main() {
    int cases;
    std::ios::sync_with_stdio(false);
    scanf("%d", &cases);
    for(int t = 1; t <= cases; ++t) {
        string inp;
        int k;
        cin >> inp >> k;
        int a = 0;
        bool flag = false;
        for(int i = 0; i < inp.size(); ++i) {
            flag = false;
            if(inp[i] == '-') {
                for(int j = i; j < i + k && i + k <= inp.size(); ++j) {
                    if(flag == false) {
                        a++;
                        flag = true;
                    }
                    inp[j] = (inp[j] == '-') ? '+' : '-';
                }
            }
            //cout << "INP: " << inp << '\n';
        }
        bool answer = true;
        for(int i = 0; i < inp.size(); ++i) {
            if(inp[i] == '-') answer = false;
        }
        if(answer == true) {
            cout << "Case #" << t <<": " << a << '\n';
        } else {
            cout << "Case #" << t << ": IMPOSSIBLE\n";
        }
    }
}