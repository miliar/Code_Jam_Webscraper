#include <bits/stdc++.h>
using namespace std;

#define min(a,b) ((a<b) ? (a) : (b))
#define max(a,b) ((a>b) ? (a) : (b))
#define ll long long
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORL(i,n) for(long long i=0;i<n;i++)
#define MOD 1000000007
#define PI 3.141592653589
#define fastio ios_base::sync_with_stdio(false); cin.tie(0);
#define pb push_back

int main()
{
    fastio
    freopen("input_2.txt", "r", stdin);
    freopen("output_2.txt", "w", stdout);

    int test;
   	int ans=0;
   	string s;
   	int i,j,k,n,p,l;
    cin>>test;
    bool check;
    vector<int> r;
    vector< vector<int> > q;
    //vector< map<int,int> > q1;
    vector <int> iter;
    for(int t=1;t<=test;t++)
    {
        cin>>n>>p;
        q.clear();
        iter.clear();
        r.clear();
        FOR(i,n)
        {
          cin>>l;
          r.pb(l);
          iter.pb(0);
        }
        FOR(i,n)
        {
          vector<int> m;
          FOR(j,p)
          {
            cin>>l;
            m.pb(l);
          }
          sort(m.begin(),m.end());
          q.pb(m);
       
        }

        int ans=0;
        int max_it =0;
        int maxl,minl;
        while(max_it<p)
        {
          minl=0;
          maxl=INT_MAX;
          FOR(i,n)
          {
            int x=r[i];
            int y=q[i][iter[i]];
            double x1=(double)y/(double)x;
            double y1 = x1/0.9;
            x1/=1.1;
            minl = max(minl,ceil(x1));
            maxl = min(maxl,(int)y1);


          }
          if(minl<=maxl)
          {
            ans++;
            FOR(i,n)
              iter[i]++;
            max_it++;
            continue;
          }
          FOR(i,n)
          {

            int x=r[i];
            int y=q[i][iter[i]];
            double x1=(double)y/(double)x;
            double y1 = x1/0.9;
            x1/=1.1;
            while((int)y1 < minl && max_it<p)
            {
              iter[i]++;
              max_it = max(max_it , iter[i]);
              x=r[i];
              y=q[i][iter[i]];
              x1=(double)y/(double)x;
              y1 = x1/0.9;
              x1/=1.1;
            }

          }


        }
        
        

        cout<<"Case #"<<t<<": "<<ans<<endl;
       
    }
    return 0;
}

