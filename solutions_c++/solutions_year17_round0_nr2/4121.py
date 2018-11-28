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

bool v(long long n) {
    int last = 10;
    while(n) {
        if(n % 10 > last)
            return 0;
        last = n % 10;
        n /= 10;
    }
    return 1;
}

void sol() {
    long long n;

    cin >> n;

    while(!v(n)) {

        long long z = n, p10 = 1;

        int last = 10;
        while(z) {
            if(z % 10 > last) {
                break;
            }
            last = z % 10;
            z /= 10;
            p10 *= 10;
        }

        p10 /= 10;
        while(p10 != 1 && (n / p10) % 10 == 0)
            p10 /= 10;

        n -= p10;
    }

    out << n;
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
