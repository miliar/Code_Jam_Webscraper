#include<bits/stdc++.h>
using namespace std ;

vector<pair<unsigned long long,unsigned long long> > a,b;
long long dp[1009][1009];
 long long t,n,k,x,y;
unsigned long long ma=0;
double const pi=4*atan(1.0);
bool foo(pair<unsigned long long,unsigned long long> i, pair<unsigned long long,unsigned long long> j)
{
      return i.first>j.first;
}

long long ha(int con,int i)
{
        if(con==k || i==n)return 0;
        if(dp[con][i]!=-1)return(dp[con][i]);
        long long c1=ha(con,i+1);
        long long c2=0;
        if(con==0)c2=a[i].first*a[i].first+(2*a[i].first*a[i].second)+ha(con+1,i+1);
        else c2=(2*a[i].first*a[i].second)+ha(con+1,i+1);
        return(dp[con][i]=max(c1,c2));
}
int main()
{
//        freopen("A-large.in","r",stdin);
//        freopen("out","w",stdout);
        cin>>t;
        for(int o=0;o<t;o++)
        {
                memset(dp,-1,sizeof(dp));
                b.clear();
                a.clear();
                cin>>n>>k;
                for(int i=0;i<n;i++)
                {
                        cin>>x>>y;
                        a.push_back(make_pair(x,y));
//                        b.push_back(make_pair(2*x*y,i));
//                        a.push_back(make_pair((x*x)+(2*x*y),i));
                }
                sort(a.begin(),a.end(),foo);
                //sort(b.begin(),b.end(),foo);
                ma=ha(0,0);
                cout<<"Case #"<<o+1<<": ";
                cout<<fixed<<setprecision(9)<<ma*pi<<endl;
        }
}
