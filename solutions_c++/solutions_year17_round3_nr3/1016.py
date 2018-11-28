#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;
typedef long long ll;

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int n, k;
        cin >> n >> k;
        double u;
        cin >> u;
        vector<double> v;
        v.resize(n);
        double sum = u;
        for (int i = 0; i < n; i++) {
            cin >> v[i];
            sum += v[i];
        }
        sort(v.begin(), v.end());
        
        int i = n-1;
        for (i = n-1; i >= 0; i--) {
            if (sum/(i+1) >= v[i]) {
                break;
            }else{
                sum -= v[i];
            }
        }
        double ans = pow(sum/(i+1), i+1);
        for (int j = i+1; j < n; j++) {
            ans *= v[j];
        }
        cout.precision(6);
        cout << fixed;
        cout << "Case #" << t << ": " << ans << endl;
    }
}