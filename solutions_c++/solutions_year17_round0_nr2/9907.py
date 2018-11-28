//
//  main.cpp
//  CodeJam
//
//  Created by Alex Loyko on 4/7/17.
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
    int p;
    string number;
    
    file >> n;
    
    cout << n;
    bool done;
    for(int i = 1; i <= n; i++)
    {
        file >> number;
        
            for(int j = 0; j < number.length() - 1; j++)
            {
                if(number[j] <= number[j+1])
                    continue;
                    //if(j == number.length()-2)
                    //{
                     //   out << "Case #" << i << ": "<< number << endl;
                     //   done = true;
                    //}
                else
                {
                    if(j != 0 && number[j-1] == number[j])
                        {
                            for(int k = j; ; k--)
                                if(number[k] == number[k-1])
                                    continue;
                                else
                                {
                                    number[p] -= 1;
                                    
                                    for(int m = p+1; m < number.length(); m++)
                                        number[m] = '9';
                                    for(int m = 0; m < number.length();m++)
                                        if(number[m] == '0')
                                            number = number.substr(m+1, number.length()-1);

                                    p = k;
                                    break;
                                }
                        }
                    else
                    {
                        number[j] -= 1;
                        
                        for(int m = j+1; m < number.length(); m++)
                            number[m] = '9';
                        for(int m = 0; m < number.length();m++)
                            if(number[m] == '0')
                                number = number.substr(m+1, number.length()-1);
                    }
                    
                }
            }
        
          out << "Case #" << i << ": "<< number << endl;
        
    }
    return 0;
}
