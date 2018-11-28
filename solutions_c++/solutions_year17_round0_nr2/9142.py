//
//  main.cpp
//  G_17_Q_BB
//
//  Created by Willindigo ☠ on 4/7/17.
//  Copyright © 2017 Glo.am Interactive, LLC. All rights reserved.
//
#pragma once
#include <iostream>
#include <string>
#include "bigint.h"

using namespace std;

bool isTidy (BigInt);
BigInt cN; // Global candidate for fast decrement

int main(int argc, const char * argv[]) {

    int T;  // Variable for # of cases
    std::string SN;  // String input
    apstring nn;
    BigInt N, tidiest; // BigInt representation of input
    bool found = false; // Highest Tidy Number Found Flag
    
    
    // Take in # of cases
    cin >> T;
    
    for (int counter = 1; counter <= T; counter++)
    {
        found = false; // Initialize found flag to false for this case
        tidiest = 0;  // Initialize tidiest number found to 0 fot this case
        cin >> nn;  // Accept candidate N from as input
        
        N = BigInt(nn);  // Convert input to BigInteger for interator operation
        cN = N;
        //SN = bigIntegerToString(N);  // The candidate to be evaluated for tidiness
        
        //cout << N.getLength() << endl;
        //cout << "Capacity - " << N.getCapacity() << endl;
        
        while (!found && (cN > 0))
        {
            if (isTidy(cN))
            {
                found = true;
                tidiest = (cN+1)-1;
            }
//            else
//            {
//                cN = cN - 1;
//            }
        }
        
        if (found)
        {
            cout << "Case #" << counter << ": " << tidiest.ToString() << endl;
        }
        else
        {
            cout << "Case #" << counter << ": " << "Nothing found" << endl;
        }
        
    }
    
    
    
    return 0;
}

// Accepts a string representation of an integer to be compared for tidiness
bool isTidy (BigInt tidyCandidate)
{
    if (tidyCandidate.NumDigits() == 1)
    {
        return true;
    }
    for (int iStr = 0; iStr < tidyCandidate.NumDigits(); iStr = iStr + 1)
    {
        
        // If the
        if (!(tidyCandidate.GetDigit(iStr) >= tidyCandidate.GetDigit(iStr+1)))
        {
            // If the next significant digit is NOT a one
//            if (cN.GetDigit(iStr+1) != 1)
//            {
                cN.ChangeDigit(iStr+1, cN.GetDigit(iStr+1)-1);
                for (int backfill = iStr; backfill >= 0; backfill--)
                {
                    cN.ChangeDigit(backfill, 9);
                }
                //cN.ChangeDigit(iStr, 9);
//            }
//            else
//            {
//                // Set next digit over to 0
//                cN.ChangeDigit(iStr+1, cN.GetDigit(iStr));
//                // Back fill with 9s
//                for (int backfill = iStr; backfill >= 0; backfill--)
//                {
//                    cN.ChangeDigit(backfill, 9);
//                }
//            }

            
            
            // Check for cascading deficit in preceding number chain
            //if (tidyCandidate.NumDigits() > 3)
//            while ((cN.GetDigit(iStr) < cN.GetDigit(iStr+1)) && (iStr < (cN.NumDigits()-1)))
//            {
//                // Enable fast decrement
//                cN.ChangeDigit(iStr+1, cN.GetDigit(iStr));
//                iStr = iStr + 1;
//                //cout << "Changing " << cN.GetDigit(iStr+1)  << " to " << tidyCandidate.GetDigit(iStr) << endl;
//                //cN.ChangeDigit(iStr+1, tidyCandidate.GetDigit(iStr));
//                
//            }
            if (isTidy(cN))
            {
                return true;
            }
            return false;
        }
        
    }
    return true;
}
