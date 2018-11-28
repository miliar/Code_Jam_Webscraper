#include<bits/stdc++.h>
using namespace std;

main()
{
freopen("C-small-1-attempt2.in","r",stdin);
freopen("output.txt","w",stdout);
    int t;
    int m = 1;
    cin>>t;
    while(t--)
    {
        long long n,k;
        cin>>n>>k;
//        if(n/2 < k)
//        {
//            printf("Case #%d: 0 0\n",m);
//            m++;
//        }
        {
            long long z=0,y=0,sample=n,zero=0;
            vector<long long> v;
            while(k--)
            {
                if(sample%2)
                {
                    y=z=sample/2;
                    v.push_back(z);
                    v.push_back(y);

                }
                else
                {
                    z=sample/2-1;
                    y=sample/2;
                    v.push_back(y);
                    v.push_back(z);
                }
                sample=*max_element(v.begin(),v.end());
                v.erase(max_element(v.begin(),v.end()));
                //cout<<sample<<" ";
            }
            printf("Case #%d: %lld %lld",m,y,z);
            cout<<endl;
            m++;
        }
    }
}
