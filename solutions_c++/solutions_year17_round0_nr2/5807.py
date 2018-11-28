#include <iostream>
#include <cstdio>

using namespace std;


unsigned long long a;

void read() {

    scanf("%lld", &a);

}

bool isTidy(unsigned long long b) {
    int prev = b % 10;
    while(b != 0) {
        //cout << "Comparing  "<< b % 10 << " > " << prev << b << endl;
        if((b % 10) > prev) {
            return false;
        }
        prev = (b % 10);
        b /= 10;
    }
    return true;
}

void solve(int c) {

    for(unsigned long long i = a; i >= 0; i--) {
        if(isTidy(i)) {
            printf("Case #%d: %lld\n", c, i);
            return;
        }
    }

}

int main() {
    int t;
    scanf("%d", &t);
    for(int tt = 0; tt < t; tt++) {
        read();
        solve(tt + 1);
    }

}
