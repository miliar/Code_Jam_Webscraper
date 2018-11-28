#include <bits/stdc++.h>

using namespace std;

pair<long long, long long> _partition(long long n)
{
    if (n % 2 == 0) {
        return make_pair(n / 2, n / 2 - 1);
    }
    return make_pair(n / 2, n / 2);
}

long long msb(long long n)
{
    int val = 0;
    while (n > 0) {
        n = n >> 1;
        val++;
    }
    return 1LL << (val - 1);
}

pair<long long, long long> solve(long long n, long long k)
{
    //cout << n << " " << k << endl;
    if (n == k) {
        return make_pair(0LL, 0LL);
    }
    auto portions = _partition(n);
    if (k == 1) {
        return portions;
    }
    if (k % 2 == 0) {
        return solve(portions.first, k / 2);
    }
    return solve(portions.second, k / 2);

    /*

    long long full_low_level = msb(k);
    long long max_full_tree = full_low_level - 1;
    long long actual_low_level = k - max_full_tree;

    if (actual_low_level <= full_low_level / 2) {
        return solve(portions.first, max_full_tree / 2 + actual_low_level);
    }
    return solve(portions.second, max_full_tree / 2 + actual_low_level - full_low_level / 2);
    */
}
/*
int main()
{
   // freopen("C-small-1-attempt1.in", "r", stdin);
   // freopen("aa.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    //int t;
    //cin >> t;
    long long n, k;
    n = 17;
    //aaa:

    for (int x = 11; x <= n; x++) {
      //  cin >> n >> k;
        k = x;
        auto ans = solve(n, k);
        vector<int> v;
        queue<int> q;
        q.push(n);
        while (!q.empty()) {
            int temp = q.front();
            q.pop();
            if (temp == 0)continue;
            v.push_back(temp);
            if (temp == 1)continue;
            auto temp2 = _partition(temp);
            q.push(temp2.first);
            q.push(temp2.second);
        }
        auto temp = _partition(v[k - 1]);
        //cout << "Case #" << x << ": " << ans.first << " " << ans.second << endl;
        //cout << ans.first << " " << ans.second << end;
        //cout << temp.first << " " << temp.second << endl << endl;

//        cout << "Case #" << x << ": " << temp.first << " " << temp.second;
//        cout << ", " << ans.first << " " << ans.second << endl;
        if (temp.first != ans.first || temp.second != ans.second) {
            cout << n << " " << k << ": " << temp.first << " " << temp.second;
            cout << ", " << ans.first << " " << ans.second << endl;
            break;
        }

    }
//    if (n < 20) {
//        n++;
//        goto aaa;
//    }
    return 0;
}

*/

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int x = 1; x <= t; x++) {
        long long n, k;
        cin >> n >> k;
        auto ans = solve(n, k);
        cout << "Case #" << x << ": " << ans.first << " " << ans.second << endl;

    }
    return 0;
}
