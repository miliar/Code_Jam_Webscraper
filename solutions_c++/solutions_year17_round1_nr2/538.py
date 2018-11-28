#include <bits/stdc++.h>
using namespace std;
int test;
int n, p;
vector<int> q[59];
int r[59];
int cnt[59];
int minimal(int rr, int qq)
{
    int val=qq*10;
    val/=11;
    if(val*11<10*qq) val++;
    if(val%rr==0) return val/rr;
    return val/rr+1;
}
int maximal(int rr, int qq)
{
    int val=qq*10;
    val/=9;
    if(val*9>10*qq) val--;
    return val/rr;
}
int main()
{
    cin>>test;
    for(int tt=1; tt<=test; tt++)
    {
        int ans=0;
        for(int i=0; i<=50; i++) q[i].clear();
        cin>>n>>p;
        for(int i=1; i<=n; i++)
        {
            cin>>r[i];
        }
        for(int i=1; i<=n; i++)
        {
            cnt[i]=0;
            for(int j=1; j<=p; j++)
            {
                int szam;
                cin>>szam;
                q[i].push_back(szam);
            }
            sort(q[i].begin(), q[i].end());
        }
        while(1)
        {
            int kezdmaxh=1;
            int vegminh=1;
            for(int u=2; u<=n; u++)
            {
                if(minimal(r[kezdmaxh], q[kezdmaxh][cnt[kezdmaxh]])<minimal(r[u], q[u][cnt[u]])) kezdmaxh=u;
                if(maximal(r[vegminh], q[vegminh][cnt[vegminh]])>maximal(r[u], q[u][cnt[u]])) vegminh=u;
            }
            if(minimal(r[kezdmaxh], q[kezdmaxh][cnt[kezdmaxh]])<=maximal(r[vegminh], q[vegminh][cnt[vegminh]]))
            {
                ans++;
                bool dupla=false;
                for(int u=1; u<=n; u++)
                {
                    cnt[u]++;
                    if(cnt[u]==p)
                    {
                        dupla=true;
                        break;
                    }
                }
                if(dupla) break;
            }
            else
            {
                cnt[vegminh]++;
                if(cnt[vegminh]==p) break;
            }
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }

    return 0;
}
