#include <bits/stdc++.h>
using namespace std;
using ll=long long;
int cas;

int main(){
    int T;
    cin >> T;
    for(; T--; ){
        printf("Case #%d: ", ++cas);
        // //////////////////////////////////

        int n, d;
        cin >> d >> n;
        double res=DBL_MAX;
        for(int i=0; i<n; i++){
            int k, m;
            cin >> k >> m;
            res=min(res, double(m)*d/(d-k));
        }
        printf("%.6f\n", res);



        /////////////////////////////////////////////

    }
    return 0;
}