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

void change(vector<string> &s)
{
    ll i,j,flag=0,pos=-1,com=0,eflag=0;
    char ch,c='?';
    for(j=0;j<s[0].size();j++)
    {
        flag=0;
        pos=-1;
        for(i=0;i<s.size();i++)
        {
            if(s[i][j]!='?')
            {
                c=s[i][j];
                if(flag==0)
                {
                    flag=1;
                    pos=i;
                    ch=c;
                }
            }
            else if(flag==1)
                s[i][j]=c;
        }
        if(flag==1)
        {
            for(i=0;i<pos;i++)
                s[i][j]=ch;
            if(eflag==0)
            {
                eflag=1;
                com=j;
            }
        }
        else if(eflag==1)
        {
            for(i=0;i<s.size();i++)
                s[i][j]=s[i][j-1];
        }
    }
    for(j=com-1;j>=0;j--)
    {
        for(i=0;i<s.size();i++)
            s[i][j]=s[i][j+1];
    }
}

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.out");
	ll t,r,c,i,j,l;
	fin>>t;
	for(l=1;l<=t;l++)
    {
        fin>>r>>c;
        vector<string> s(r);
        for(i=0;i<r;i++)
            fin>>s[i];
        change(s);
        fout<<"Case #"<<l<<":"<<endl;
        for(i=0;i<r;i++)
            fout<<s[i]<<endl;
    }
	fin.close();
    fout.close();
	return 0;
}
