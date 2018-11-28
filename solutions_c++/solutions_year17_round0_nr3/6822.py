#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0; i<t; ++i)
    {
        unsigned long long m, n;
        cin>>m>>n;
        unsigned long long arr[m+2] = {0};
        arr[0] = 1;
        arr[m+1] = 1;
        for(unsigned long long k = 0; k<n; ++k){
        unsigned long long startr =0, endr=0;
        unsigned long long maxran = 0, temp=0;

        for(int j = 0 ; j<m+2;)
        {
            if(arr[j]==0){
                temp++;
                j++;
            }
            else if(arr[j]==1)
            {
                if(temp>maxran)
                {
                    maxran =0;
                    maxran = temp;
                    temp = 0;
                    endr = j;
                }
                else if(temp<=maxran)
                    temp=0;
                j++;
            }
        }
        startr = endr - (maxran+1);
        //cout<<startr<<' '<<endr<<' '<<maxran<<' '<<endl;
        arr[(startr+endr)/2] = 1;
        if(k==(n-1)){
        cout<<"Case #"<<i+1<<": "<<max(((startr+endr)/2 - startr), endr - (startr+endr)/2) - 1<<' '<<min(((startr+endr)/2 - startr), endr - (startr+endr)/2) - 1<<endl;
        }
    }
    }
}
