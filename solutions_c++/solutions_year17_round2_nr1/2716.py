#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;


int main(int argc, char** argv){
    int ncases;
    cin >> ncases >> ws;
    for(int c=0; c<ncases; c++){
        double maxH = 0;
        double d,n;
        cin >> d >> ws >> n >> ws;
        for(; n > 0; --n ){
            double k, s;
            cin >> k >> ws >> s >> ws;
            double h = (d - k) / s;
            if(h > maxH){
                maxH = h;
            }
        }
        double res = d/maxH;
         cout << "Case #" << c + 1 << ": " << setprecision(6) << fixed << res << endl;    
    }
    return 0;
}