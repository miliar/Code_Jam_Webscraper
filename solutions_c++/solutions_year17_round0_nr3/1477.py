#include <iostream>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;

int main() {
    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        ll N, K;
        cin >> N >> K;

        ll auxi = K, top = N+1, pot = 1, l0 = 1, l1 = 0, nl0, nl1;
        while (auxi > 0) {
            nl0 = 0, nl1 = 0;
            if (l1) {
                auxi -= l1;
                if (auxi <= 0) {
                    top++;
                    break;
                }
                if ((top+1) % 2 == 0) nl1 += 2*l1;
                else {
                    nl0 += l1;
                    nl1 += l1;
                }
            }
            auxi -= l0;
            if (auxi > 0) {
                if (top % 2 == 1) {
                    nl0 += l0;
                    nl1 += l0;
                } else nl0 += l0*2;
                pot *= 2;
                top /= 2;
            }
            l0 = nl0, l1 = nl1;
        }

        printf("Case #%d: ", c);
        ll mid = (top) / 2;
        ll maxi = max(mid, top - mid), mini = min(mid, top - mid);
        printf("%lld %lld\n", maxi-1, mini-1);
    }
    return 0;
}
