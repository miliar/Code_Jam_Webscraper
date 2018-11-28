#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <utility>
#include <string>

using namespace std;

typedef long long lint;

int main() {
    int t;
    scanf("%d", &t);
    int n, k;
    string state;
    for(int CASE = 1; CASE <= t; CASE++) {
        cin>>state>>k;
        n = state.length();
        int z = 0, flip = 0;
        for(int i = 0; i < n-k+1; i++) {
            if(state[i] == '-') {
                for(int j = i; j < i+k; j++)
                    state[j] = (state[j] == '-')?'+':'-';
                flip++;
            }
        }
        if(state.find("-") == std::string::npos)
            printf("Case #%d: %d\n", CASE, flip);
        else
            printf("Case #%d: IMPOSSIBLE\n", CASE);
    }
    return 0;
}