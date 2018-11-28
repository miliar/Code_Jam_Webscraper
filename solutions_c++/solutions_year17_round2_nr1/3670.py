#include <iomanip>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cmath>

std::ifstream cin("large_test.in");
std::ofstream cout("large_test.out");


//using std::cout;

using std::min;
//using std::cin;

int main() {
    double D;
    int T,N;
    double P,V;
    double ti;
    double vi;
    double viMin=10000000000001;

    cin >> T;

    freopen("output2.txt", "wt", stdout);


    for(int e=1;e<=T;++e){
        viMin=10000000000001;
        cin >> D >> N;


        for(int i=0;i<N;++i){
                cin >> P >> V;
                ti = (D-P)/V;
                vi = D/ti;
                viMin=min(viMin,vi);
        }


    cout <<std::setprecision(20)<<"Case #"<<e<<": "<<viMin<<"\n";
    printf("Case #%i: %.10lf\n",e,viMin);




    }

    return 0;
}




