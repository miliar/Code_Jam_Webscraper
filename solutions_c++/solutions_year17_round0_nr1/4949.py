#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

void display(vector<bool> cakes)
{
    //for(int i=0; i<cakes.size(); ++i)
        //cout << (cakes[i]?'+':'-');
    //cout << endl;
}
vector<bool> decode(string cakes_str)
{
    vector<bool> cakes (cakes_str.size());
    for(int i=0; i<cakes_str.size(); ++i)
    if(cakes_str[i]=='+')
    cakes[i] = 1;
    else if(cakes_str[i]=='-')
    cakes[i] = 0;
    else
    cout << "Invalid input!!!" << endl;
    return cakes;
}

void flip(vector<bool> & cakes, int k, int first)
{
    if(first<=cakes.size()-k)
    {
        for(int i=first; i<first+k; ++i)
            cakes[i] = !cakes[i];
    }
    else
    {
        //cout << "error!" << endl;
    }
}

int test_case(vector<bool> cakes, int k)
{
    //cout << "------------" << endl;
    //cout << k << " ";
    display(cakes);
    //cout << endl;

    int flips = 0;

    for(int i=0; i<cakes.size()-k+1; ++i)
    {
        if(cakes[i]==0)
        {
            flip(cakes,k,i);
            ++flips;
        }
        //cout << i << "\t";
        display(cakes);
    }
    for(int i=cakes.size()-k+1; i<cakes.size(); ++i)
    {
        if(cakes[i]==0)
            flips=-1;
    }
    //cout << "Flips: " << flips << endl;
    return flips;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int n_cases;
    fin >> n_cases;
    for(int h=0; h<n_cases; ++h)
    {
        string s;
        fin >> s;
        vector<bool> cakes = decode(s);
        int k;
        fin >> k;
        int flips = test_case(cakes,k);
        fout << "Case #" << h+1 << ": ";
        if(flips!=-1)
            fout << flips << endl;
        else
            fout << "IMPOSSIBLE" << endl;
    }
}
