#include <bits/stdc++.h>
using namespace std;
 
#define fr(i,a,b) for(int (i)=(int) a;(i)<=(int)(b);++(i))
#define li list<int>
#define ll long long
#define mp make_pair
#define mod 1000000007
#define pb push_back
#define pi pair<int,int>
#define pr printf
#define vi vector<int>
#define vpi vector< pi > 
int main() {
	// your code goes here
      std::ios_base::sync_with_stdio(false);
      int t,tt;
      cin>>t;tt=t;
      while(t--)
      {
            cout<<"Case #"<<tt-t<<": ";
            ll n,k,r1,r2,x=0,y,z;
            cin>>n>>k;
            int l=0,m;
            priority_queue<ll>q;
            q.push(n);
            map<ll,ll> mm;
            mm[n]=1;
            map<ll,ll>ms;
            ms[n]=1;
            while(x<k)
            {
                  y=q.top();
                  q.pop();
                  r1=(y+1)/2;
                  r2=y-r1;
                  r1--;
                 // cout<<r1<<" "<<r2<<" j \n";
                  x+=((ll)mm[y]);
                  if(ms[r1]==0)
                  {
                  q.push(r1);ms[r1]=1;
                  }
                  if(ms[r2]==0)
                  {
                        q.push(r2);
                        ms[r2]=1;
                  }
                  
                  mm[r1]+=mm[y];
                  mm[r2]+=mm[y];
                  ms[y]=0;
            }
            //r1++;r2++;
            cout<<max(r1,r2)<<" "<<min(r1,r2)<<"\n";
            
      }
      
	return 0;
}

