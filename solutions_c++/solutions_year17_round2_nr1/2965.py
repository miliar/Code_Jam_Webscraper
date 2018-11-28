#include <bits/stdc++.h>

using namespace std;
vector<pair<int,int> > vec;
int main()
{
    freopen("linput.in","r",stdin);
    freopen("output.out","w",stdout);
    int test;cin>>test;
    for(int tt=1;tt<=test;tt++)
    {
        vec.clear();
        int dest;cin>>dest;
        int n;cin>>n;
        for(int i=0;i<n;i++)
        {
            int d,s;
            cin>>d>>s;
            vec.push_back({d,s});
        }
        sort(vec.begin(),vec.end());
        double maxt=-1;
        for(int i=vec.size()-1;i>=0;i--)
        {
            int a=vec[i].first,b=vec[i].second;
            a=dest-a;
            double c=(double)a/(1.*b);
            if(c>maxt)maxt=c;
        }
        cout<<"Case #"<<tt<<": ";
        double ans=(double)dest/(1.*maxt);
        cout<<fixed<<setprecision(10)<<ans<<endl;
    }
    return 0;
}
