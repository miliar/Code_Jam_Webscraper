#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

ifstream in("data.in");
ofstream out("data.out");

int main()
{
    long int t;
    in>>t;
    for(int i=1; i<=t; i++)
    {
        long double d,horses;
        long double maxi=-1;
        in>>d>>horses;
        for(int j=1; j<=horses; j++)
        {
            long double k,speed;
            in>>k>>speed;
            long double answ=d-k;
            answ=answ/speed;
            if(answ>maxi)
                maxi=answ;
        }

        out<<"Case #"<<i<<":"<<" ";
        long double tout;
        tout=d/maxi;
        out<<setprecision(6)<<fixed<<tout<<'\n';
    }
}
