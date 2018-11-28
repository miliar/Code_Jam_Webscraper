#include <bits/stdc++.h>
using namespace std;
 
#define fr(i,a,b) for(int (i)=(int) a;(i)<=(int)(b);++(i))
#define li list<int>
#define ll long long
#define mp make_pair
#define mod 1000000007
#define pb push_back
#define pi pair<double,double>
#define pr printf
#define vi vector<int>
#define vpi vector< pi >
vpi v;
double k[1010],s[1010];
int main() {
	// your code goes here
      std::ios_base::sync_with_stdio(false);
      freopen("input","r",stdin);
      freopen("output","w",stdout);
      int t,tt;
      cin>>t;tt=t;
      while(t--)
      {
            cout<<"Case #"<<tt-t<<": ";
            int n;
            double d,res=mod,r,w,x,y,z,tm;
            cin>>d>>n;
            fr(i,1,n)
            {cin>>k[i]>>s[i];v.pb(mp(k[i],s[i]));}
            v.clear();
            sort(v.begin(),v.end());
            fr(i,1,n)
            {
                  k[i]=v[i-1].first;
                  s[i]=v[i-1].second;
            }
            res=(d-k[n])/s[n];
           /* w=d;x=s[n];y=s[n];
            deque<pair< pair<double,double>,double > > p;
            deque<pair< pair<double,double>,double> > q;
            q.pb(mp(mp(k[n],s[n]),(double)0));
            q.pb(mp(mp(d,s[n]),res));
            for(int i=n-1;i>0;i--)
            {
                  y=k[i];z=s[i];
                  int f=0;
                  if((n-i)%2!=0)
                  {
                  
                       while(!q.empty()&&y<d)
                       {
                             w=q.front().first.first;
                             x=q.front().first.second;
                             tm=q.second;
                             q.pop_front();
                            if(y+z*q.front().second>q.front.first.first)
                            {
                                  f=1;
                                  
                            }
                       }
                        
                  }
                  
            }*/
            fr(i,1,n-1)
            {
                  res=max(res,(d-k[i])/s[i]);
                  
            }
            std::cout << std::fixed;
    std::cout << std::setprecision(8);
            cout<<(d/res);
            cout<<"\n";
      }
      
	return 0;
}

