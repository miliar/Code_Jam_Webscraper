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

using namespace std;

//Globals
bool debug;

//Helper Functions




int main()
{
    int T;
    debug = false;
    int N;
    int starts[1000];
    int speeds[1000];
    double longestTime;
    double times[1000];
    int D;


    if (debug) cout << "<<<<<DEBUG PRINTS ENABLED>>>>>" << endl;

    cin >> T;

    for (int tc=1; tc<=T; tc++){
        if (debug) cout << "Test Case #" << tc << " of " << T << endl;
        //read data
        cin >> D >> N;

        for (int i=0; i<N; i++){
            cin >> starts[i] >> speeds[i];
            times[i] = double(D - starts[i]) / speeds[i];
            if (!i || times[i] > longestTime) longestTime = times[i];

        if (debug) cout << i << " " << times[i] << " " << longestTime << endl;


        }




        cout << "Case #" << tc << ": " << fixed << setprecision(9) << D / longestTime << endl;
    }



    if (debug) cout << "<<<<<DEBUG PRINTS ENABLED>>>>>" << endl;
    return 0;
}
