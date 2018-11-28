#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t, n, m;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        long long int n,a,c=0,p=0,temp,count=0,ans,rem;
        cin>>n;
l:
        c=0;
        a=n;
        p=0;
        count=0;
        while(a!=0)
        {
            rem=a%10;
            a=a/10;

            if(c&&temp<rem)
            {
                p=1;
                break;
            }
            temp=rem;
            c=1;
            count++;
        }
        if(p)
        {
            ans=a;
            ans=ans*10+rem-1;
            while(count--)
                ans=ans*10+9;
            n=ans;

            goto l;
        }
        else
            cout << "Case #" << i << ": " << n<< endl;
    }
}
