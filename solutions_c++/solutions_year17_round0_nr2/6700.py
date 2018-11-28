#include <iostream>
#include <fstream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <bits/stdc++.h>
#define PI 3.14159265
#define MOD 1000000007
using namespace std ;


int main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    #else
     online submission
    #endif

    int t;
    cin>>t;
    int m=1;
    while(m<=t)
    {

        long long unsigned k1,k2, n,i,d,d1;
        cin>>n;
        i=n;
        int j=0,k;
        while(i!=0)
        {
            j++;
            i=i/10;
        }
        j--;
        k=j+1;
        for(;j>0;j--)
        {
            d = pow(10,j);
            d1 = pow(10,j-1);
            k1 = (long long unsigned) (n/d) % 10;
            k2 = (long long unsigned) (n/d1)%10;
            if(k1<k2)
            {
                k=j;
                continue;
            }
            else if (k1==k2)
            continue;
            else
            {
                n=n/pow(10,k-1);
                n--;
                n=n*pow(10,k-1);
                k1=0;
                while(k-1>0)
                {
                  i= pow(10,k-2)*9;
                  //cout<<i<<"\n";
                  k1+=i;
                  //cout<<k1<<"\n";
                  k--;
                }
                n+=k1;
                break;
            }
        }
        cout<<"Case #"<<m<<": "<<n<<"\n";
        m++;
    }




   return 0;
}
