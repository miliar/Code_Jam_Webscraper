#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

using i64 = long long int;

//  . . . . x . . . . .
//  x x x x x x x x x

void calc_rl(i64 n, i64 k, ostream& out) {

    i64 last_mmax = 0;
    i64 last_mmin = 0;
    map<i64, i64, greater<i64>> sample;
    sample[n] = 1;

    //for (i64 i = 0; i < k; ++i) {
//    if (n / k == 1) {
//        out << 0 << " " << 0;
//        return;
//    }
    while (k > 0) {
        auto it = sample.begin();
        auto v = it->first;
        auto mul = it->second;
        k -= mul;
        sample.erase(it);
        i64 mid = v / 2;
        auto a = mid;
        auto b = v - mid - 1;
        sample[a] += mul;
        sample[b] += mul;

        last_mmax = max(a, b);
        last_mmin = min(a, b);
    } 

    out << last_mmax << ' ' << last_mmin;
}

int main(int argc, char* argv[]) {
    int test_num = 0;
    cin >> test_num;
    for (int i = 0; i < test_num; ++i) {
        i64 n = 0;
        i64 k = 0;
        cin >> n >> k;
        cout << "Case #" << i + 1 << ": ";
        calc_rl(n, k, cout);
        cout << endl;
    }
    return 0;
}
