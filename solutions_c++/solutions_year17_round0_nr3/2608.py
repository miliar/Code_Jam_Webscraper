#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int cnt = 0; cnt < t; cnt++){
        long long n, k;
        cin >> n >> k;
        k--;
        long long a = 1;
        long long b = 0;
        while (k >= a + b){
            k -= a + b;
            long long a1 = a;
            long long b1 = b;
            if (n % 2 == 0) b1 += a + b;
            else a1 += a + b;
            a = a1;
            b = b1;
            n = (n - 1) / 2;
        }
        cout << "Case #" << cnt + 1 << ": ";
        if (k >= b){
            cout << n / 2 << " " << (n - 1) / 2;
        }
        else{
            cout << (n + 1) / 2 << " " << n / 2;
        }
        cout << "\n";
    }
    return 0;
}
