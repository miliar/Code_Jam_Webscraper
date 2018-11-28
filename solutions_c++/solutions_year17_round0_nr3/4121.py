#include<bits/stdc++.h>
using namespace std;
priority_queue<long long > pq;
int main()
{

    freopen("test1.txt","r",stdin);
    freopen("file1.txt","w",stdout);
    long long t,n,k;
    cin>>t;
    long cnt=0;
    while(t--)
    {
        cnt++;
        cout<<"Case #"<<cnt<<": ";
        cin>>n>>k;
        /*long long val= n-(k-1);
        long long val1= val/k;
        if(val%k !=0)
            val1++;
        //cout<<val1<<endl;
        long long val2= val1-1;
        long long val3 = val2/2;
        if(val2%2 !=0)
            val3++;
        cout<<val3<<" "<<val2-val3<<endl;*/
       /* if(k> (n+1)/2){
            cout<<0<<" "<<0<<endl;
            continue;
        }*/
        pq.push(n);
        int flag=0;
        for(long i=1;i<=k-1;i++)
        {
            long long val4= pq.top();
            pq.pop();
            if(val4==1){
                cout<<0<<" "<<0<<endl;
                flag=1;
                break;
            }
            val4= val4-1;
            pq.push(val4/2);
            pq.push((val4/2)+ (val4%2));
        }
        if(flag==0){
            long long ans= pq.top();
            ans--;
            cout<<(ans/2  + (ans%2))<<" "<<(ans/2)<<endl;
        }
        while(!pq.empty())
            pq.pop();
    }
}
