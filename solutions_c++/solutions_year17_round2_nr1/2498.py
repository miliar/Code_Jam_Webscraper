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




int main()
{
    int inputnumber,ii,n,N,J,countcopy;
    long long count;
    long long div;
    long long divs[11];
    string ss;
    int total=0;
    fin>>inputnumber;
    
    
    for (int ii=1;ii<=inputnumber;ii++)
    {
        double d;
        int n;
        fout<<"Case #"<<ii<<": ";
        fin>>d>>n;
        double maxs=DBL_MAX;
        double p[n];
        double s[n];
        for (int i=0;i<n;i++)
        {
            fin>>p[i];
            fin>>s[i];
            maxs=min(maxs,d/((d-p[i])/s[i]));
        }
        fout<<setiosflags(ios::fixed)<<setprecision(6)<<maxs;
        fout<<endl;
    }
    return 0;
}