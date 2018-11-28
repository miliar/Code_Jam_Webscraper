#include <bits/stdc++.h>
using namespace std;

fstream f("A-large.in", ios_base::in);
fstream g("res.out", ios_base::out);

void sol()
{
    int D, N;
    f>>D>>N;
    vector<int> k, s;
    for(int i=0; i<N; ++i)
    {
        int k1, s1;
        f>>k1>>s1;
        k.push_back(k1); s.push_back(s1);
    }
    vector<double> v2;
    for(int i=0; i<N; ++i)
    {
        v2.push_back(double(D-k[i])/double(s[i]));
    }
    double m=*max_element(v2.begin(),v2.end());
    g<<double(D)/m<<endl;
}

int main()
{
    g<<fixed;
    int T;
    f>>T;
    for(int i=1; i<=T; ++i)
    {
        g<<"Case #"<<i<<": ";
        sol();
    }
    return 0;
}
