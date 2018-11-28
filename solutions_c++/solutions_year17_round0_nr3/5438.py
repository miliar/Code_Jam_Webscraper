#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
       int ansl=0,ansr=0;
        long long int n,k;
        cin>>n>>k;
        if(n==k)
        {
            cout<<"Case #"<<i<<": "<<"0 0"<<"\n";
            continue;
        }
        priority_queue<long long int> myq;
        myq.push(n);
        for(int j=0;j<k;j++)
        {
            long long int topNum=myq.top();
            myq.pop();
          //  cout<<topNum<<endl;
            if(topNum%2==0)
            {
                myq.push(topNum/2);
                myq.push(topNum-(topNum/2)-1);
                ansr=topNum-(topNum/2)-1;
                ansl=topNum/2;
            }
            else
            {
                myq.push(topNum/2);
                myq.push(topNum/2);
                ansr=topNum-(topNum/2)-1;
                ansl=topNum/2;
            }
        }
       cout<<"Case #"<<i<<": "<<ansl<<" "<<ansr<<"\n";
    }
    return 0;
}