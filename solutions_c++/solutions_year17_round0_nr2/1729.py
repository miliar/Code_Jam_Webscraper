#include <bits/stdc++.h>
using namespace std;

#define int long long
vector<int> num;
void build(int digit, int val, int last)
{
    if (digit >= 19)
        return;
    num.push_back(val);
    for (int i = last; i <= 9; i++) {
        build(digit + 1LL, val * 10LL + i, i);
    }
}
#undef int
int main()
{
#define int long long
    for (int i = 1; i <= 9; i++)
        build(1, i, i);
    int T;
    cin >> T;
    int kase = 0;
    sort(num.begin(), num.end());
    while (T--) {
        cout << "Case #" << ++kase << ": ";
        int N;
        cin >> N;
        int l = 0;
        int r = num.size() - 1;
        int ans = 0;
        while (l <= r) {
            int mid = (l + r) >> 1LL;
            if (num[mid] > N)
                r = mid - 1LL;
            else {
                if (num[mid] > ans)
                    ans = num[mid];
                l = mid + 1LL;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
