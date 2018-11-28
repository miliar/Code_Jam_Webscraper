#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

string MakeTidy(string sn)
{
    auto it = adjacent_find(sn.begin(), sn.end(), [](char a, char b){return a > b;});
    while(it != sn.end())
    {
        (*it)--;
        for_each(it+1, sn.end(), [](char& ch){ch = '9';});
        it = adjacent_find(sn.begin(), sn.end(), [](char a, char b){return a > b;});
    }
    if(sn.front() == '0')
        sn.erase(sn.begin());
    return sn;
}

int main() 
{
    ifstream ifile("input.txt");
    ofstream ofile("output.txt");
    int t;
    ifile >> t;
    for(int i = 1; i <= t; ++i)
    {
        string sn;
        ifile >> sn;
        ofile << "Case #" << i << ": " << MakeTidy(sn) << endl;    
    }
	return 0;
}
