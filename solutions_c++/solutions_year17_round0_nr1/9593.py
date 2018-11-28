//
//  main.cpp
//  pancake
//
//  Created by Supanut Dokmaithong on 4/8/2560 BE.
//  Copyright © 2560 Supanut Dokmaithong. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

const vector<string> explode(const string& s, const char& c)
{
    string buff{""};
    vector<string> v;
    
    for(auto n:s)
    {
        if(n != c) buff+=n; else
            if(n == c && buff != "") { v.push_back(buff); buff = ""; }
    }
    if(buff != "") v.push_back(buff);
    
    return v;
}

bool checkResult(string txt)
{
    for(int i=0; i< txt.size(); i++)
    {
        if(txt[i] == '-')
        {
            return false;
        }
    }
    
    return true;
}

string flip(string numCase ,string txt, int count)
{
    int result = 0;
    
    for(int i=0; i<txt.size(); i++)
    {
        if(checkResult(txt))
        {
            //cout << txt + " " + to_string(count)<< "\n";
            string str = "Case #"+ numCase +": " + to_string(result);
            return str;
        }
        else
        {
            if(count+i-1 < txt.size())
            {
                string txtTemp = txt;
                for(int n=i; n<count+i; n++)
                {
                    if(txtTemp[i] == '-')
                    {
                        if(n == i)
                        {
                            result++;
                        }
                        
                        txt[n] = txt[n] == '-' ? '+' : '-';
                    }
                }
            }
            else
            {
                //cout << txt + " " + to_string(count)<< "\n";
                string str = "Case #"+ numCase +": IMPOSSIBLE";
                return str;
            }
        }
    }
    
    //cout << txt + " " + to_string(count)<< "\n";
    string str = "Case #"+ numCase +": IMPOSSIBLE";
    return str;
}

int main(int argc, const char * argv[]) {
    
    //ifstream file("/Users/supanutdokmaithong/Downloads/A-large.in");
    //freopen("output.txt","w",stdin);
    //freopen("/Users/supanutdokmaithong/Downloads/output.txt","w",stdout);
    string s;
    vector<string> listTemp;
    vector<string> list;
    int testCase;

    while (getline(cin, s))
    {
        listTemp.push_back(s);
        //cout << s << "\n";
    }
    
    for(int i=0; i< listTemp.size(); i++)
    {
        if(i == 0)
        {
            testCase = stoi(listTemp[i]);
        }
        else
        {
            list.push_back(listTemp[i]);
        }
    }
    
    for(int i=0; i<list.size(); i++)
    {
        vector<string> v{explode(list[i], ' ')};
        string str = flip(to_string(i+1),v[0], stoi(v[1]));
        cout << str << "\n";

    }
    
    return 0;
}

