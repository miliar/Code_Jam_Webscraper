#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
#define present(m,v) (m.find(v)!=m.end())
#define INF 1e18
#define mod 1000000007
#define lim 1000001
#define sz(a) int(a.size())
#define all(x) (x).begin(), (x).end()
#define rep(i,n) for(i=0;i<n;i++)
#define forn(i,a,b) for(i=a;i<b;i++)

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.out");
	ll t,k,i,l,j,flip;
	fin>>t;
	for(l=1;l<=t;l++)
    {
        flip=0;
        string s;
        fin>>s>>k;
        fout<<"Case #"<<l<<": ";
        for(i=s.size()-1;i>k-2;i--)
        {
            if(s[i]=='+')
                continue;
            for(j=i;j>i-k;j--)
            {
                if(s[j]=='+')
                    s[j]='-';
                else s[j]='+';
            }
            flip++;
        }
        for(i=k-2;i>=0;i--)
            if(s[i]=='-')
                break;
        if(i==-1)
            fout<<flip<<endl;
        else fout<<"IMPOSSIBLE"<<endl;
    }
	fin.close();
    fout.close();
	return 0;
}
