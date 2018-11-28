#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin ("q3small2.in");
    ofstream fout ("q3small2.out");
    int tc;
    fin >> tc;
    for(int t=1;t<=tc;t++)
    {
        int n,k;
        fin >> n >> k;
        int lastl,lastr;
        map<long long int,long long int>m;
        int pres=n;
        m[pres]=1;
        for(int i=0;i<k;i++)
        {
            lastl=pres-1;
            lastr=lastl-lastl/2;
            lastl=lastl/2;
            if(!m[lastl])
                m[lastl]=1;
            else
                m[lastl]++;
            if(!m[lastr])
                m[lastr]=1;
            else
                m[lastr]++;
            m[pres]--;
            if(m[pres] && m[pres]>0)
                pres=pres;
            else
            {
                if(m[pres-1]&&m[pres-1]>0)
                {
                    pres=pres-1;
                }
                else
                {
                    if(m[max(lastl,lastr)+1] && m[max(lastl,lastr)]>0)
                        pres=max(lastl,lastr)+1;
                    else
                        pres=max(lastl,lastr);
                }
            }
            if(lastl==0 && lastr==0)
            {
                break;
            }
        }
        fout <<"Case #" << t << ": " << max(lastl,lastr) << " " << min(lastl,lastr) << endl;
    }
    return 0;
}
