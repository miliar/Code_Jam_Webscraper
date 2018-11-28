#include<iostream>
#include<iomanip>
using namespace std;
typedef long long ll;

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        ll d, n;
        cin >> d >> n;
        ll k, s;
        double time = 0.0;
        for (int i = 0; i < n; i++) {
            cin >> k >> s;
            time = max(time, ((double)d-k)/s);
        }
        cout.precision(6);
        cout << fixed;
        cout << "Case #" << t << ": " << (double)d/time << endl;
    }
}