#include <cstdio>
#include <iostream>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

void solve(int test){
    printf("Case #%d: ", test);
    long long n, k;
    cin >> n >> k;
    map<long long, long long> mp;
    mp[n] = 1;
    while (true){
        vector< pair<long long, long long> > keys;
        for (map<long long, long long>::iterator it = mp.begin(); it != mp.end(); it++){
            keys.push_back(make_pair((*it).first, (*it).second));
        }
        sort(keys.begin(), keys.end());
        reverse(keys.begin(), keys.end());
        long long sum = 0;
        for (int i = 0; i < keys.size(); i++){
            sum += keys[i].second;
            if (k <= sum){
                long long l = (keys[i].first % 2 == 1 ? keys[i].first / 2 : keys[i].first / 2 - 1);
                long long r = keys[i].first / 2;
                cout << r << ' ' << l << endl;
                return;
            }
        }
        vector< pair<long long, long long> > t;
        for (int i = 0; i < keys.size(); i++){
            long long l = (keys[i].first % 2 == 1 ? keys[i].first / 2 : keys[i].first / 2 - 1);
            long long r = keys[i].first / 2;
            k -= keys[i].second;
            t.push_back(make_pair(l, keys[i].second));
            t.push_back(make_pair(r, keys[i].second));
        }
        mp.clear();
        for (int i = 0; i < t.size(); i++){
            mp[t[i].first] += t[i].second;
        }
    }
}

int main(){
    //freopen("input.txt", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("C-large-out.txt", "w", stdout);
    int t; cin >> t;
    for (int i = 0; i < t; i++){
        solve(i + 1);
    }
    return 0;
}
