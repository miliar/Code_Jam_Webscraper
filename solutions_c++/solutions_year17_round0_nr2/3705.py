#include <bits/stdc++.h>

using namespace std;
vector <int> v;
int main()
{
    //freopen("B-large.in", "r", stdin);
  //  freopen("out.txt", "w", stdout);
    int t, k, cases = 1;
    long long n, m;
    scanf("%d", &t);
    while (t--) {
        scanf("%I64d", &n);
        m = n;
        v.clear();
        while (m > 0) {
            v.push_back(m % 10);
            m /= 10;
        }
        m = 10;
        int last = -1;
        for (int i = 0; i < v.size(); i++) {
            if (v[i] > m) {
                v[i]--;
                last = i;
            }
            m = v[i];
        }
        for (int i = 0; i < last; i++) {
            v[i] = 9;
        }
        if (v[v.size() - 1] == 0)v.pop_back();

        m = 0;

        for (int i = v.size() - 1; i >= 0; i--) {
            m = m * 10 + v[i];
        }

        printf("Case #%d: %I64d\n", cases ++ , m);
    }
    return 0;
}
