// Kasimir Tanner 2017
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;
typedef long double uld;

int main(){
    ullint T;
    cin >> T;

    for(ullint t = 0;t<T;t++){
        uld D, N;
        cin >> D >> N;

        uld m = -1;

        for(ullint i = 0;i<N;i++){
            uld k,s;
            cin >> k >> s;
            uld d = D-k;
            uld dt = d/s;
            
            if(dt > m){
                m = dt;
            }
        }

        cout << "Case #" << t+1 << ": " << fixed << setprecision(6) << D/m << "\n";


    }

}
