#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

long long fromVector(const vector <int>& v) {
    long long ans = 0;
    for (int i = 0; i < v.size(); ++i) {
        ans *= 10;
        ans += v[i];
    }
    return ans;
}

vector <int> fromInt(long long a) {
    vector <int> res;
    while(a) {
        res.push_back(a % 10);
        a /= 10;
    }
    reverse(res.begin(), res.end());
    return res;
}

bool check (int a, vector <int> v) {
    for (int i = 0; i < v.size (); ++i) {
        if (v[i] < a)
            return false;
        if (v[i] > a)
            return true;
    }
    return true;
}

int main () {
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int t1 = 0; t1 < t; ++t1) {
        cout << "Case #" << t1 + 1 << ": ";
        long long n;
        cin >> n;
        vector <int> num = fromInt(n);
        if (num.size() == 1) {
            cout << n << endl;
            continue;
        }
        vector <int> baseAns (num.size() - 1, 9);
        //cout << "STATS: " << n << " " << check(1, num) << " ";
        //for (int i = 0; i < baseAns.size(); ++i)
        //    cout << baseAns[i] << " ";
        //cout << endl;
        if (!check(1, num)) {
            cout << fromVector(baseAns) << endl;
            continue;
        }
        vector <int> ans (num.size(), 9);
        for (int i = 1; i <= 9; ++i)
            if (check(i, num))
                ans[0] = i;
        if (ans[0] < num[0]) {
            cout << fromVector(ans) << endl;
            continue;
        }
        //cout << "STATS: " << ans[0] << " " << ans.size() << endl;
        for (int i = 1; i < num.size(); ++i) {
            vector <int> cutNum;
            for (int j = i; j < num.size(); ++j)
                cutNum.push_back(num[j]);
            for (int j = ans[i-1]; j <= 9; ++j)
                if (check(j, cutNum)) {
                    ans[i] = j;
                }
            if (ans[i] < num[i])
                break;
        }
        cout << fromVector(ans) << endl;
    }
}
