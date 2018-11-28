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
#define MAXN 10
#define PI 3.14159265358979323846264

using namespace std;

//Globals
bool debug;
int N, K;

//Helper Functions
int getnext(int key){


    if (debug) cout << "key in get_next " << key << endl;
    int _key,c;
    bool found =0;

    while (key > 0){
        key--;
        _key = key;
        while (_key){
            c = 0;
            for (int i=0; i<10; i++){
                if (_key%2) c++;
                _key /=2;
            }

        }
        if (c == K) return key;
    }
    return 0;

}

double solve(int R[], int H[]){  //sorted

    int maxR = 0;
    double RH[MAXN];
    int maxKey = 1;
    for (int i=0; i<N; i++) {
        maxKey *= 2;
        RH[i] = double (R[i])  * H[i];
    }
    double bestSoFar = 0.0;

    int next_key;

    next_key = getnext(maxKey);
    if (debug) cout << "key " << next_key << endl;

    while (next_key){
        int this_key = next_key;
        double this_R_area = 0;
        double this_H_area = 0;

        for (int i=0; i<N; i++){
            if (this_key%2){
                if (PI*R[i]*R[i] > this_R_area) this_R_area = PI*R[i]*R[i];
                this_H_area += (2*PI*RH[i]);
            }
            this_key/=2;

        }
        if (this_H_area+this_R_area > bestSoFar) bestSoFar = this_H_area+this_R_area;
        next_key = getnext(next_key);

        if (debug) cout << "key "  << next_key << endl;


    }
    return bestSoFar;




}


//Main solver function


int main()
{
    int T;
    debug = false;
    int R[MAXN];
    int H[MAXN];


    if (debug) cout << "<<<<<DEBUG PRINTS ENABLED>>>>>" << endl;

    cin >> T;

    for (int tc=1; tc<=T; tc++){
        if (debug) cout << "Test Case #" << tc << " of " << T << endl;
        //read data
        cin >> N >> K;
        for (int i=0; i<N; i++) {
            cin >> R[i] >> H[i];

        }





        cout << "Case #" << tc << ": " << setprecision(9) << solve(R, H) << endl;
    }



    if (debug) cout << "<<<<<DEBUG PRINTS ENABLED>>>>>" << endl;
    return 0;
}
