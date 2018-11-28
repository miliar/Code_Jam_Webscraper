#include<bits/stdc++.h>
#define ll long long
#define vll vector<ll>
#define mll map<ll,ll>
#define sll set<ll>
#define fo(i,n) for(i=0;i<n;i++)
#define eps 1e-2
using namespace std;

ll p,r[2],q[2][10];
map<pair<ll,ll>,ll > map1;

ll calc(ll mask1,ll mask2,ll tot)
{
    //cout<<mask1<<" "<<mask2<<" "<<tot<<endl;
    if(mask1==tot)
        return 0;

    if(map1.find(make_pair(mask1,mask2))!=map1.end())
        return map1[make_pair(mask1,mask2)];

    ll p1=1,ma=0,p2=1;

    for(ll i=0;i<p;i++)
    {
        p2=1;
        for(ll j=0;j<p;j++)
        {
            if(!(mask1 & p1) && !(mask2 & p2))
            {
                ll c=q[0][i]/(1.1*r[0])-10;
                int flag=0;
                while((c-1)*0.9*r[0]<=q[0][i])
                {
                    //cout<<c*0.9*r[0]<<" "<<q[0][i]<<" "<<c*1.1*r[0]<<" "<<c*0.9*r[1]<<" "<<q[1][j]<<" "<<c*1.1*r[1]<<endl;
                    if(c*0.9*r[0]-eps<=q[0][i] && q[0][i]<=c*1.1*r[0]+eps && c*0.9*r[1]-eps<=q[1][j] && q[1][j]<=c*1.1*r[1]+eps)
                    {
                        ma=max(ma,calc(mask1|p1,mask2|p2,tot)+1);
                        flag=1;
                        break;
                    }
                    c++;
                }
                if(flag==0)
                    ma=max(ma,calc(mask1|p1,mask2|p2,tot));
            }
            p2<<=1;
        }
        p1<<=1;
    }

    map1[make_pair(mask1,mask2)]=ma;
    return ma;
}

int main()
{
    ios::sync_with_stdio(false);
    //freopen("000.txt","r",stdin);
    freopen("0bs.in","r",stdin);
    //freopen("0bl.in","r",stdin);
    freopen("02bs2.txt","w",stdout);
    //freopen("02bl.txt","w",stdout);

    ll n,i,j,k,t,l;

    cin>>t;

    for(l=1;l<=t;l++)
    {
        map1.clear();
        cin>>n>>p;

        fo(i,n)
            cin>>r[i];

        fo(i,n)
        {
            fo(j,p)
            {
                cin>>q[i][j];
            }
        }

        ll ans=0;
        cout<<"Case #"<<l<<": ";
        if(n==1)
        {
            fo(i,p)
            {
                ll c=q[0][i]/(1.1*r[0])-10;
                while((c-1)*0.9*r[0]<=q[0][i])
                {
                    if(c*0.9*r[0]-eps<=q[0][i] && q[0][i]<=c*1.1*r[0]+eps)
                    {
                        ans++;
                        break;
                    }
                    c++;
                }
            }
            cout<<ans;
        }
        else
            cout<<calc(0,0,pow(2,p)-1);
        cout<<endl;
    }

    return 0;
}
