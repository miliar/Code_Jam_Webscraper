#include<iostream>
using namespace std;
int f(unsigned long long int num)
{
    unsigned long long int x=num%10,rem,check=0;
    while(num)
    {
        rem=num%10;
        if(rem<=x)
        {
            x=rem;
            num/=10;
            check=1;
        }
        else
        {
            check=0;
            break;
        }

    }
    if(check)
        return 1;
    return 0;
}
int main()
{
    unsigned long long int n,num,i,j,check;
    cin>>n;
    unsigned long long int a[n]={0};
    for(j=0;j<n;j++)
    {
        cin>>num;
        for(i=0;i<num;i++)
        {
            check=f(num-i);
            if(check)
            {
                a[j]=num-i;
                break;
            }
        }
    }
    for(i=0;i<n;i++)
    {
        cout<<"Case #"<<i+1<<": "<<a[i]<<"\n";
    }
}
