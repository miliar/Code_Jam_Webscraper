#include <bits/stdc++.h>
using namespace std;

ifstream be ("Steed 2 Cruise Controlin.txt");
ofstream ki ("Steed 2 Cruise Controlout.txt");

long long t;
vector<double> megoldas;

void process()
{
    long long d,n;
    be>>d>>n;
    double mini=1000000000000000000;
    for(long long i=1;i<=n;i++)
    {
        long long s, k;
        be>>k>>s;
        mini=min(mini,(double(d)*double(s))/double(double(d)-double(k)));
    }
    megoldas.push_back(mini);
}

int main()
{
    ios_base::sync_with_stdio(false);
    be>>t;
    for(long long i=1;i<=t;i++) process();
    for(long long i=0;i<megoldas.size();i++)
    {
        ki<<setprecision(7)<<fixed<<"Case #"<<i+1<<": "<<megoldas[i]<<endl;
    }
    return 0;
}
