#include <bits/stdc++.h>

using namespace std;
ifstream f("in.in");
ofstream g("inn.out");
int T;

void solve(int cases)
{
    int v[11110],nr=0,cnt=0,k;
    string s;
    f>>s>>k;
    for(auto it:s)
        if(it=='+') v[++nr]=1;
        else v[++nr]=0;

    for(int i=1; i<=nr; i++)
        if(v[i]==0 )
        {
            if( i+k-1<=nr)
            {
                cnt++;
                for(int j=i; j<=i+k-1; j++) v[j]=1-v[j];
            }

            else
            {
                g<<"Case #"<<cases<<": "<<"IMPOSSIBLE\n";
                return;
            }
        }
    g<<"Case #"<<cases<<": "<<cnt<<'\n';
}

int main()
{
    f>>T;
    for(int i=1; i<=T; i++)
    {
        solve(i);
    }
}
