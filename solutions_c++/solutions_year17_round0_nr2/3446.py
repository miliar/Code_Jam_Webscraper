#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ifstream infile;
    ofstream outfile;
    infile.open("B-large.in");
    outfile.open("out.txt");

    ll t;
    infile>>t;

    for(int cas=1;cas<=t;cas++)
    {
        ll n,nc;
        infile>>n;
        nc =n;
        vector <int> v;
        while(nc)
        {
            v.push_back(nc%10);
            nc/=10;
        }
        reverse(v.begin(),v.end());
        int i= 0;
        while(i+1<v.size() && v[i+1]>=v[i])
            i++;
        if(i+1!=v.size())
        {
            while(i-1>=0 && v[i-1]==v[i])
                i--;
            v[i]--;
            i++;
            while(i<v.size())
                {
                    v[i]=9;
                    i++;
                }
        }
        outfile<<"Case #"<<cas<<": ";
        if(v[0]!=0)
            outfile<<v[0];
        for(i=1;i<v.size();i++)
            outfile<<v[i];
        outfile<<endl;
    }


}
