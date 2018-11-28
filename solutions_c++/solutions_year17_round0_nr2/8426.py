#include <iostream>
using namespace std;

const int N = 1001;
bool isTidy[N];

bool tidy(int n)
{
    int prev = 9;
    while (n >= 10)
    {
        int t = n%10;
        if (t > prev) return false;
        n /= 10;
        prev = t;
    }
    return prev >= n;
}

int solve(int n)
{
    for (int i=n; n >= 0; --i) {
        if (isTidy[i]) return i;
    }
    return 0;
}

int main()
{
    for (int i=0; i < N; ++i) {
        isTidy[i] = tidy(i);
    }

    int T;
    cin >> T;
    for (int ci=0; ci < T; ++ci) {
        int n = 0;
        cin >> n;
        int res = solve(n);
        cout << "Case #" << ci+1 << ": " << res << endl;
    }
}
