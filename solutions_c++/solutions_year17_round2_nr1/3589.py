#include<iostream>
#include<vector>
#include<iomanip>

using namespace std;

double eps = 1e-6;

int main(){

    int T = 0;
    cin >> T;
    for(int t=0;t<T;t++){

        int n, d;
        cin >> d >> n;

        vector<double> pos(n), speed(n);
        for(int i=0;i<n;i++){
            cin >> pos[i] >> speed[i];
        }

        double l = 0;
        double r = 1e13;

        // if(t==34){
        //     cout << n << " " << d<< endl;
        //     for(int i=0;i<n;i++){
        //         cout << pos[i] << " " << speed[i] << endl;
        //     }
        // }
        while( (r-l) > eps ){

            bool ok = true;
            double mid  = (r+l)/2;

            for(int i=0;i<n;i++){

                //cout << "! " << i << " " << pos[i] << " " << speed[i] << endl;

                //  0 + mid * t = pos[i] + speed[i] * t

                // t = pos[i] / (mid-speed[i])

                double t1 = d / mid;
                double t2 = (d - pos[i]) / speed[i];

                // if(t==39)
                // {
                //     cout << "!! " << d << " " << pos[i] << " " << speed[i] << endl;
                //     cout << "! " << t1 << " " << t2 << endl;
                // }

                if (t1 < t2)
                    ok = false;
            }

            if(ok)
                l = mid;
            else
                r = mid;


            
             //cout << l << " " << r << endl;
        }

        cout << setprecision(6) << fixed;
        cout << "Case #" << t+1 << ": " << (l+r)/2 << endl;
    }
    return 0;
}