    #include<bits/stdc++.h>
    using namespace std;
    #define pb push_back
    typedef vector<int> vi;
    typedef vector<char> vc;
    typedef long long int ll;

    int main()
    {
        freopen("C-small-2-attempt1.in","r",stdin);
        freopen("c3.out","w",stdout);
        int t;
        cin>>t;
        for(ll z=1;z<=t;z++)
        {
          ll n,k,m,o;
          cin>>n>>k;

          priority_queue<ll> arr;
          arr.push(n);
          for(ll i=1;i<=k;i++)
          {
              n=arr.top();
              arr.pop();
              m=n/2;
              o=n-m-1;
              n=m;
              if(i==k)
              {
                  cout<<"Case #"<<z<<": "<<m<<" "<<o<<"\n";
              }
              else {arr.push(m);arr.push(o); }
          }
        }
        return 0;
    }
