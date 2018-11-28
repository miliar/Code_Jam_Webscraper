#include <bits/stdc++.h>

using namespace std;

int main()
{
#ifdef DEBUG
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
#endif // DEBUG
    std::ios::sync_with_stdio(false);
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        int N;
        double K, S, D;
        cin >> D >> N;
        double ats = 1000000001;
        double max = 0;
        double curr, curr1;
        for(int j = 0; j < N; j++) {
            cin >> K >> S;
            curr1 = (D - K)/S;
            curr = D/curr1;
            if(curr < ats) {
                ats = curr;
            }
            if(curr1 > max) {
                max = curr1;
            }
        }
        //cout << fixed << setprecision(10) << "Case #" << i+1 << ": " << ats << endl;
        cout << fixed << setprecision(10) << "Case #" << i+1 << ": " << D/max << endl;
    }
    return 0;
}
