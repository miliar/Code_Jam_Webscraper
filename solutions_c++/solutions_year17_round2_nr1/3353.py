#include <iostream>
#include <string> 
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <iomanip>
using namespace std;
#define scale 0.000001

int main(){

    int T;
    cin >> T;
    for (int x=0;x<T;x++){
        long double D=0.000000,N;
        cin >> D >> N;
        long double maxTime = 0.000000;
        for(int i =0;i<N;i++){
            long double K=0.000000,S=0.000000;
            cin >> K >> S;
            long double time = 0.000000;
            time = (D-K)/S;
            maxTime = maxTime > time ? maxTime:time;
        }
        double speed = 0.000000000000000;
        speed = D/maxTime;
        cout << std::fixed;
        cout << std::setprecision(6);
        cout << "Case #"<<x+1<<": "<<speed<<endl;
        
    }
    return 0;
}