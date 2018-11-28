#include <bits/stdc++.h>
using namespace std;

ifstream be("Bathroomin.txt");
ofstream ki("Bathroomout.txt");

long long t;
vector<pair<long long, long long> > megoldas;

void process()
{
    long long n,k;
    be>>n>>k;
    if(n==k)
    {
        megoldas.push_back({0,0});
        return;
    }
    long long eddig=0;
    long long akttwopow=1;
    long long minfed=n;
    while(eddig+akttwopow<k)
    {
        eddig+=akttwopow;
        minfed=(minfed-1)/2;
        akttwopow*=2;
    }
    long long l=n-akttwopow*(minfed+1)+1;
    long long hossz;
    if(eddig+l>=k) hossz=minfed+1;
    else hossz=minfed;
    //cout<<eddig<<" "<<akttwopow<<" "<<minfed<<" "<<l<<" "<<hossz<<endl;
    if(hossz%2==1)
    {
        megoldas.push_back({(hossz-1)/2,(hossz-1)/2});
    }
    else
    {
        megoldas.push_back({hossz/2,hossz/2-1});
    }
}



int main()
{
    ios_base::sync_with_stdio(false);
    be>>t;
    for(long long i=1;i<=t;i++)
    {
        process();
    }
    long long akt=1;
    for(auto s:megoldas)
    {
        ki<<"Case #"<<akt<<": ";
        ki<<s.first<<" "<<s.second<<endl;
        akt+=1;
    }
    return 0;
}
