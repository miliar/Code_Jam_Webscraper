#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        int n, c, m;
        cin >> n >> c >> m;
        vector<int> customer(c, 0), place(n, 0);
        for (int i = 0; i < m; ++i) {
            int p, b;
            cin >> p >> b;
            ++place[p - 1];
            ++customer[b - 1];
        }
        int ride = 0, sum = 0;
        for (int i = 0; i < n; ++i) {
            sum += place[i];
            ride = max(ride, sum / (i + 1) + (sum % (i + 1) > 0));
        }
        ride = max(ride, *max_element(customer.begin(), customer.end()));
        int promo = 0;
        for (int i = 0; i < n; ++i)
            promo += max(place[i] - ride, 0);
        cout << ride << " " << promo << endl;
    }
}