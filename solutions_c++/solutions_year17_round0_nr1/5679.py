//
//  main.cpp
//  CodeJam #1
//
//  Created by Daniel Huang on 4/7/17.
//  Copyright (c) 2017 Daniel Huang. All rights reserved.
//
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
int flipcake(string S, int K)
{
    int flips = 0;
    for(int i = 0; i <= S.length()- K; i++)
    {
        if(S[i] == '-')
        {
            for(int j = 0; j < K; j++)
            {
                if(S[i+j] == '-')
                {
                    S[i+j] = '+';
                }
                else
                {
                    S[i+j] = '-';
                }
            }
            flips++;
        }
        
    }
    for(int a = 0; a < S.length(); a++)
    {
        if(S[a] == '-')
            flips = -1;
    }
    return flips;
}
int main()
{
    ifstream in;
    ofstream out;
    in.open("/Users/danielhuang/Downloads/A-large.in");
    out.open("/Users/danielhuang/Desktop/Tester/CodeJam/CodeJam #1/CodeJam #1/output.txt");
    int numberofTests;
    in >> numberofTests;
    cerr << numberofTests;
    int* ptr1 = new int[numberofTests];
    for(int i = 0; i < numberofTests; i++)
    {
        string a;
        in >> a;
        int b;
        in >> b;
        ptr1[i] = flipcake(a,b);
        
    }
    for(int i = 0; i < numberofTests; i++)
    {
        if(ptr1[i] < 0)
        {
            out<< "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
        }
        else
        {
            out<< "Case #" << (i+1) <<": " << ptr1[i] << endl;
        }
    }
    delete ptr1;
    in.close();
    out.close();
    return 0;
}
