#include<bits/stdc++.h>
#define pb push_back
using namespace std;
int main()
{
    ifstream inp;
    ofstream out;
    inp.open("input.txt");
    out.open("output.txt");
    int T,r,c;
    vector<string> v;
    inp>>T;
    for(int t=1;t<=T;t++)
    {
        inp>>r>>c;
        v.resize(r);
        for(int i=0;i<r;i++)
            inp>>v[i];
        vector<string> A (c);
        for(int i=0;i<c;i++)
        {
            for(int j=0;j<r;j++)
            {
                if(v[j][i]=='?')
                    continue;
                A[i].pb(v[j][i]);
            }
        }
        int i=0,j=0;
        while(i<c)
        {
            //cout<<i<<' '<<j<<endl;
            while(i<c && A[i].size()==0)
                i++;
            if(i==j)
            {
                i++;
                j++;
            }
            else
            {
                if(i<c)
                {
                    A[j]=A[i];
                    for(int k=0;k<r;k++)
                        v[k][j]=v[k][i];
                    j++;
                }
            }
        }
        if(j!=c)
        {
            while(j<c)
            {
                A[j]=A[j-1];
                for(int k=0;k<r;k++)
                    v[k][j]=v[k][j-1];
                j++;
            }
        }
        for(int i=0;i<c;i++)
        {
            int k = 0;
            for(int j=0;j<r;j++)
            {
                if(k<A[i].size() && v[j][i]=='?')
                {
                    v[j][i]=A[i][k];
                }
                else if(k<A[i].size() && v[j][i]!=A[i][k])
                {
                    k++;
                }
            }
        }
        out<<"Case #"<<t<<": "<<endl;
        for(int i=0;i<r;i++)
            out<<v[i]<<endl;
    }
    return 0;
}
