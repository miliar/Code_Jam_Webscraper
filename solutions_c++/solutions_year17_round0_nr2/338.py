
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int64_t solve() {
    int64_t n;
    cin >> n;

    vector <int> dig;
    int64_t m = n;
    while (m > 0)
        dig.push_back(m % 10), m /= 10;
    reverse(dig.begin(), dig.end());

    for (int i = 1; i < dig.size(); i++) {
        if (dig[i - 1] <= dig[i])
            continue;
        int j = i - 1;
        while (j > 0 && dig[j - 1] == dig[j])
            j--;
        dig[j]--;
        j++;
        while (j < dig.size())
            dig[j] = 9, j++;

        int64_t r = 0;
        for (j = 0; j < dig.size(); j++)
            r = 10 * r + dig[j];
        return r;
    }
    return n;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " << solve() << endl;
    }
}
