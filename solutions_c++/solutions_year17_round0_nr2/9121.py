#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
      freopen("B-small-attempt0.in","r",stdin);
    freopen("ja.txt","w",stdout);
    int t,n,b,mio,y=1,c;
    cin>>t;
    while(t--)
    {


        cin>>n;
        while(n)
        {
        int a[1000],o=-1,kam=0;
        mio=0;
        b=n;
        while(b)
        {
            c=b%10;
            a[++o]=c;
            b=b/10;
        }
        for(int i=o;i>=0;i--)
        {
            if(a[i]>=mio)
            {
                mio=a[i];
            }
            else
            {
                kam=1;
                break;
            }
        }
        if(kam)
        {
            n--;
        }
       else
       {
           cout<<"case #"<<y<<": "<<n<<endl;
            ++y;
            break;
       }
        }

    }

}
