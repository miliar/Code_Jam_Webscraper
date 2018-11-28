#include <bits/stdc++.h>
#include <math.h>
#define INF 100000000000005
#define MAXN 2005
#define mod 1000000007
#pragma comment(lib, "user32")

using namespace std;

#define F first
#define S second
#define MP make_pair
#define all(x) (x).begin(), (x).end()
#define pi 3.14159265358979323846

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

pair <int, int> d[MAXN + 2];

bool cmp(const pair<int, int>&i, const pair<int, int>&j) {
    if(i.first == j.second)
        return i.second < j.second;
    return i.first < j.first;
}

int main() {
    freopen("A-large (2).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, n, k;
    cin >> t;
    for(int z = 0; z < t; ++z) {
        cin >> n >> k;
        for(int i = 0; i < n; ++i) {
            cin >> d[i].first >> d[i].second;
        }
        sort(d, d + n, cmp);

        double ans = 0.0;

        vector <vector <double> > tm;

        for(int i = 0; i < n; ++i) {
            vector <double> temp;
            for(int j = 0; j <= i - 1; ++j) {
                temp.push_back( 2. * d[j].second * pi * d[j].first);
            }
            sort(temp.begin(), temp.end());
            tm.push_back(temp);
        }

        for(int i = k - 1; i < n; ++i) {

            int len = tm[i].size();
            double res = 1. * d[i].first * d[i].first * pi + 2. * d[i].first * d[i].second * pi;

            int kz = 1;
            for(int j = len - 1; j >= 0; --j) {

                if(kz == k) break;

                res += tm[i][j];
                kz += 1;


            }


            ans = max(ans, res);


        }

        cout << "Case #" << z + 1 << ": " << fixed << setprecision(9) << ans << endl;


    }
}
