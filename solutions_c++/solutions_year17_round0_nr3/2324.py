#include<bits/stdc++.h>
#define ull unsigned long long
using namespace std;

int main()
{
    unsigned long long i,j,k,n,m;
    int test=0,testcase;

    cin>>testcase;

    while(testcase>test++)
    {
        cin>>n>>m;

        ull a[2][2],temp[2][2];

        printf("Case #%d: ",test);

        if(n%2==1)
        {
            a[0][0]=n/2;
            a[0][1]=2;
            a[1][0]=0;
            a[1][1]=0;
        }
        else
        {
            a[0][0]=n/2;
            a[0][1]=1;
            a[1][0]=(n/2)-1;
            a[1][1]=1;
        }
        if(m==1)
        {
            if(n%2==1)cout<<(n/2)<<" "<<(n/2)<<endl;
            else cout<<(n/2)<<" "<<((n/2)-1)<<endl;
            continue;
        }

        m--;

        while(m>0)
        {
            if(a[0][0]%2==1)
            {
                temp[0][0] = a[0][0] / 2 ;
                temp[0][1] = 2*a[0][1] + a[1][1];
                temp[1][0] = (a[0][0] / 2) - 1 ;
                temp[1][1] = a[1][1];
            }
            else
            {
                temp[0][0] = a[0][0] / 2 ;
                temp[0][1] = a[0][1];
                temp[1][0] = (a[0][0] / 2) - 1 ;
                temp[1][1] = a[0][1] + 2*a[1][1];
            }

            if(m > a[0][1] + a[1][1])m -= (a[0][1] + a[1][1]);

            else if(m <= a[0][1])
            {
                if(a[0][0]%2==1)cout<<(a[0][0]/2)<<" "<<(a[0][0]/2)<<endl;
                else cout<<(a[0][0]/2)<<" "<<(a[0][0]/2)-1<<endl;
                break;
            }

            else
            {
                if(a[1][0]%2==1)cout<<(a[1][0]/2)<<" "<<(a[1][0]/2)<<endl;
                else cout<<(a[1][0]/2)<<" "<<(a[1][0]/2)-1<<endl;
                break;
            }

            a[0][0]=temp[0][0];
            a[0][1]=temp[0][1];
            a[1][0]=temp[1][0];
            a[1][1]=temp[1][1];
        }
    }

    return 0;
}
