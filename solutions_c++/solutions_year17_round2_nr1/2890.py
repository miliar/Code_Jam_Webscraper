#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t = 0;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        long double d = 0;
        int n = 0;
        cin >> d >> n;
        vector<long double> k(n, 0);
        vector<long double> s(n, 0);
        long double max_t = 0;
        for (int j = 0; j < n; ++j) {
            cin >> k[j] >> s[j];
            long double len = d - k[j];
            if (len/s[j] > max_t) {
                max_t = len/s[j];
            }
        }
        cout << std::fixed << "Case #" << i + 1 << ": " << d/max_t << endl;
    }
	return 0;
}