#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <sstream>
#include <deque>
#include <iomanip>
#include <utility>
#include <bitset>
#define MAXN 51

using namespace std;

//Globals
bool debug;
int N, K;

//Helper Functions

double solve(double p[], double U){
    sort(p,p+N);
    if (debug) cout << "In solve U= " << U << endl;
    if (debug)
        for(int i=0; i<N; i++) cout << p[i] << " ";
    if (debug) cout << endl;
    int nums = 0; //I will add to p upto this index
    while (U > 1e-9 && nums < N-1){

        double gap = p[nums+1] - p[0];
        if (debug) cout << "\t IN LOOP nums = " << nums << " U now " << U << " gap " << gap << endl;
        if (U>=gap*(nums+1)){
            if (debug) cout << "\t\t FITS" << endl;
            U -= (gap*(nums+1));

        }
        else{
            if (debug) cout << "\t\t NOT FITS" << endl;
            gap = U / (nums+1);
            U=0;
        }
        for (int i=0; i<=nums; i++){
            p[i] += gap;

        }
        nums++;



    }
    double out = 1;
    for (int i=0; i<N;i++){
        out *= p[i];
    }
    return out;

}
//Main solver function


int main()
{
    int T;
    debug = false;
    double U;
    double p[MAXN];



    if (debug) cout << "<<<<<DEBUG PRINTS ENABLED>>>>>" << endl;

    cin >> T;

    for (int tc=1; tc<=T; tc++){
        if (tc==-1) debug =true;
        else debug = false;
        if (debug) cout << "Test Case #" << tc << " of " << T << endl;
        //read data
        cin >> N >> K;
        cin>> U;
        if (debug) cout << "Read U " << U << endl;
        for(int i=0; i<N;i++) {
            cin >> p[i];
            if (debug) cout << "\tRead p " << p[i] << endl;
        }
        p[N] = 1.0;
        N++;






        cout << "Case #" << tc << ": " << setprecision(9) << solve(p,U) << endl;
    }



    if (debug) cout << "<<<<<DEBUG PRINTS ENABLED>>>>>" << endl;
    return 0;
}
