#include <bits/stdc++.h>
using namespace std;
int test;
int n, p;
int darab[8];
int main()
{
    cin>>test;
    for(int tt=1; tt<=test; tt++)
    {
        cin>>n;
        for(int u=0; u<8; u++) darab[u]=0;
        cin>>p;
        for(int i=1; i<=n; i++)
        {
            int szam;
            cin>>szam;
            darab[szam%p]++;
        }
        int ans=0;
        ans+=darab[0];
        if(p==2)
        {
            ans+=((darab[1]+1)/2);
        }
        else if(p==3)
        {
            int mini=min(darab[1], darab[2]);
            int maxi=max(darab[1], darab[2]);
            ans+=mini;
            ans+=((maxi-mini+2)/3);
        }
        else if(p==4)
        {
            ans+=(darab[2]/2);
            int mini=min(darab[1], darab[3]);
            int maxi=max(darab[1], darab[3]);
            ans+=mini;
            if(darab[2]%2)
            {
                ans++;
                ans+=((maxi-mini+1)/4);
            }
            else
            {
                ans+=((maxi-mini+3)/4);
            }
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }

    return 0;
}
