#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        string N;
        cin >> N;
        if (N.length() <= 4 ) {
            int n = stoi(N);
            while (n > 0) {
                int rb = n/1000%10;
                int rt = n/100%10;
                int pl = n/10%10;
                int st = n/1%10;
                if ((rb <= rt) && (rt <= pl) && (pl <= st))
                    break;
                n--;
            }
            printf("Case #%d: %d\n", t, n);
        }
    }
}
