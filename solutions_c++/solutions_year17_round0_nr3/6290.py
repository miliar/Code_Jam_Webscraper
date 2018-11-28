#include <bits/stdc++.h>
using namespace std;
int test;
int db[1000009];
int n, k;
int main()
{
    cin>>test;
    for(int tt=1; tt<=test; tt++)
    {
        cin>>n>>k;
        for(int u=0; u<=1000000; u++) db[u]=0;
        db[n]=1;
        int maxi=n;
        while(k>1)
        {
            while(db[maxi]>0)
            {
                if(maxi%2)
                {
                    db[maxi/2]++;
                    db[maxi/2]++;
                    db[maxi]--;
                }
                else if(maxi>0)
                {
                    db[maxi/2]++;
                    db[(maxi/2)-1]++;
                    db[maxi]--;
                }
                k--;
                if(k==1) break;
            }
            maxi--;
            if(k==1) break;
        }
        for(int u=1000000; u>=0; u--)
        {
            if(db[u]>0)
            {
                if(u%2)
                {
                    cout<<"Case #"<<tt<<": "<<(u/2)<<" "<<(u/2)<<endl;
                }
                else
                {
                    cout<<"Case #"<<tt<<": "<<(u/2)<<" "<<(u/2)-1<<endl;
                }
                break;
            }
        }
    }
    return 0;
}
