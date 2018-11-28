//============================================================================
// Name        : cruisecontrol.cpp
// Author      : Ajay Kedare
// Version     :
// Copyright   : Your copyright notice
// Description : Patterns Overlap
//============================================================================

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int T;
    cin >> T;
    int j=0;
    int D,N;
    while(T--){
    	    j++;
    	    cin >> D >> N;
    	    double maxTime=0;
    	    double Ki,Si;
    	    for(int i=0; i<N; i++){
    	    	cin >> Ki >> Si;
    	    	double time = (D-Ki)/Si;
    	    	if(time > maxTime) {
    	    		maxTime=time;
    	    	}
    	    }
    	    double out = (double)D/maxTime;

    	    cout <<"Case #"<<j<<": ";
    	    printf("%.7f\n", out);
    	}
    return 0;
}
