#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

#define DEBUG false

string s;
int k;
int n;

short a[1020];

void read() {
    cin >> s >> k;
    n = s.size();
    for(int i = 0; i < n; i++) {
        if(s[i] == '+') {
            a[i] = 1;
        } else {
            a[i] = 0;
        }
    }
}

void solve(int tes) {

    int l = 0;
    int r = s.size() - 1;

    int counts = 0;

    while(l <= r) {
        DEBUG && printf("%d %d %d\n", l, r, k);
        if(a[l]) {
            l++;
            continue;
        }
        if(a[r]){
            r--;
            continue;
        }
        if(l + k - 1 > r) {
            printf("Case #%d: IMPOSSIBLE\n", tes);
            return;
        }
        int st = l;
        for(int i = l; i < st + k; i++) {
            DEBUG && printf("Flipping %d - %d\n", i, a[i] ^ 1);
            a[i] ^= 1;
            if(a[l])
                l++;
        }
        counts++;
    }
    printf("Case #%d: %d\n", tes, counts);



}

int main() {
    int t;
    scanf("%d", &t);
    for(int tt = 0; tt < t; tt++) {
        read();
        solve(tt + 1);
    }
}
