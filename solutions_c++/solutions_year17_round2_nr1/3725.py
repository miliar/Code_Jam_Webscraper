#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ll t,l,k=0;
    double d,gandu=0,pagal;
    ifstream input;
    input.open("A-large.in");
    ofstream output;
    output.open("codejammm.txt");
    input>>t;
    l=t;
    for(int suck=0;suck<t;suck++)
    {
        ll n,i;
        gandu=0;
        input>>d>>n;
        double k[n],p,s[n];
        for (i=0;i<n;i++)
        {
            input>>k[i]>>s[i];
            k[i]=d-k[i];
            p=k[i]/s[i];
            if (gandu<p)
            {
                gandu=p;
            }
        }
        pagal=d/gandu;
        output<<"Case #"<<suck+1<<": ";
        output<<fixed<<setprecision(6)<<pagal<<endl;
    }
}
