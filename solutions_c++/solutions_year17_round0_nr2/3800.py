#include <iostream>
#include <vector>

using namespace std;

int first_non_zero(vector<int> a) {

    for (int i = 0; i < a.size(); i++) {
        if (a[i] > 0) return i;
    }
    return a.size();
}

int main() {

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        unsigned long long N, M;
        cin >> N;
        vector<int> a;
        M = N;
        while (M > 0) { a.insert(a.begin(), M % 10); M /= 10; }
        int x;
        bool done = false;
        for (int i = 0; i < a.size() - 1 && !done; i++) {
            if (a[i] > a[i + 1]) {
                x = i;
                done = true;
            }
        }
        cout << "Case #" << t << ": ";
        if (done) {
            int n = a[x];
            while (x > 0 && a[x - 1] == n) x--;
            a[x]--;
            for (int i = x + 1; i < a.size(); i++) a[i] = 9;
            for (int i = first_non_zero(a); i < a.size(); i++) cout << a[i];
        }
        else {
            cout << N;
        }
        cout << "\n";
    }

    return 0;
}
