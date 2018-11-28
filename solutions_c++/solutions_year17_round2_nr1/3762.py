#include <iostream>
#include <vector>
#include <fstream>
#include <stack>
#include <algorithm>
#include <cstdio>
#include <iomanip>
using namespace std;
int main()
{
    vector<double > v;
    int t,d,n,k,s;
    ofstream out("output.txt");
    ifstream in("input.in");
    in>>t;
    for(int i=0;i<t;i++)
    {
        v.clear();
        in>>d>>n;
        for(int j=0;j<n;j++)
        {
            in>>k>>s;
            v.push_back((d-k)/(double)s);
        }
        sort(v.begin(),v.end());
        out << "Case #" << i+1<< ": ";
        out<< std::fixed<<setprecision(7)<< d/v[v.size()-1] << endl;
    }
}


