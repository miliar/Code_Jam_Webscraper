#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

int  main()
{
    int t, count =1;
    cin>>t;
    while(count <= t)
    {
        unsigned long long int N, p,sum = 0;
        cin>>N;
        p = N;
        int A[100], B[100],j=-1;
        while(p>0)
        {
            A[++j] = p%10;
            p /= 10;
        }
        for(int i=0;i<=j;i++)
        {
            B[i] = A[j-i];
        }

        int last = 0;
        for(int i=0;i<=j;i++)
        {
            if(i>0)
            {
                if(B[i] != B[i-1])
                {
                    last = i;
                }
            }
            if(i<j)
            {
                if(B[i]>B[i+1])
                {
                    for(int k = i+1;k<=j;k++)
                    {
                        B[k] = 9;
                    }
                    for(int k=last+1;k<=i;k++)
                        B[k] = 9;

                    B[last]--;
                    break;
                }
            }

        }

       /* if(pos == 98989723)
            pos = -1;

        for(int i = pos;i<=j;i++)
        {
            B[i] = 9;
        }*/
        cout<<"Case #"<<count<<": ";
        int k=0;
        while(B[k] == 0)
            k++;
        for(int i=k;i<=j;i++)
        {
            sum += B[i]*pow(10,j-i);
            cout<<B[i];
        }
        cout<<"\n";
        //cout<<B[0];
       // cout<<"Case #"<<count<<": "<<sum<<"\n";
        memset(A, 0, sizeof A);
        memset(B, 0, sizeof B);

        count++;

    }
    return 0;
}

