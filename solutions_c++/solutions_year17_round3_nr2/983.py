#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

#define mp make_pair
#define f first
#define s second

pair<int,int> v[200];
pair<int,int> w[200];
int n,m;

int main()
{
    int cnt = 0;
    int t,i;
    fin>>t;
    while(t--)
    {
        ++cnt;
        fout<<"Case #"<<cnt<<": ";
        fin>>n>>m;
        for(i=1; i<=n; ++i)
            fin>>v[i].f>>v[i].s;
        for(i=1; i<=m; ++i)
            fin>>w[i].f>>w[i].s;
        if(n<=1 && m<=1)
            fout<<2<<'\n';
        else
        {
            if(n==2)
            {
                if(max(v[1].s,v[2].s)-min(v[1].f,v[2].f)>720 && min(v[1].s,v[2].s)-max(v[1].f,v[2].f)+1440>720)
                    fout<<4<<'\n';
                else
                    fout<<2<<'\n';
            }
            else
                if(max(w[1].s,w[2].s)-min(w[1].f,w[2].f)>720 && min(w[1].s,w[2].s)-max(w[1].f,w[2].f)+1440>720)
                    fout<<4<<'\n';
                else
                    fout<<2<<'\n';
        }
    }
}
