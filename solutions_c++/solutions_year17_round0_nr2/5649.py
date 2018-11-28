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
#include <cstring>
using namespace std;
void deleteZeroes(char* p)
{
    
    while(*p != 0)
    {
        if(*p == '0')
        {
            int a = 0;
            while(*p != 0)
            {
                *p = *(p+1);
                p++;
                a++;
            }
            p -= (a+1);
        }
        p++;
    }
    p--;
}
void tidying(char* S)
{
    int index = 0;
    while(*(S+1) != 0)
    {
        index++;
        if(*S > *(S+1))
        {
            (*S)--;
            S++;
            while(*S != 0)
            {
                *S = '9';
                index++;
                S++;
            }
            S -= (index+1);
            index = 0;
        }
        S++;
    }
    S -= index;
    deleteZeroes(S);
}
int main()
{
    ifstream in;
    ofstream out;
    in.open("/Users/danielhuang/Downloads/B-large.in");
    out.open("/Users/danielhuang/Desktop/Tester/CodeJam/CodeJam #1/CodeJam #1/output.txt");
    int numberofTests;
    in >> numberofTests;
    string* ptr1 = new string[numberofTests];
    for(int i = 0; i < numberofTests; i++)
    {
        string a;
        in >> a;
        char *b = new char[a.length()+1];
        for(int k = 0; k < a.length(); k++)
        {
            b[k]=a[k];
        }
        b[a.length()] = NULL;
        tidying(b);
        ptr1[i] = b;
        delete []b;
        
    }
    for(int j = 0; j < numberofTests; j++)
    {
        out << "Case #" << (j+1) << ": " << ptr1[j]<<endl;
    }
    delete []ptr1;
    in.close();
    out.close();
    return 0;
}