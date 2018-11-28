#include <iostream>
#include <cstring>
using namespace std;

void go() {
    long long n, k;
    cin >> n >> k;
    long long cur1 = n, cur2 = n;
    long long count1 = 1, count2 = 0;
    long long sofar = 0;
    long long ans;
    while (sofar < k) {
        if (sofar + count1 >= k) {
            ans = cur1;
            break;
        } else if (sofar + count1 + count2 >= k) {
            ans = cur2;
            break;
        }
        sofar += count1 + count2;
        long long ncur1 = cur1 / 2;
        long long ncount1 = count1;
        long long ncur2 = cur1 / 2 - 1;
        long long ncount2 = 0;
        if ((cur1-1)/2 == ncur1) {
            ncount1 += count1;
        } else {
            ncount2 += count1;
        }
        if (cur2 / 2 == ncur1) {
            ncount1 += count2;
        } else {
            ncount2 += count2;
        }
        if ((cur2-1) / 2 == ncur1) {
            ncount1 += count2;
        } else {
            ncount2 += count2;
        }
        cur1 = ncur1;
        count1 = ncount1;
        cur2 = ncur2;
        count2 = ncount2;
    }
    cout << ans/2 << ' ' << (ans-1)/2;
}

int main() {
    int testn;
    cin >> testn;
    for (int testi = 0; testi < testn; testi++) {
        cout << "Case #" << testi+1 << ": ";
        go();
        cout << '\n';
    }
}
