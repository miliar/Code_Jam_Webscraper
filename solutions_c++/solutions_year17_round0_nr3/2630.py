#include <fstream>
#include <string>
#include <map>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

int main() {
    
    int t;
    cin >> t;
    for (int j = 0; j < t; ++j) {
        map<long long, long long> m;
        long long n, k;
        cin >> n >> k;
        m[n] = 1;
        while (true) {
            auto it = m.end();
            it--;
            long long f, s;
            f = (*it).first;
            s = (*it).second;
            if (s >= k) {
                cout << "Case #" << j + 1 << ": ";
                cout << f / 2 << ' ' << (f - 1) / 2;
                cout << '\n';
                break;
            }
            else {
                k -= s;
                m[f / 2] += s;
                m[(f - 1) / 2] += s;
                m.erase(it);
            }
        }
    }

    return 0;
}