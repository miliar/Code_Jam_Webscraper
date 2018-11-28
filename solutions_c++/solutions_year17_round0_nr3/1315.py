#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = (n)-1; i >= 0; i--)
using namespace std;
using lli = long long int;
bool f[1000005] = {};
int L[1000005] = {};
int R[1000005] = {};
void solve(lli n, lli k, int l)
{

    map<lli, lli> hoge;
    hoge[n] = 1;
    while (1) {
        lli sum = 0;
        map<lli, lli> foo;
        for (auto& s : hoge) {
            if (s.first == 0)
                continue;
            sum += s.second;
        }
        if (k > sum) {
            for (auto& s : hoge) {
                if (s.first == 0)
                    continue;
                lli j = s.first;
                j--;
                lli temp = j - j / 2;
                j -= temp;
                foo[j] += s.second;
                foo[temp] += s.second;
                //cout << "# " << j << "# " << temp << endl;
            }
            k -= sum;
            swap(hoge, foo);
        } else {
            vector<pair<lli, lli>> ve;
            for (auto& s : hoge) {
                ve.push_back(make_pair(s.first, s.second));
            }
            sort(ve.begin(), ve.end(), greater<pair<lli, lli>>());
            for (auto& bar : ve) {
                //cout << "$" << bar.second << endl;
                if (bar.first == 0)
                    continue;
                if (bar.second < k) {
                    //cout << "HOGE" << bar.second << endl;
                    k -= bar.second;
                } else {
                    lli j = bar.first;
                    j--;
                    lli temp = j - j / 2;
                    j -= temp;
                    cout << "Case #" << l << ": " << temp << " " << j << endl;
                    return;
                }
            }
        }
    }
}
int main()
{
    lli t;
    cin >> t;
    lli n, k;
    rep(i, t)
    {
        cin >> n >> k;
        solve(n, k, i + 1);
    }
}
