//
//  main.cpp
//  TidyNumbers
//
//  Created by Sneha Rishi on 4/7/17.
//  Copyright © 2017 Bikram Singh. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool istidy(string str)
{
    for(unsigned long i=0; i<str.length()-1;i++)
    {
        
        if(str[i]>str[i+1])
        {
            return false;
        }
    }
    return true;
}

string convert(string str, unsigned long len)
{
    if(str[len] != '0' || len ==0)
    {
        
        str[len] = ((int)str[len])-1;
        return str;
        
    }
    else
    {
        str[len]='9';
        return convert(str,len-1);
    }
}

int main(int argc, const char * argv[]) {
    
    // insert code here...
    ifstream inFile;
    ofstream outFile;
    inFile.open("large.txt");
    outFile.open("lanswer.txt");
    //Check for error
    if(inFile.fail())
    {
        cerr << "File not found" << endl;
        exit(1);
    }
    string N ="";
    string totalcases;
    
    getline(inFile, totalcases);
    int tc = 0;
    stringstream(totalcases) >> tc;
    
    
    for(int i=0;i<tc;i++)
    {
        outFile << "Case #" << i+1<<": ";
        getline(inFile, N);
            if(N.length()==1)
            {
                outFile<<N<<endl;
            }
            else
            {
                unsigned long j = N.length();
                while(j>0)
                {
                    if(N[0]=='0')
                    {
                        N=N.substr(1,N.length()-1);
                    }
                    bool boolistidy = istidy(N);
                    if(boolistidy == true)
                    {
                        outFile<<N<<endl;
                        break;
                    }
                    else
                    {
                        N[j-1] = '9';
                        if(N[j-2]=='0')
                        {
                            N = convert(N, j-2);
                        }
                        else
                        {
                            N[j-2]= ((int)N[j-2])-1;
                        }
                        j--;
                    }
                }
            }
    }
}

