#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair

int main()
{
    //ios::sync_with_stdio(0);
    freopen("4.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int r=0; r<T; r++) {
        ll d,n;
        cin >> d >> n;
        ll temp, temp2;
        cin >> temp >> temp2;
        double maxi = 1.0*(d-temp)/temp2;
        for (int i=1; i<n; i++) {
            cin >> temp >> temp2;
            maxi = max(1.0*(d-temp)/temp2, maxi);
        }
        printf("Case #%d: %.7f\n", r+1, d/maxi);
    }
    return 0;
}
