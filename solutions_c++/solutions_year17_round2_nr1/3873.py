#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;


int main() {
    int T, goal, horses;
    int Ki, Si;
    double maxTime;
    double result;
    cin >> T;
    for (int i = 1; i <= T; ++i){
        cin >> goal;
        cin >> horses;
        maxTime = 0;
        for(int j=0; j<horses; j++){
            cin >> Ki;
            cin >> Si;
            double time = (double)(goal-Ki)/(double)(Si);
            if(time>maxTime){
                maxTime = time;
            }
        }
        result = (double)goal/maxTime;
        printf("Case #%d: %.6f\n", i, result);
    }
}
