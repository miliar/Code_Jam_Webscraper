//
//  main.cpp
//  CodeJam2
//
//  Created by Alex Loyko on 4/8/17.
//  Copyright © 2017 Alex Loyko. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream file;
    ofstream out;
    out.open ("output.txt", ios::out);
    file.open ("input.in");
    
    int n;
    string sex;
    int k;
    
    
   
    
    file >> n;
   
    for(int i = 1; i <= n; i++)
    {
        bool impossible = false;
        
        int op = 0;
        
        file >> sex;
        file >> k;
        
        for(int i = 0; i <= sex.length()-k; i++)
        {
            if(sex[i] == '-')
            {
                op++;
                for(int j = i; j <= i+k-1; j++)
                {
                    if(sex[j] == '-')
                        sex[j] = '+';
                    else
                        sex[j] = '-';
                }
            }
        }
        
        for(int i = sex.length()-k+1; i < sex.length(); i++)
        {
            if(sex[i] != '+')
            {
                impossible = true;
                break;
            }
        }
        
        if(!impossible)
            out << "Case #" << i << ": "<< op << endl;
        else
            out << "Case #" << i << ": "<< "IMPOSSIBLE" << endl;

        
    }
    return 0;
}
