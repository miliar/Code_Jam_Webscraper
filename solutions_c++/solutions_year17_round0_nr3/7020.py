#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

pair<int, int> masuk(int x) {
    pair<int,int> ret;
    if (((x-1)%2 == 0) || (x == 1)) {
        ret.first = (x-1) / 2;
        ret.second = ret.first;
    } else {
        ret.first = (x-1)/2 + 1;
        ret.second = ret.first - 1;
    }
    return ret;
}


//void printga(vector<int> x) {
//    cout << "list : ";
//    for (auto it = x.begin(); it != x.end(); it++)
//        cout << *it << " ";
//    cout << endl;
//}

bool cmp (int a, int b) { return a > b;}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string N, K;
        cin >> N >> K;
        if (N.length() <= 4) {
            pair<int,int> res;
            int k = stoi(K);
            vector<int> s;

            res = masuk(stoi(N));
            s.push_back(res.first);
            s.push_back(res.second);
            sort(s.begin(), s.end(), cmp);
//            cout << res.first << " " << res.second << endl;
//            printga(s);
            for (int i = 1; i < k; i++) {
                res = masuk(*(s.begin()));
                s.erase(s.begin());
                s.push_back(res.first);
                s.push_back(res.second);
                sort(s.begin(), s.end(), cmp);
//                printga(s);
//                cout << res.first << " " << res.second << endl;
            }
            cout << "Case #" << t << ": "
                 << res.first << " " << res.second << endl;
        }

    }
}
