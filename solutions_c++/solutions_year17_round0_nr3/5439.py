    #include <bits/stdc++.h>
    using namespace std;

    int main()
    {
        ios::sync_with_stdio(false);
        int t;
        cin>>t;

        for(int i=0; i<t; i++)
        {
          long long n,k;
          cin>>n>>k;

          vector<long long>D={n};
          long long L=0,R=0;

          for(int i=0; i<k;i++)
          {
              stable_sort(D.begin(),D.end());
              long long c = D.back();
              D.pop_back();

              if(c%2!=0)
              {
                  L=R=c/2;
                  D.push_back(L);
                  D.push_back(R);
              }
              else
              {
                  L=c/2-1;
                  R=c/2;
                  D.push_back(L);
                  D.push_back(R);
              }
          }
          cout<<"Case #"<<i+1<<": "<<max(L,R)<<" "<<min(R,L)<<"\n";

        }

    }

