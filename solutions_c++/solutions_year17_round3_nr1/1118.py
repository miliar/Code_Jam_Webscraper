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
    double pi=3.14159265358979323846;
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
        vector<pair<double,double>> r(n);
        for (int i=0;i<n;i++)
        {
            fin>>r[i].first>>r[i].second;
            r[i].second*=(2*pi*r[i].first);
        }

        sort(r.begin(),r.end());
        double mm=0;
        for (int i=k-1;i<n;i++)
        {
            double sur=pi*(r[i].first)*(r[i].first)+r[i].second;
            vector<double> arr;
            for (int j=0; j<i;j++)
                arr.push_back(r[j].second);
            sort(arr.begin(),arr.end(),greater<double>());
            double ss=0;
            for (int j=0;j<k-1;j++)
                ss+=arr[j];
            sur+=ss;
            mm=max(mm,sur);
        }
        fout<< std::fixed<<setprecision(9)<<mm<<endl;
    }
    return 0;
}