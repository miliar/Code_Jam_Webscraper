#include <bits/stdc++.h>
using namespace std;

int main()
{
      freopen("B-small-attempt2.in","r",stdin);
      freopen("out.txt","w",stdout);
    long long t,n,cas=1;
    cin>>t;

    while(t--)
    {
        cin>>n;

            while(n>=0)
            {
            long long temp = n;
            long long rem = temp%10;
            temp/=10;
            while(temp>0)
            {
                if(temp%10<=rem)
                    rem = temp%10;
                else
                    break;
                    temp/=10;
            }
            if(temp==0)
                break;
                n--;
            }

        cout<<"Case #"<<cas++<<": "<<n<<endl;
    }
}
