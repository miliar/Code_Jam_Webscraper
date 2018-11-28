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
double pii=3.14159265358979;;
vpi v;
vi w;
bool cmp(pi a,pi b)
{
      return a.first>b.first;
}
double cal(double r)
{
      return r*r;
}
double cal2(double h,double r)
{
      return (double)2.00*r*h;
}
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
            int n,k;
            double x,h;
            cin>>n>>k;
            v.clear();
            fr(i,0,n-1)
            {
                  cin>>x>>h;
                  v.pb(mp(x,h));
            }
            sort(v.begin(),v.end(),cmp);
            double res=0.0000,e,f,g,r;
            priority_queue< pi, vector <pi> , greater<pi> > pq;
            double a[n+10][n+10];
            fr(i,0,n-k)
            {
                  r=0.00;
                  if(k<=2) continue;
                  while(!pq.empty()) pq.pop();
            fr(j,i+1,i+k-2) {pq.push(mp(v[j].second*v[j].first,v[j].first));
                  r+=cal2(v[j].second,v[j].first);
                        
                  }
                  
                  a[i][i+k-1]=r;
                  fr(j,i+k-1,n-2)
                  {
                       
                       r+=cal2(v[j].second,v[j].first);
                       pq.push(mp(v[j].second*v[j].first,v[j].first));
                       r-=((double)2.00*pq.top().first) ;
                      // cout<<pq.top().first<<" ";
                       pq.pop();
                       a[i][j+1]=r;
                  }
            }
           // fr(i,0,n-1) cout<<v[i].second<<" ";
            fr(i,0,n-k)
            {
                  if(k==1)
                  {
                  res=max(res,cal(v[i].first)+cal2(v[i].second,v[i].first));
                  continue;
                  }
                  fr(j,i+k-1,n-1)
                  {
                        r=cal(v[i].first);//cout<<r<<" "
                       // r-=cal(v[j].first);
                        r+=cal2(v[i].second,v[i].first);
                        r+=cal2(v[j].second,v[j].first);
                        if(k>2)
                        r+=a[i][j];
                        res=max(r,res);
                  }
            }
            res=res*pii;
            cout.precision(50);
            
           cout<<res<<"\n"; 
      }
	return 0;
}

