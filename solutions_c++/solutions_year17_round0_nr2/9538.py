#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
freopen("output_file_name.out","w",stdout);
   long long  int t,n,b,c,d,j,i;
    cin >> t;
    for(i=1;i<=t;i++)
    {
        cin >> n;
        if(n%10==n)
            cout <<"Case #"<< i <<": " <<n<< endl;
        else if(n%100==n)
        {
            b=n%10;
            c=n/10;
            if(c==b)cout <<"Case #"<< i <<": "<<n<< endl;
            else if(c>b){ for(j=n-1;j>=1;j--)
                {
                    b=j%10;
                    c=j/10;

                    if( b>=c){cout <<"Case #"<< i <<": "<<j<< endl;break;}
                }}
            else{cout <<"Case #"<< i <<": "<<n<< endl;}
        }
        else if(n%1000==n)
        {
            b=n%10;
            c=(n/10)%10;
            d=(n/10)/10;
            if( b>=c && c>=d){cout <<"Case #"<< i <<": "<<n<< endl;}
            else
            {
                for(j=n-1;j>=1;j--)
                {
                    b=j%10;
                    c=(j/10)%10;
                    d=(j/10)/10;
                    if( b>=c && c>=d){cout <<"Case #"<< i <<": "<<j<< endl;break;}
                }
            }
        }
        else if(n==1000)cout <<"Case #"<< i <<": 999"<< endl;

    }
    return 0;
}
