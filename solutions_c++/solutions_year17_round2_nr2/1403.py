#include <bits/stdc++.h>

using namespace std;

bool good(const vector<int>& arrangement) {
    int n = arrangement.size();
    for(int i = 0 ;i < n ; i++){
        int j = (i + 1)%n;
        if(i == j) {
            continue;
        }
        if(arrangement[i] & arrangement[j]) {
            return false;
        }
    }
    return true;
}

string toStr(int color) {
    string ret;
    switch(color) {
        case 1:
            ret = "B";
            break;
        case 2:
            ret = "Y";
            break;
        case 3:
            ret = "G";
            break;
        case 4:
            ret = "R";
            break;
        case 5:
            ret = "V";
            break;
        case 6:
            ret = "O";
            break;
        default:
            break;
    }
    return ret;
}

void put(int color, int num, vector<int>& arrangement) {
    for(int i = 0 ;i <num ; i++) {
        int where = 0;
        int n = arrangement.size();
        for(int j =0 ; j < n ;j++) {
            int k = (j + 1)%n;
            if(k == j) {
                continue;
            }
            if(arrangement[j] & arrangement[k]) {
                where = k;
                break;
            } else {
                if(arrangement[j] & color) {
                    ;
                } else if(arrangement[k] & color) {
                    ;
                } else {
                    where = k;
                }
            }
        }
        arrangement.insert(arrangement.begin() + where, color);
    }
}

void solve() {
    int counts[10];
    auto nums = {4, 6, 2, 3, 1, 5};
    int _;
    cin >> _;
    for(auto num: nums) {
        cin >> counts[num];
    }

    // for(int i = 1 ; i <= 6 ; i++){
    //     cout << toStr(i) << " : " << counts[i] << endl;
    // }
    // cout << endl;

    vector<int> arrangement;

    // small
    vector<pair<int, int> > colors;
    colors.push_back(make_pair(counts[1], 1));
    colors.push_back(make_pair(counts[2], 2));
    colors.push_back(make_pair(counts[4], 4));
        
    sort(colors.begin(), colors.end(), std::greater<pair<int, int>>());

    // for(auto color:  colors) {
    //     cout << toStr(color.second) << " : " << color.second << " : " << color.first << endl;
    // }

    for(int i = 0 ;i < colors[0].first; i++) {
        arrangement.push_back(colors[0].second);
    }

    put(colors[1].second, colors[1].first, arrangement);
    put(colors[2].second, colors[2].first, arrangement);

    //

    // cout << "have : " << endl;
    // for(auto color : arrangement) {
    //     cout << toStr(color) << " ";
    // }
    // cout << endl << endl;

    if (good(arrangement)) {
        for(auto color: arrangement) {
            cout << toStr(color);
        }
        cout << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    int te;
    cin >> te;
    for(int t = 1 ; t <= te ; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
