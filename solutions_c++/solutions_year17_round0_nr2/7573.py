#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
using namespace std;
bool solve(char buff[]) {
    int idx = 1;
    while(buff[idx] && buff[idx] >= buff[idx - 1])
        idx++;
    if(buff[idx]) {
        --buff[idx - 1];
        while(buff[idx])
            buff[idx++] = '9';
        return true;
    }
    return false;
}
int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        char buff[20];

        scanf("%s", buff);
        while(solve(buff));

        printf("Case #%d: %s\n", t, (buff[0] == '0' ? (buff + 1) : buff));
    }
    return 0;
}
