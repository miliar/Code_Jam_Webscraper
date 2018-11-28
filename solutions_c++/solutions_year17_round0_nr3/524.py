//
//  main.cpp
//  Codejam2017
//
//  Created by Lavi on 2017-04-08.
//  Copyright © 2017 Lavi. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;


int main() {
    int T;
    cin >> T;
    for (int t=1;t<=T;t++){
        long long unsigned int N, K;
        cin >> N  >> K;
        long long unsigned int under2pow=1;
        while (under2pow * 2 <= K) under2pow*=2;
        long long unsigned int smallerpart = (N - (under2pow-1))/under2pow;
        long long unsigned int numberbiggerparts = (N - (under2pow-1)) % under2pow;
        long long unsigned int finalpart = numberbiggerparts >= K - (under2pow -1) ? smallerpart +1 : smallerpart;
        long long unsigned int finalpartbroken = (finalpart-1)/2;
        cout << "Case #" << t << ": ";
        if (finalpart %2 == 1){
            cout << finalpartbroken << " " << finalpartbroken << endl;
        }
        else cout << finalpartbroken+1 << " " << finalpartbroken << endl;
    }
}
