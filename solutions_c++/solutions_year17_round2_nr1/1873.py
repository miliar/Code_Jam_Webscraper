#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <set>
#include <functional>
#include <iomanip>

#define x first
#define y second

using namespace std;

int main(){
    FILE * pFile;
    pFile = fopen ("1.out","w");

    int t;
    cin >> t;
    for (int tt=0;tt<t;tt++){
        int d,n;
        cin >> d>>n;

        double maxTime=0;
        for (int i=0;i<n;i++){
            int position,speed;
            cin >> position>>speed;

            double time = (d-position)*1.0/speed;
            maxTime=max(time,maxTime);
        }

        double ans=d/maxTime;

        fprintf (pFile, "Case #%d: %.6f\n",tt+1,ans);
//        output << "Case #" << tt+1 << ": " <<ans<< endl;
//        cout << "Case #" << tt+1 << ": " <<ans<< endl;
    }

    fclose(pFile);
    return 0;
}
