#include <iostream>
#include <vector>
using namespace std;

#define PRINT 0

int main()
{
    long long t,n,k,ans;
    cin>>t;
    for(int i = 1; i <= t; i++)
    {
        cin>>n>>k;
        bool filled[n+2];
        long long dl[n+2];
        long long dr[n+2];
        long long ll = 0,lr = n+1;
        for(int p = 1; p < n+1; p++)
        {
            filled[p] = false;
        }
        filled[0] = filled[n+1] = true;
        vector<long long> pans;
        long long min;
        long long max;
        for(int z = 0; z < k; z++)
        {
            for(int x = 0; x < n+2; x++)
            {
                if(filled[x])
                {
                    ll = x;
                    dl[x] = 0;
                }
                else
                {
                    dl[x] = x - ll; 
                }
            }
            #if PRINT
                for(int i = 0; i < n+2; i++)
                    cout<<"dl : "<<dl[i]<<" ";
                cout<<endl;
            #endif
            for(int x = n+1; x >= 0; x--)
            {
                if(filled[x])
                {
                    lr = x;
                    dr[x] = 0;
                }
                else
                {
                    dr[x] = lr -x; 
                }
            }
            #if PRINT
                for(int i = 0; i < n+2; i++)
                    cout<<"dr : "<<dr[i]<<" ";
                cout<<endl;
            #endif
            pans.clear();
            min = max = 0;
            for(int x = 1; x < n+1; x++)
            {
                if(std::min(dl[x], dr[x]) == min)
                {
                    pans.push_back(x);
                }
                else if(std::min(dl[x], dr[x]) > min)
                {
                    pans.clear();
                    pans.push_back(x);
                    min = std::min(dl[x], dr[x]);
                }
            }
            #if PRINT
            for(auto iter = pans.begin(); iter != pans.end(); iter++)
                cout<<"pans : "<<*iter<<" ";
            cout<<endl;
            #endif
            for(auto iter = pans.begin(); iter != pans.end(); iter++)
            {
               if(std::max(dl[*iter], dr[*iter]) > max)
               {
                   ans = *iter;
                   max = std::max(dl[*iter], dr[*iter]);
               }
            }
            #if PRINT
            cout<<"ans : "<<ans<<endl;
            #endif
            filled[ans] = true;
        }
        cout<<"Case #"<<i<<": "<<std::max(dl[ans], dr[ans]) - 1<<" "<<std::min(dl[ans], dr[ans]) - 1<<endl; 
    }
    return 0;
}
