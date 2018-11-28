
#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
   freopen("C:\\Downloads\\Documents\\Downloads\\C1.in","r",stdin);
    freopen("C:\\Downloads\\Documents\\Downloads\\out1.txt","w",stdout);
    int t;
    cin>>t;
    int h=1;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
         priority_queue<int>q;
         //queue<int>q;
         q.push(n);
        int g=0;
        int orig;
        while(!q.empty())
        {
            orig=q.top();
            g++;
            if(g==k)
                break;
            q.pop();
            if(orig%2==0)
            {
                q.push(max((orig-orig/2),0));
                q.push(max(((orig/2)-1),0));
            }
            else
            {
                q.push(max(((orig-1)/2),0));
                q.push(max(((orig-1)/2),0));
            }
        }
        cout<<"Case "<<"#"<<h++<<":"<<" ";
        n=orig;
        if(n%2!=0)
        {
               long long mi=(n-1)/2;
                long long ma=(n-1)/2;
                ma=max(ma,0ll);
                mi=max(mi,0ll);
                cout<<ma<<" "<<mi<<"\n";
        }
        else
        {
                long long ma=n/2;
                long long mi=(n-2)/2;
                ma=max(ma,0ll);
                mi=max(mi,0ll);
                cout<<ma<<" "<<mi<<"\n";
        }
    }
    return 0;
}
