#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t, n, s;
    long d, k;
    cin >> t;
    for (int z=1; z<=t; ++z){
        cin >> d >> n;
        double prev, currtime;
        for (int i=0; i<n; ++i){
            cin >> k >> s;
            double currtime = double(d-k)/s;
            if (i == 0){
                prev = currtime;
            }
            else if (currtime > prev){
                prev = currtime;
            }
        }
        double ans = double(d)/prev;
        cout << fixed;
        cout << setprecision(6);
        cout << "Case #" << z << ": " << ans << "\n";
    }
    return 0;
}
