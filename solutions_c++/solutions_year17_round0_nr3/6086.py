#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long T,cnt=1;
    cin>>T;
    while(T--)
    {    long long n,k,a,b,y,z;
         cin>>n>>k;
         priority_queue <int> p;
         p.push(n);
         while(k!=0)
         {
             n=p.top();
             p.pop();
             if(n%2==0)
             {
                 a=n/2;
                 b=(n/2)-1;
                 p.push(b);
                 p.push(a);
             }
             else
             {
                 a=n/2;
                 b=n/2;
                p.push(a);
                p.push(b);
             }
             k--;
         }
         y=max(a,b);
         z=min(a,b);
         cout<<"Case #"<<cnt<<":"<<" "<<y<<" "<<z<<endl;
         cnt++;
    }
    return 0;
}
