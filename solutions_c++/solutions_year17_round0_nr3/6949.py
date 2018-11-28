#include <iostream>
#include <math.h> 
#include <vector>
#include <functional>
#include <queue>
using namespace std;



int main() {
    int numCases = 0;
    cin >> numCases;

    unsigned long long n = 0;
    unsigned long long k = 0; 


    for (int i = 0; i < numCases; i++) {
        cin >> n;
        cin >> k;
        std::priority_queue<unsigned long long> runs;


        unsigned long long y = 0;
        unsigned long long z = 0;

        unsigned long long longestRun = 0;
        runs.push(n);

        for (unsigned long long i = 0; i < k; i++) {

          //  cout <<  "heap top: " << runs.top() << endl;
            //pop the max
            longestRun = runs.top();

            unsigned long long midpnt = longestRun/2;

          //  cout <<  "longest run: " << longestRun << endl;
            if (longestRun %2 == 0) {
                y = midpnt;
                z = y - 1;
            } else {
                y = midpnt;
                z = midpnt;
            }
            //cout <<  "z " << z << endl; //min
           // cout <<  "y " << y << endl << endl; // max

            runs.push(z);
            runs.pop();
            runs.push(y);



        }

        cout << "Case #" << (i+1) << ": " << y << " " << z << endl;
    }
}

