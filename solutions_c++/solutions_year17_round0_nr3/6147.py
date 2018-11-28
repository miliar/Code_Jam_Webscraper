#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, c = 0; cin >> t;
    while(t--){
        cout << "Case #" << ++c << ": ";
        long long n, k;
        cin >> n >> k;

        priority_queue <long long> curr;
        curr.push(n);

        int i = 0;
        while(i < k-1){
            long long val = curr.top() - 1;
            curr.pop();

            long long x = val/2;
            long long y = val - x;

            curr.push(max(x, y));
            curr.push(min(x, y));
            i++;
        }

        long long ans = curr.top()-1;
        long long x = ans / 2;
        long long y = ans - x;

        cout  << max(x, y) << " " << min(x, y) << "\n";
    }
    return 0;
}
