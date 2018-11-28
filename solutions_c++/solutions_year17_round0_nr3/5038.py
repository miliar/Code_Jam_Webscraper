#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;
ll arr[100100],t,k,n,ans,temp1,temp,temp2;
int main()
{
    freopen("input1codejam.in","r",stdin);
    freopen("output1codejam.out","w",stdout);
    cin>>t;
    priority_queue<ll> que;
    for(int i=1;i<=t;i++)
    {
        while(!que.empty())
            que.pop();
        cin>>n>>k;
        temp=n,ans=0;
        que.push(n);
        pair<ll,ll> ans1;
        while(ans<k)
        {
            temp=que.top();
            temp--;
            que.push(temp/2);
            que.push(temp-temp/2);
            ans1.first=max(temp/2,temp-temp/2);
            ans1.second=min(temp/2,temp-temp/2);
            que.pop();
            ans++;
        }
        cout<<"Case #"<<i<<": "<<ans1.first<<" "<<ans1.second<<endl;
    }
return 0;
}
