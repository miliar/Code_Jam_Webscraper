//
//  main.cpp
//  codeJam 2
//
//  Created by Mohammad Heydary on 4/7/17.
//  Copyright © 2017 Mohammadreza Hajy Heydary. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    int size;
    double number;
    
    string temp;
    unsigned long stringSize;
    bool tidy;
    int tideyNum;
    
    ifstream file;
    ofstream outfile;
    file.open("B-small-attempt1.in"); ///
    outfile.open("outFile.txt");
    file >> size;
    cout << size << endl;
    for (int k = 0; k < size; k++)
    {
        file >> number;
        cout << number << endl;
        tideyNum = 0;
        for (int i = 1; i <= number; i++)
        {
            temp = to_string(i);
            stringSize = temp.size();
            tidy = true;
            for (int j = 0; j < stringSize-1 ; j++)
            {
                if (temp[j] > temp[j+1])
                {
                    tidy = false;
                    break;
                }
            }
            if (tidy)
            {
                tideyNum = i;
            }
        }
        outfile << "Case #" << k+1 << ": " << tideyNum << endl;
    }
    
    
    return 0;
}

















