#include <iostream>
#include <fstream>
#include <cfloat>
#include <math.h>
#include <vector>
#include <limits>
#include <iomanip>
using namespace std;

bool getanswer;
int fretraget[26];
int currentfretraget[26];
bool toobig;
int fre[10][26]={0};
string letter[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
ifstream fin("input");
ofstream fout("output");
char firstc;



int main()
{
    int inputnumber,ii,n,N,J,countcopy;
    long long count;
    long long div;
    long long divs[11];
    string ss;
    int total=0;
    fin>>inputnumber;
    double u;
    int k;
    for (int ii=1;ii<=inputnumber;ii++)
    {
        
        fout<<"Case #"<<ii<<": ";
        
        fin>>n>>k;
        fin>>u;
        vector<double> v(n);
        for (int i=0;i<n;i++)
        {
            fin>>v[i];            
        }
        vector<double> vv;
        sort(v.begin(),v.end(),greater<double>());
        for (int i=0;i<k;i++)
        {
            vv.push_back(v[i]);
        }
        sort(vv.begin(),vv.end());
        vector<double> diff(k);
        double fo=0;
        for (int i=0;i<k-1;i++)
        {            
            diff[i]=(vv[i+1]-vv[i])*(i+1)+fo;
            fo=diff[i];
        }

        diff[k-1]=fo+(1-vv[k-1])*k;
        if (u>=diff[k-1])
        {
            fout<<"1.000000"<<endl;
            continue;
        }
        int ic=0;
        while (u>diff[ic])
            ic++;
        int j=ic;
        double level;
        if (j==0)
            level=vv[0]+u;    
        else
            level=vv[j]+ (u-(diff[j-1]))/(j+1.0);
        cout<<vv[0]<<endl;
        cout<<vv[1]<<endl;
        cout<<level<<endl;
        cout<<j<<endl;
        for (int i=0; i<=j;i++)
            vv[i]=level;
        double xx=1;
        for (int i=0;i<k; i++)
            xx*=vv[i];
        fout<< std::fixed<<setprecision(6)<<xx<<endl;
    }
    return 0;
}