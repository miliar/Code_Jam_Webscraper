#include <bits/stdc++.h>
using namespace std;
const int EPS = 1e-8;
int main()
{
    freopen("input.txt", "r",stdin);
    freopen("output.txt", "w",stdout);

    int t;
    cin >> t;
    for(int f=0; f<t; f++){
        int dest, n;
        cin >> dest >> n;
        double mx = 0;

        for(int i=0; i<n; i++){
            int pos, speed;
            scanf("%d %d", &pos, &speed);
            mx = max(mx, (dest - pos) / (1.0 * speed));
        }
        cout << "Case #" << f + 1 << ": ";
        if(n == 0 || abs(mx) > EPS){
            cout << fixed << setprecision(7) << dest / mx ;
        }else{
            cout << 0 ;
        }
        cout << endl;
    }

    return 0;
}
