//
//  main.cpp
//  oversizedPancakeFlipper
//
//  Created by Mario Jimenez on 4/8/17.
//  Copyright © 2017 mariot. All rights reserved.
//

#include <iostream>
#include "string"
using namespace std;

//string flipPancakes(string &pancakes, int position, int flipperLength);

int main() {

    bool impossible = false;
    int testCases, flipperLength, flipCount;
    string pancakes;
    
    cin >> testCases;
    
    for (int test = 1; test <= testCases; test++) {
        
        cin >> pancakes; // T test cases
        cin >> flipperLength; // K flipper
        
        flipCount = 0; // Reset flip Count
        
        //For every pancake position between (0..length - K)
        for (int position = 0; position <= pancakes.length() - flipperLength; position++) {
            
            if(pancakes[position] == '-') {
                
                for (int count = 0; count < flipperLength; count++) {
                    
                    if(pancakes[position + count] == '-') {
                        pancakes[position + count] = '+';
                    } else {
                        pancakes[position + count] = '-';
                    }
                    
                }
                
                /*
                for (int position = 0; position < pancakes.length(); position++) {
                    cout << pancakes[position];
                }
                cout << endl; */
                
                flipCount++;
            
            }
        }
    
        
        for (int position = 0; position < pancakes.length(); position++) {
            
            //Loop over pancakes and check to see if any 1 is not happy.
            if(pancakes[position] == '-') {
                impossible = true;
                break;
            } else {
                impossible = false;
            }
        }
        
        if(impossible) {
            cout << "Case #" << test << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << test << ": " << flipCount << endl;
        }
        
    }
    
    return 0;
}

