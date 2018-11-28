#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define speed std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define int long long
#define pi 3.141592653
using namespace std;

pair<int, int> p[1001];
bool comp(pair<int,int> x, pair<int, int> y)
{
    return ((x.first>=y.first)&&(x.first*x.second>=y.first*y.second));
}
 main()
{
       ///speed
    freopen("inpu.in","r",stdin);
    freopen("outx.txt","w",stdout);
    int t,c=1,n,k;
    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<c<<": ";
        c++;
        cin>>n>>k;
        for(int i=0; i<n; i++)
        {
            cin>>p[i].first>>p[i].second;
        }
        //for()
        sort(p,p+n);
        double sum=0.0,maxx=-1e10;
        for(int i=1; i<((int)1<<n); i++)
        {
            int cnt=0,lst,sum=0.0;
            for(int j=0; j<n; j++)
            {
               if( (1<<j)&i )
               {
                   //cout<<"lol";
                   cnt++;
                   sum+=double(p[j].first*p[j].second);
                   lst=p[j].first;
               }
            }
            //cout<<sum*2*pi+pi*lst*lst<<endl;
            if(cnt==k)
            {
                maxx=max(maxx,sum*2*pi+pi*lst*lst);
            }

        }

   /*     for(int i=0; i<k; i++)
        {
            cout<<p[i].first<<" "<<p[i].second<<endl;
            sum+=double(p[i].first*p[i].second);
        }
        sum*=2.0;
        sum+=double((p[0].first*p[0].first));
        sum*=pi;*/
        printf("%.7lf\n",maxx);
    }
    return 0;
}
