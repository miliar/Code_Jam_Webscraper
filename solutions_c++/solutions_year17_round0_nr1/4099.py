#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin ("q1large.in");
    ofstream fout ("q1large.out");
    int tc;
    fin >> tc;
    for(int t=1;t<=tc;t++)
    {
        string s;
        int k;
        fin >> s >> k;
        int a[s.size()];
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
                a[i]=0;
            else
                a[i]=1;
        }
        int ans=0;
        for(int i=0;i<s.size();i++)
        {
            if(i<=s.size()-k)
            {
                if(a[i]==0)
                {
                    for(int j=0;j<k;j++)
                    {
                        if(a[i+j]==0)
                            a[i+j]=1;
                        else
                            a[i+j]=0;
                    }
                    ans++;
                }
            }
            else
            {
                while(i<s.size())
                {
                    if(a[i]==0)
                    {
                        ans=-1;
                        break;
                    }
                    i++;
                }
            }
        }
        if(ans!=-1)
            fout << "Case #" << t << ": " << ans << endl;
        else
            fout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
