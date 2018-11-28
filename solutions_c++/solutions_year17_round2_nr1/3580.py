#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    long long int t, d, nh, c = 0, k, v;
    long double max, time, s;

    cin >> t;
    for(int i = 0; i < t; i++){
        cin >> d >> nh;
        max = 0;

        for(int j = 0; j < nh; j++){
            cin >> k >> v;
            k = d - k;
            time = (long double)k / (long double)v;
            if(max < time)
                max = time;
        }
        cout << fixed;
        s = d / max;
        cout << setprecision(6);
        cout << "Case #" << ++c << ": " << s << endl;
    }
    return 0;
}
