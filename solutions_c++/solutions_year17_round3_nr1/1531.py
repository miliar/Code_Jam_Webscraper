#include <bits/stdc++.h>
using namespace std;

fstream f("A-large.in", ios_base::in);
fstream g("res.out", ios_base::out);

bool comp(const pair<double,double>& p1, const pair<double,double>& p2)
{
    return (p1.first<p2.first);
}

void sol()
{
    vector<pair<double,double>> v;
    int n, k, t1, t2;
    f>>n>>k;

    for(int i=0; i<n; ++i)
    {
        f>>t1;   f>>t2;
        v.push_back(pair<double,double>(t1,t2));
    }
    sort(v.begin(),v.end(),comp);
    double res=0, rec=0;
    for(int i=0; i<n-k+1; ++i)
    {
        res=0;
        res+=(v[n-1-i].first*v[n-1-i].first+2*v[n-1-i].first*v[n-1-i].second);
        vector<double> s;
        for(int j=n-1-i-1; j>=0; --j)
        {
            s.push_back(v[j].first*v[j].second);
        }
        sort(s.begin(),s.end());
        for(int j=0; j<k-1; ++j) res+=(2*s[s.size()-1-j]);
        if(res>rec) rec=res;
    }
    g.precision(8);
    g<<fixed;
    g<<rec*3.14159265358979323846<<endl;
}

int main()
{
    int T;
    f>>T;
    for(int i=1; i<=T; ++i)
    {
        g<<"Case #"<<i<<": ";
        sol();
    }
    return 0;
}
