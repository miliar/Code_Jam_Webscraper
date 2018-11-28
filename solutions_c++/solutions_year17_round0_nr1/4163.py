#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<bitset>
using namespace std;

ofstream out("tttt");

int n, l;
char a[1010];

void sol() {

    cin >> a >> l;
    n = strlen(a);

    int s = 0, i;

    for(i = 0; i < n - l + 1; ++i) if(a[i] == '-') {
        for(int j = i; j < i + l; ++j)
            a[j] = (a[j] == '+' ? '-' : '+');
        ++s;
    }

    for(; i < n; ++i) if(a[i] == '-') {
        out << "IMPOSSIBLE";
        return;
    }

    out << s;
}

int main() {
    freopen("ttt", "r", stdin);
    //freopen("tttt", "w", stdout);

    int t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        out << "Case #" << a << ": ";
        sol();
		out << "\n";

        printf("Test %d\n", a);
    }

    return 0;
}
