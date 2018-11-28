#include<iostream>
#include<iomanip>
#include<fstream>
#define ll long long int
using namespace std;
int main()
{
    fstream fin;
    fin.open("A-large (1).in");
    ofstream fout;
    fout.open("BLL.out");
    ios_base::sync_with_stdio(false);
    int t;
    fin>>t;
    for(int i=1;i<=t;i++)
    {
        ll d,n;
        fin>>d>>n;
        double _max = -1;
        fout<<fixed<<showpoint<<setprecision(10);
        while(n--)
        {
            ll p,v;
            fin>>p>>v;
            double t = (double)(d-p)/(double)v;
            _max = max(_max,t);
        }
        fout<<"Case #"<<i<<": "<<d/_max<<endl;
    }
    return 0;
}
