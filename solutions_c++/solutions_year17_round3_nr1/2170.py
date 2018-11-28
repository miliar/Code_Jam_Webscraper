#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long int ULLI;
typedef long long int LLI;
typedef long double LD;

bool orderFun (pair<LD,LD> i, pair<LD,LD> j) { return (i.first>j.first); }
LD brute(vector<pair<LD,LD> >& panc, int k, int n, int pos)
{
    LD sup_max = 0;
    LD s = 2*M_PI*panc[pos].first*panc[pos].second; //Sl
    if(k<=1)
        return s + M_PI*pow(panc[pos].first,2);
    for(int i=pos+1; i<n; i++)
    {
        LD tmp = s;
        tmp += brute(panc, k-1, n, i) + M_PI*pow(panc[pos].first,2) - M_PI*pow(panc[i].first,2);
        if(tmp > sup_max)
            sup_max = tmp;
    }
    return sup_max;
}
int main(int argc, char** argv)
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
    ULLI t;
    cin >> t;
    for(int c=0; c<t; c++)
    {
        vector<pair<LD,LD> > panc;
        ULLI n, k;
        cin >> n >> k;
        for(int i=0; i<n; i++)
        {
            pair<LD,LD> data;
            cin >> data.first >> data.second;
            panc.push_back(data);
        }
        sort(panc.begin(), panc.end(), orderFun);
        for(int j=0;j<panc.size(); j++)
            cerr << panc[j].first << "  " <<panc[j].second << endl;
        LD sup_max = 0;
        for(int i=0; i<n-k+1; i++)
        {
            LD tmp = brute(panc, k, n, i);
            if(tmp>sup_max)
                sup_max = tmp;
        }
        cout.precision(9);
        cout << "Case #" << c+1 << ": " << fixed << sup_max << endl;
    }
    return 0;
}
