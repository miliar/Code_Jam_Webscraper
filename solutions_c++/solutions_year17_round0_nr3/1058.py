#include <iostream>
#include <map>
using namespace std;

int nrt;
long long n, k;
map< long long, long long, greater<long long> > m;

int main() {

    cin >> nrt;
    for(int t = 1; t <= nrt; ++t) {
        cin >> n >> k;
        m.clear();
        m[n] = 1;

        while(1) {
            pair<long long, long long> x = *m.begin();
            m.erase(m.begin());

            long long a = (x.first - 1) / 2;
            long long b = x.first - 1 - a;

            if(a > 0)
                m[a] += x.second;
            if(b > 0)
                m[b] += x.second;

            if(x.second < k)
                k -= x.second;
            else {
                cout << "Case #" << t << ": " << max(a, b) << " " << min(a, b) << "\n";
                break;
            }
        }
    }

    return 0;
}