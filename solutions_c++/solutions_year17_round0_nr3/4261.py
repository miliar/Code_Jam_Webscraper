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

multiset<long long> s;

void sol() {
    long long n, k;

    cin >> n >> k;

    s.clear();
    s.insert(n);

    while(--k) {
        int l = (*s.rbegin());
        s.erase(s.find(l));

        s.insert(l / 2);
        s.insert(l - l / 2 - 1);
    }

    int l = *s.rbegin();
    out << l / 2 << " " << l - l / 2 - 1;
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
