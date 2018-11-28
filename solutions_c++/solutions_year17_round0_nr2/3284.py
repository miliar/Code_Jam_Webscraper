//
//  main.cpp
//  CPPTest
//
//  Created by Roi Berlin on 3/11/17.
//  Copyright © 2017 uMake. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <set>
#include <map>
#include <vector>
using namespace std;

long getFirstNotTidyIndex(string& number)
{
    for (long index = 0 ; index < number.size() - 1 ; ++index)
    {
        if (number[index] > number[index+1])
        {
            return index;
        }
    }
    
    return -1;
}

string createTidyNum(long size)
{
    string newNum;
    
    for (long index = 0 ; index < size ; ++index)
    {
        newNum += "9";
    }
    
    return newNum;
}

string tryFixToTidy(string& number, long index)
{
    if (index == 0 && number[0] == '1')
    {
        return createTidyNum(number.size() - 1);
    }
    
    number[index] = number[index] - 1;
    
    return number.substr(0, index + 1) + createTidyNum(number.size() - (index + 1));
}




int main(int argc, const char * argv[]) {
    // insert code here...
    FILE *fin = freopen("B-large.in", "r", stdin);
    
    int T = 0;
    string number = "";
    
    cin >> T;
    
    for (int iteration = 1 ; iteration <= T ; ++iteration)
    {
        cin >> number;
        
        long notTidyIndex = getFirstNotTidyIndex(number);
        
        while (notTidyIndex != -1)
        {
            number = tryFixToTidy(number, notTidyIndex);
            notTidyIndex = getFirstNotTidyIndex(number);
        }
        
        cout << "Case #" << iteration << ": " << number << endl;
    }
    
    return 0;
}
