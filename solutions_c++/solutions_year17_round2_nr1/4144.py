#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream in; in.open("A-small-attempt3.in");
    ofstream out; out.open("out2.txt");

    int T,N,D; in >> T;
    for(int t = 1 ; t <= T ; t++)
    {
        in >> D >> N;
        int k,s,mn=1e5,ind; bool f=1;
        vector < pair<int,int> > p(N);
        for(int i = 0 ; i < N ; i++)
        {
            in >> k >> s;
            p[i]=make_pair(k,s);
        }
        sort(p.begin(),p.end());

        for(int i = 0 ; i < N ; i++)
        {
            if(f && p[i].second<mn){ind=i; mn=p[i].second;}
            else f=0;
        }
        long double mx=0.0;
        for(int i = 0 ; i <= ind ; i++)
        {
            long double hrs = (long double)(D-p[i].first)/p[i].second;
            mx=max(mx,hrs);
        }
        out << "Case #" << t << ": " << fixed << setprecision(8) << D/mx << "\n";
    }
    return 0;
}
