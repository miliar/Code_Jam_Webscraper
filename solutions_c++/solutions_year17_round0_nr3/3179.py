
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

pair<ll, ll> solve(ll N, ll K) {
    if (K == N)
        return make_pair(0, 0);
    
    auto m = map<ll, ll>();
    m[N] = 1;
    ll count = 0; 
    while (count < K) {
        auto it = m.rbegin();
        ll key = it->first, val = it->second;
        if (key % 2 == 0) {
            m[key/2] += val;
            m[key/2-1] += val;
        }
        else 
            m[(key-1)/2] += 2*val;
        m.erase(key);

        if (count + val >= K) {
            if (key % 2 == 1)
                return make_pair((key-1)/2, (key-1)/2);
            else 
                return make_pair(key/2, key/2-1);
        }

        count += val;
    }
    return make_pair(0, 0);
}

int main(int argc, char* argv[]) {
    ifstream infile(argv[1]);
    ofstream outfile(argv[2]);
    ll T, N, K;
    infile >> T;
    for (int i=1; i<=T; i++) {
        infile >> N >> K;
        auto ans = solve(N, K);
        outfile << "Case #" << i << ": " << ans.first << " " << ans.second << endl;
    }
    infile.close();
    outfile.close();
}
