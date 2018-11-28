#include <bits/stdc++.h>

using namespace std;

int calc(int d, int occupied[], int index) {
    int now = index;
    while(!occupied[now]) {
        now += d;
    }
    if(now > index) {
        return now - index -1 ;
    }
    return index - now - 1;
}

pair<pair<int, int>, int> calc(int occupied[], int index) {
    auto a = calc(-1, occupied, index);
    auto b = calc(1, occupied, index);
    return make_pair(make_pair(min(a, b), max(a, b)), -index);
}

string solve() {
    pair<int, int> ans;

    int n, k;
    cin >> n >> k;
    
    int occupied[10000] = {0};
    occupied[0] = 1;
    occupied[n + 1] = 1;

    for(int i = 0 ;i < k ; i++) {
        pair<pair<int, int>, int> choice;
        for(int j = 1 ; j <= n ; j++) {
            choice = max(choice, calc(occupied, j));
        }
        occupied[-choice.second] = 1;
        // cout << "# ";
        // for(int i = 0 ;i <= n+1; i++){
        //     cout << occupied[i] << " ";
        // }
        // cout << endl;
        ans = choice.first;
    }

    stringstream formatter;
    swap(ans.first, ans.second);
    formatter << ans.first << " " << ans.second;
    return formatter.str();
}

int main() {
    int tests;
    cin >> tests;
    for(int i = 1 ;i <= tests; i++) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    return 0;
}
