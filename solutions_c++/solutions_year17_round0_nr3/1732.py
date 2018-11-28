#include <bits/stdc++.h>
#define ll long long
#define mp make_pair
#define inf 1000000000
#define pb push_back
using namespace std;
string str;
map<ll,ll> sum;
int main()
{
   // freopen("txtin.txt","r",stdin);
    //freopen("txtout2.txt","w",stdout);
    ll n,m,i,j,k,l;
    int t;
    cin>>t;
    //t=100;
    for(int test=1;test<=t;test++)
    {
        sum.clear();
        cout<<"Case #"<<test<<": ";
        cin>>n>>k;
      //  n=1000000000000000000;
       // k=100000;
        if(k==n)
        {
            cout<<"0 0\n";
            continue;
        }
        /*class prioritize{public: bool operator ()(int &p1 ,int &p2){
            return p1>p2;
            };*/
        //priority_queue<int,vector<int> , prioritize> pq;
        priority_queue<ll> pq;
        pq.push(n);
        k--;
        sum[n]=1;
        while(!pq.empty())
        {
            ll ind=pq.top();
            //cout<<ind<<" ";
            if(sum[ind]>k)
            {
                break;
            }
            k-=sum[ind];
            pq.pop();
            m=ind/2;
            if(m!=0){
                    if(sum[m]==0)
            pq.push(m);
                sum[m]+=sum[ind];
            //sum[m]++;
            m=(ind-1)/2;
            if(sum[m]==0)
            pq.push(m);
                sum[m]+=sum[ind];
                //sum[m]++;
            }
        }
        if(pq.empty())
            cout<<"0 0\n";
        else{
        cout<<pq.top()/2<<" "<<max((pq.top()-(ll)1)/(ll)2,(ll)0)<<"\n";
        }
    }
    return 0;
}

