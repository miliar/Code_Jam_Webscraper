#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int,int>pii;


int main(){
    freopen("inin.in","r",stdin);
    freopen("outout.out","w",stdout);

    int n; scanf("%d", &n);
    for(int f = 0; f < n; f++){
        double d;
        int h;
        cin >> d >> h;
        double mx = 0;
        for(int f = 0; f < h; f++){
            double s, v;
            cin >> s >> v;
            mx = max(mx, (d-s)/v);
        }
        cout << fixed << setprecision(10) << "Case #" << f+1 <<": " << d / mx << endl;
    }


    return 0;
}
