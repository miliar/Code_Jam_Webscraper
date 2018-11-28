#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define repd(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long int
#define mod 1000000007


long long int powe(long long int x, long long int y, long long int m)
{
    if (y == 0)
        return 1;
    long long int p = powe(x, y/2, m) % m;
    p = (p * p) % m;
    return (y%2 == 0)? p : (x * p) % m;
}

int main()
{
    int t=100,ti;
    cin>>t;
    rep(ti,1,t)
    {
        int i=0,j,n,p,a,maxr=1000001,maxv=0,ans=0,r[54],val[54][54],x[54][54],y[54][54],pos[54]={0};
        multiset<int> ms[54];
        vector< pair<int,int> > xy[54];
        cin>>n>>p;
        rep(i,0,n-1)
        {
            cin>>r[i];
            maxr=min(maxr,r[i]);
            pos[i]=0;
        }
        rep(i,0,n-1)
        {
            rep(j,0,p-1)
            {
                cin>>val[i][j];
                maxv=max(maxv,val[i][j]);
                x[i][j]=ceil((double)val[i][j]/r[i]/1.1);
                y[i][j]=floor((double)val[i][j]/r[i]/0.9);
                if(x[i][j]>y[i][j])
                    {
                        x[i][j]=-1;
                        y[i][j]=-1;
                    }
                xy[i].pb({x[i][j],y[i][j]});
                //cout<<x[i][j]<<" "<<y[i][j]<<endl;
            }
        }
        multiset<int>::iterator it;
        rep(i,0,n-1)
            sort(xy[i].begin(),xy[i].end());
        int maxa=ceil((double)maxv/maxr/0.9);
        //cout<<maxa;
        rep(a,1,maxa)
        {
            int flag=0;
            rep(i,0,n-1)
            {
                while(pos[i]<p&&xy[i][pos[i]].fi<=a)
                {
                    ms[i].insert(xy[i][pos[i]].se);
                    pos[i]++;
                }
                if(ms[i].size()!=0){
                it=ms[i].begin();
                while(*(it)<a)
                {
                    ms[i].erase(it);
                    if(ms[i].size()==0)
                        break;
                    it=ms[i].begin();
                }}
                if(ms[i].size()==0)
                    flag=1;
            }
            if(flag==0)
            {
                rep(i,0,n-1)
                {
                    it=ms[i].begin();
                    ms[i].erase(it);
                }
                ans++;
                a--;
            }
//            cout<<ans<<" " ;
        }
        printf("Case #%d: %d\n",ti,ans);

    }
        return 0;
}
