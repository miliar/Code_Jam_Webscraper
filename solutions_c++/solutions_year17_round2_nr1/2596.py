#include<iostream>

using namespace std;

int main() {
    int T; cin >> T;
    cout.precision(9);
    cout.flags(ios::fixed);
    for(int t=1; t<=T; t++) {
        double result = 0;
        long long d, n; cin >> d >> n;
        long long k, s;
        for(long long i = 0; i<n; i++) {
            cin >> k >> s;
            k= d-k;
            if(result==0) {
                result=((d*1.0)*s)/k;
            }
            else {
                result=min(result, ((d*1.0)*s)/k);
            }
        }
        cout << "Case #"<< t << ": " << result << "\n";
    }
}
