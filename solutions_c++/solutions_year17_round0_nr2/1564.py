#include <bits/stdc++.h>
using namespace std;

ifstream be("Tidyin.txt");
ofstream ki("Tidyout.txt");

long long t;
vector<long long> megoldas;
const string digits="0123456789";

vector<long long> vectorreverse(vector<long long> x)
{
    vector<long long> kimenet;
    for(long long i=x.size()-1;i>=0;i--) kimenet.push_back(x[i]);
    return kimenet;
}


bool tidy(long long x)
{
    vector<long long> s;
    long long akt=x;
    while(akt>0)
    {
        s.push_back(akt%10);
        akt-=akt%10;
        akt/=10;
    }
    s=vectorreverse(s);
    for(long long i=0;i<s.size()-1;i++)
    {
        if(s[i]>s[i+1]) return false;
    }
    return true;
}


long long vectortolonglong(vector<long long> x)
{
    long long kimenet=0;
    vector<long long> rev=vectorreverse(x);
    for(long long i=0;i<rev.size();i++)
    {
        kimenet+=pow(10,i)*rev[i];
    }
    return kimenet;
}

void process()
{
    long long n;
    be>>n;
    vector<long long> kimenet;
    if(n<10)
    {
        megoldas.push_back(n);
        return;
    }
    vector<long long> s;
    long long akt=n;
    while(akt>0)
    {
        s.push_back(akt%10);
        akt-=akt%10;
        akt/=10;
    }
    s=vectorreverse(s);
    /*for(auto l:s) ki<<l;
    ki<<endl;*/
    akt=0;
    bool mehetmeg=true;
    while(akt<s.size()-1 && mehetmeg)
    {
        if(s[akt]<=s[akt+1]) akt+=1;
        else mehetmeg=false;
    }
    if(akt==s.size()-1)
    {
        megoldas.push_back(vectortolonglong(s));
        return;
    }
    if(s[akt]==1)
    {
        for(long long i=1;i<s.size();i++) kimenet.push_back(9);
        megoldas.push_back(vectortolonglong(kimenet));
        return;
    }
    s[akt]-=1;
    long long visszaakt=akt-1;
    while(visszaakt>=0 && s[visszaakt]>s[visszaakt+1])
    {
        s[visszaakt]-=1;
        visszaakt-=1;
    }
    akt=visszaakt+1;
    for(long long i=0;i<=akt;i++)
    {
        kimenet.push_back(s[i]);
    }
    for(long long i=akt+1;i<s.size();i++)
    {
        kimenet.push_back(9);
    }
    megoldas.push_back(vectortolonglong(kimenet));

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
        if(s!=-INT_MAX) ki<<s<<endl;
        else ki<<"IMPOSSIBLE"<<endl;
        akt+=1;
    }
    return 0;
}
