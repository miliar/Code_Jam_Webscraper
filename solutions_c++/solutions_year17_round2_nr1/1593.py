#include <bits/stdc++.h>

using namespace std;

int x[1010], s[1010];
double T[1010];

int main()
{
//    ios_base::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int tc=1;tc<=t;tc++){
        int n,d;
        double Tmax = 0;
        cin >> d >> n;
        for(int i=0;i<n;i++){
            cin >> x[i];
            cin >> s[i];
            T[i] = 1.0*(d-x[i])/s[i];
            if(T[i] >= Tmax){
                Tmax = T[i];
            }
        }
        double S = 1.0*d/Tmax;
        cout << "Case #" << tc << ": ";
        cout << fixed << setprecision(8) << S << '\n';
    }
    return 0;
}
