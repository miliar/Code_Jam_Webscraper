#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        string k;
        long long w=0, q;
        cin>>k;
        for(int i=0;i<k.size()-1;i++)
        {

            if(k[i]>k[i+1])
            {
                k[i]--;
                q=i;
                while(q>0 and k[q]<k[q-1])
                {
                    k[q-1]--;
                    q--;
                }
                q++;
                while(q<k.size())
                {
                    k[q]='9';
                    q++;
                }
                i=0;
            }
        }
        for(int i=0;i<k.size();i++)
            w=w*10+(k[i]-48);
        cout<<"Case #"<<z<<": "<<w<<"\n";
    }
    return 0;
}
