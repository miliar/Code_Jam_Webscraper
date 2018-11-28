#include <bits/stdc++.h>
#define M_PI 3.141592653589793238462643383279502884197

using namespace std;
typedef long long ll;

struct classcmp {
    operator () (pair<int, int> a, pair<int, int> b) {
        return (a.first > b.first || a.first == b.first && a.second > b.second);
    }
};

int main(int argc, char* argv[])
{
#ifdef DEBUG
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
#endif // DEBUG
    std::ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        int K, N;
        ll max = 0;
        multiset<pair<ll, ll>, classcmp > A;
        cin >> N >> K;
        for(int j = 0; j < N; j++) {
            ll r, h;
            cin >> r >> h;
            A.insert(make_pair(r, h));
        }
        vector<pair<ll, ll> > b (A.begin(), A.end());

        ll area = b[0].first * b[0].first + b[0].first * b[0].second * 2;
        multiset<ll> c;
        for(int j = 1; j < b.size(); j++) {
            ll ar = b[j].second * b[j].first * 2;
            c.insert(ar);
        }
        multiset<ll>::reverse_iterator it = c.rbegin();
        for(int j = 0; j < K - 1; j++) {
            area += *it;
            it++;
        }
        if(area > max) {
            max = area;
        }
        for(int j = 1; j < N - K + 1; j++) {
            if(b[j].first == b[j-1].first) {
                continue;
            }
            area = b[j].first * b[j].first + b[j].first * b[j].second * 2;
            //cout << area << endl;
            c.clear();
            for(int k = j+1; k < b.size(); k++) {
                ll ar = b[k].second * b[k].first * 2;
                c.insert(ar);
            }
            it = c.rbegin();
            for(int k = 0; k < K - 1; k++) {
                area += *it;
                it++;
            }
            //cout << area << endl;
            if(area > max) {
                max = area;
            }
        }
        cout << fixed << setprecision(9) << "Case #" << i+1 << ": " << max*M_PI;
        cout << endl;
    }
    return 0;
}
