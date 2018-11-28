#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tt;
    cin >> tt;
    for(int tn = 1; tn <= tt; tn++){
        int n;
        double d;
        cin >> d >> n;
        double mx = 0;
        for(int i = 0; i < n; i++){
            double pos, speed;
            cin >> pos >> speed;
            double x = (d- pos)/ speed;
            mx = max(mx, x);
        }
        double xs =  d / mx;
        printf("Case #%d: %.6f\n", tn, xs);
    }
    return 0;
}
