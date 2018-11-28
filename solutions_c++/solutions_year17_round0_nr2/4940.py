#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <sstream>

using namespace std;

typedef unsigned long long ullong;

string stringify(ullong n)
{
    stringstream ss;
    ss << n;
    return ss.str();
}

string trim_zeros(string s)
{
    while(s[0]=='0')
        s.erase(0,1);
    return s;
}

string solve(string n_s,int pos,bool highest)
{
    //cout << "pos: " << pos << endl;
    //cout << "n_s: " << n_s << endl;
    //system("pause");
    string m = "";
    bool first = highest;
    for(char c=(highest?n_s[pos]:'9'); c>='0'; --c)
    {
        //cout << c << endl;
        n_s[pos] = c;
        if((pos==0 || n_s[pos]>=n_s[pos-1]) && pos<n_s.size()-1)
        {
            string res = solve(n_s,pos+1,first);
            if(res!="")
            {
                m = res;
                break;
            }
        }
        if(pos==n_s.size()-1 && n_s[pos]>=n_s[pos-1])
        {
            m = n_s;
            //cout << "FOUND" << endl;
            break;
        }
        else
        {
            m = "";
        }
        first = 0;
    }
    //cout << "m:    " << m << endl;
    return m;
}

string test_case(ullong n)
{
    cout << "----------" << endl;
    cout << n << endl;
    string n_s = stringify(n);
    string m = solve(n_s,0,1);
    string best = trim_zeros(m);
    cout << best << endl;
    return best;
}


int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int n_cases;
    fin >> n_cases;
    for(int h=0; h<n_cases; ++h)
    {
        ullong n;
        fin >> n;
        string maxtid = test_case(n);
        fout << "Case #" << h+1 << ": ";
        fout << maxtid << endl;
    }
}

