#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <climits>
using namespace std;

string solve(long long N, long long K){
    vector<pair<long long, long long>> a;
    vector<pair<long long, long long>> b;
    a.push_back(pair<long long, long long>(N, 1));
    while(!a.empty()){
        map<long long, long long> mp;
        for(auto p : a){
            b.push_back(p);
            long long tmp1 = (p.first - 1) / 2;
            long long tmp2 = p.first - 1 - tmp1;
            if(tmp1 > 0) mp[tmp1] += p.second;
            if(tmp2 > 0) mp[tmp2] += p.second;
        }
        a.clear();
        for(auto itr = mp.begin(); itr != mp.end(); itr++)
            a.push_back(pair<long long, long long>(itr->first, itr->second));
    }

    sort(b.begin(), b.end(), greater<pair<long long, long long>>());

    long long cnt = 0;
    int i;
    for(i=0; i<b.size(); i++){
        cnt += b[i].second;
        if(cnt >= K) break;
    }
    long long tmp1 = (b[i].first - 1) / 2;
    long long tmp2 = b[i].first - 1 - tmp1;
    long long mx = max(tmp1, tmp2);
    long long mn = min(tmp1, tmp2);
    return to_string(mx) + " " + to_string(mn);
}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        long long N, K;
        cin >> N >> K;
        cout << "Case #" << i+1 << ": ";
        cout << solve(N, K) << endl;
    }

    return 0;
}
