//
//  main.cpp
//  jamW1Q2
//
//  Created by Riley Desrochers on 2017-04-08.
//  Copyright © 2017 Riley Desrochers. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

string notGreater(string in,int pos)
{
    map<char,char> table;
    table['9']='8';
    table['8']='7';
    table['7']='6';
    table['6']='5';
    table['5']='4';
    table['4']='3';
    table['3']='2';
    table['2']='1';
    table['1']='0';
    in[pos]=table[in[pos]];
    for(int x=pos+1;x<in.length();x++)
    {
        in[x]='9';
    }
    if(pos!=0)
    {
        if(in[pos-1]>in[pos])
        {
            in=notGreater(in,pos-1);
        }
    }
    return in;
}

int main() {
    ifstream fin;
    map<char,char> table;
    int times;
    string in;
    fin.open("/Users/rileydesrochers/Desktop/jam/input.txt");
    if(fin.is_open())
    {
        fin>>times;
        for(int x=0;x<times;x++)
        {
            fin>>in;
            for(int y=0;y<in.length()-1;y++)
            {
                if(in[y]>in[y+1])
                {
                    in=notGreater(in,y);
                    while(in[0]=='0')
                    {
                        in=in.substr(1,in.length()-1);
                    }
                }
            }
            cout<<"Case #"<<x+1<<": ";
            cout<<in<<endl;
            
        }
    }
    fin.close();
    return 0;
}
