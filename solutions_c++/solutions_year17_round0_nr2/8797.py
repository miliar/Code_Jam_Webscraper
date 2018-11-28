#include <bits/stdc++.h>
#define fr(a, b, c) for(int a = b; a < c; ++a)
#define pb push_back

using namespace std;

bool ok(int n) {
    string str = to_string(n);
    fr(i, 0, str.size()-1) if (str[i] > str[i+1]) return false;
    return true;
}

int main() {
    int n, cas = 0;
    cin >> n;
    while (n--) {
        int val;
        scanf("%d", &val);
        while (!ok(val)) --val;
        printf("Case #%d: %d\n", ++cas, val);
    }
    return 0;
}