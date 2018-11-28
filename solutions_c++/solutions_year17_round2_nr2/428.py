/*
 Created by Saidolda Bayan.
 Copyright (c) 2015 Bayan. All rights reserved.
 LANG: C++
 */
#include <bits/stdc++.h>

#define _USE_MATH_DEFINES
#define y1 lalka
#define right napravo
#define left nalevo
#define pb push_back
#define mp make_pair
#define f first
#define s second

using namespace std;
using pii = pair<int, int>;
using ll = long long;
using ld = long double;

const int INF = (int)1e9+7, mod = (int)1e9+9, pw = 31, N = (int)1e5+123, M = (int)1e6+123;
const double eps = 1e-11;
const long long inf = 1e18;

enum colors {red, orange, yellow, green, blue, violet};
string what[] = {"R", "O", "Y", "G", "B", "V"};

int cnt[8];
vector<string> all[8];

bool check(int x, int y) {
    while (cnt[x] && cnt[y] > 1) {
        --cnt[x];
        --cnt[y];
        
        all[x].pop_back();
        string u = all[y].back();
        all[y].pop_back();
        
        string v = all[y].back();
        all[y].pop_back();
        
        all[y].pb(u + what[x] + v);
    }
    return cnt[x];
}

void solve() {
    int n;
    cin >> n;
    for (int i = 0; i < 6; i++) {
        cin >> cnt[i];
        all[i].clear();
        for (int j = 0; j < cnt[i]; j++)
            all[i].pb(what[i]);
    }
    if (check(orange, blue) || check(green, red) || check(violet, yellow)) {
        assert(false);
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    int masks[] = {red, yellow, blue};
    sort(masks, masks + 3, [](int x, int y) {
        return cnt[x] > cnt[y];
    });
    
    /*for (auto it : all[masks[0]]) cout << it << ' ';
    cout << " vs ";
    for (auto it : all[masks[1]]) cout << it << ' ';
    cout << " vs ";
    for (auto it : all[masks[2]]) cout << it << ' ';
    cout << endl;*/
    
    vector<string> ans;
    if (cnt[masks[1]] + cnt[masks[2]] < cnt[masks[0]]) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    for (auto it : all[masks[0]]) {
        ans.pb(it);
        if (!all[masks[1]].empty()) {
            ans.pb(all[masks[1]].back());
            all[masks[1]].pop_back();
        } else {
            ans.pb(all[masks[2]].back());
            all[masks[2]].pop_back();
        }
    }
    
    /*for (auto it : ans)
        cout << it;
    cout << endl;
    for (auto it : all[masks[1]]) cout << it << ' ';
    cout << " vs ";
    for (auto it : all[masks[2]]) cout << it << ' ';
    cout << endl;*/
    
    for (int i = 0; i < all[masks[1]].size(); i++) {
        ans.insert(ans.begin() + 2 * i + 1, all[masks[1]][i]);
    }
    for (int i = 0; i < all[masks[2]].size(); i++) {
        ans.insert(ans.begin() + 2 * i + 1, all[masks[2]][i]);
    }
    for (auto it : ans)
        cout << it;
    cout << endl;
}

int main ()
{
    ios_base::sync_with_stdio(0);cin.tie(NULL);

    freopen("in.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
