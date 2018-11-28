#include <bits/stdc++.h>

using namespace std;

string gr[30];
int n,m;

bool ok(int x)
{
    int i;
    bool okk=0;
    for(i=0;i<gr[x].size();i++)
        okk|=(gr[x][i]!='?');
    return okk;
}

bool solve(int x)
{
    int i;
    bool okk=0;
    for(i=0;i<gr[x].size();i++)
        okk|=(gr[x][i]!='?');
    if(!okk)
        return okk;
    char last='?';
    for(i=0;i<gr[x].size();i++)
    {
        if(gr[x][i]=='?')
            gr[x][i]=last;
        else
            last=gr[x][i];
    }
    for(i=gr[x].size()-1;i>=0;i--)
    {
        if(gr[x][i]=='?')
            gr[x][i]=last;
        else
            last=gr[x][i];
    }
    return okk;
}

int main()
{
    freopen("A_large.in","r",stdin); freopen("A_large.out","w",stdout);
    int t;
    cin >> t;
    int tc;
    for(tc=1;tc<=t;tc++)
    {
        cin >> n >> m;
        int i;
        for(i=0;i<n;i++)
            cin >> gr[i];
        int fr=-1;
        for(i=0;i<n;i++)
        {
            bool x=solve(i);
            if(x&&fr==-1)
                fr=i;
        }
        for(i=0;i<fr;i++)
            gr[i]=gr[fr];
        for(i=fr;i<n;i++)
        {
            if(ok(i))
                fr=i;
            else
                gr[i]=gr[fr];
        }
        cout << "Case #" << tc << ":\n";
        for(i=0;i<n;i++)
            cout << gr[i] << endl;
    }
}
