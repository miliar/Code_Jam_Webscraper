#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;

int main()
{
    int t,n,k,c=1;
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        int pos=INT_MIN;
        int stalls[n+2],left[n+2],right[n+2];
        memset(stalls,0,sizeof stalls);
        stalls[0]=stalls[n+1]=1;
        for(int person=0;person<k;person++)
        {
            int dist=0;
            for(int i=0;i<n+2;i++)
            {
                if(stalls[i])
                {
                    dist=0;
                }
                else
                {
                    left[i]=dist++;
                }
            }

            dist=0;
            for(int i=n+1;i>=0;i--)
            {
                if(stalls[i])
                {
                    dist=0;
                }
                else
                {
                    right[i]=dist++;
                }
            }


            int mi=INT_MIN;
            for(int i=0;i<n+2;i++)
            {
                if(stalls[i])continue;
                if(min(left[i],right[i]) == mi && max(left[i],right[i]) > max(left[pos],right[pos]))
                {
                    pos=i;
                }
                else if(min(left[i],right[i])>mi)
                {
                    mi=min(left[i],right[i]);
                    pos=i;
                }

            }

            stalls[pos]=1;
        }
            cout<<"Case #"<<c++<<": "<<max(left[pos],right[pos])<<" "<<min(left[pos],right[pos])<<endl;
    }
    return 0;
}
