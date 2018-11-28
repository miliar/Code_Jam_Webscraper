#include<bits/stdc++.h>



using namespace std;

int cnt =0;
string str;


int main()
{
   freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

    int d =0;

    int k,t;
    cin>>t;
    while(t--)
    {
        ++cnt;
      long long n,k;
      cin>>n>>k;
      priority_queue<pair<int,int> > pq;
      pq.push({n,1});


      while(1)
      {
          long long tp = pq.top().first;
          long long q = pq.top().second;
          k-=q;
          if(k<=0)
          {
              long long x = tp;
               if(x&1)
               cout<<"Case #"<<cnt<<": "<<x/2<<" "<<x/2<<"\n";
                 else
                cout<<"Case #"<<cnt<<": "<<(x/2)<<" "<<(x/2)-1<<"\n";
                break;
          }


          pq.pop();

          if(tp&1)
          {

              pq.push({(tp/2),2*q});
          }
          else
          {
            pq.push({(tp/2),q});
            pq.push({((tp/2)-1),q});
          }
      }






    }
}


