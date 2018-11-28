#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int c[t];
for(int x=0;x<t;x++)
{
    unsigned long long int n;
    cin>>n;
    unsigned long long int k=n;
    while(k)
    {
       unsigned long long  int p=k,r=0,d=0,cnt=0;
        int max=p%10;
        while(p)
        {
            r=p%10;
            d++;
            if(max>=r)
            {
                max=r;
                cnt++;
            }
            p=p/10;
        }
        if(cnt==d)
        {
            c[x]=k;
            break;
        }
        k--;
    }
}
for(int x=0;x<t;x++)
{
		cout<<"Case #"<<x+1<<": "<<c[x];
        cout<<endl;
}
}
