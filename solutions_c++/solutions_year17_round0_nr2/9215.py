#include<iostream>
using namespace std;
int main()
{
    unsigned long long int k,n,m,t,sum,i,j,in,ls;
    cin>>t;
    sum=1000;
    for(in=1;in<=t;in++)
    {
        n=sum;
        cout<<n<<" =";
        sum++;
        while(n)
        {
               int flag=1;
               m = n ;
               ls=9;
              // cout<<n<<" ";
                while(m)
                {
                    k = m%10;
                    if(ls>=k)
                    {
                        ls= k ;
                        m = m/10;
                    }
                    else{
                        m=0;
                        flag =0;
                    }
                }
                if(flag == 1)
                {
                    cout<<n<<endl;
                    n=0;
                }
                else
                {
                    n--;
                }
        }
    }
    return 0;
}
