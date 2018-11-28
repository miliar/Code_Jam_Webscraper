#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

const long double PI = 3.14159265358979323846264;

bool byr (pair <long long, long long> a, pair <long long, long long> b) {
    return a.first > b.first;
}

bool byrh (pair <long long, long long> a, pair <long long, long long> b) {
    return a.first * a.second > b.first * b.second;
}

int main () {
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");
    int t;
    cin >> t;
    for (int t1 = 1; t1 <= t; ++t1) {
        cout << "Case #" << t1 << ": ";
        int n, k;
        cin >> n >> k;
        vector < pair <long long, long long> > v (n);
        for (int i = 0; i < n; ++i)
            cin >> v[i].first >> v[i].second;

        long long ans = 0;
        sort (v.begin(), v.end(), byr);
//        cout << "-----" << endl;
//        for (int z = 0; z < n; ++z)
//            cout << v[z].first << "|" << v[z].second << " ";
//        cout << endl << "----" << endl;
        for (int j = 0; j <= n - k; ++j) {
            long long cur = 0;
            cur += v[j].first * v[j].first + 2 * v[j].first * v[j].second;
            sort (v.begin() + j + 1, v.end(), byrh);
//            cout << "!!!!" << endl;
//            for (int ll = 0; ll < n; ++ll)
//                cout << v[ll].first << "|" << v[ll].second << " ";
//            cout << endl << "!!!!" << endl;
            for (int l = 0; l < k-1; ++l)
                cur += 2 * v[l + j + 1].second * v[l + j + 1].first;
            ans = max (ans, cur);
//            cout << "Cur" << endl;
//            cout << cur << endl;
            sort (v.begin(), v.end(), byr);
        }
        long double realAns = ans * PI;
        cout << fixed << setprecision(10) << realAns << endl;
    }
}
