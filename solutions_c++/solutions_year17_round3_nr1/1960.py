#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

ll s_max = 0;
vector<pair<int, int>> s_cake;

double side(int r, int h) { return (double)2.0 * (double)M_PI * (double)r * (double)h; }

double circle(int r) { return (double)M_PI * (double)r * (double)r; }

ll sideL(int r, int h) { return 2LL * (ll)r * (ll)h; }

ll circleL(int r) { return (ll)r * (ll)r; }


bool compare(const pair<int, int> &l, const pair<int, int> &r) {
    return circle(l.first) + side(l.first, l.second) > circle(r.first) + side(r.first, r.second);
}

bool compare1(const pair<int, int> &l, const pair<int, int> &r) {
    return circleL(l.first) > circleL(r.first);
}

bool compare2(const pair<int, int> &l, const pair<int, int> &r) {
    ll lv = sideL(l.first, l.second);
    ll rv = sideL(r.first, r.second);
    if (lv == rv) {
        return l.first > r.first;
    } else {
        return lv > rv;
    }
}

void printSolution(int n, int k) {
//ll printSolution(int n, int k) {    
    sort(s_cake.begin(), s_cake.end(), compare1);
    ll max_value = 0;
    for (int i = 0; i < n; ++i) {
        auto temp = s_cake;
        long long ans = sideL(temp[i].first, temp[i].second) + circleL(temp[i].first);
        
        int max_r = temp[i].first;

        temp.erase(temp.begin() + i);
        sort(temp.begin(), temp.end(), compare2);
        int count = 1;
        for (int i = 0; i < n - 1 && count < k; ++i) {
            if (temp[i].first <= max_r) {
                ans += sideL(temp[i].first, temp[i].second);
                count++;
            }
        }
        max_value = max(max_value, ans);
    }
    
    cout << fixed << (double)max_value * (double)M_PI << endl;
    //return max_value;
}

ll getNumber(const vector<int>& picked) {
    ll ans = 0;
    int max_r = 0;
    for (int i = 0; i < (int)picked.size(); ++i) {
        ans += sideL(s_cake[picked[i]].first, s_cake[picked[i]].second);
        max_r = max(max_r, s_cake[picked[i]].first);
    }
    ans += circleL(max_r);
    return ans;
}

void pick(int n, vector<int>& picked, int toPick) {
    if (toPick == 0) {
        s_max = max(s_max, getNumber(picked));
        return;
    }

    int smallest = picked.empty() ? 0 : picked.back() + 1;

    for (int next = smallest; next < n; ++next) {
        picked.push_back(next);
        pick(n, picked, toPick - 1);
        picked.pop_back();
    }
}

void printSolution_bf(int n, int k) {
    s_max = 0;
    vector<int> temp;
    pick(n, temp, k);
    //assert(s_max == printSolution(n, k));
    cout << fixed << (double)s_max * M_PI << endl;
}

int main(int argc, char *argv[]) {
    int t;

    cin >> t;
    cout.precision(20);

    for (int i = 1; i <= t; ++i) {
        int n, k;
        cin >> n >> k;
        s_cake.clear();

        for (int j = 0; j < n; ++j) {
            int r, h;
            cin >> r >> h;
            s_cake.push_back(make_pair(r, h));
        }

        cout << "Case #" << i << ": ";
        printSolution(n, k);
    }
    return 0;
}