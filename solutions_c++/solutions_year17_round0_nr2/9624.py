#include<iostream>
using namespace std;
int isTedy(unsigned long long n)
{
    int count=0;
    unsigned long long temp=n;
    unsigned long long temp1=n;
    while(temp>0)
    {
        temp=temp/10;
        count++;
    }
    int array[count];
    int i,j;
    for(i=count-1;i>=0;i--)
    {
        j=temp1%10;
        array[i]=j;
        temp1=temp1/10;
    }
    int k;
    for(k=count-1;k>=0;k--)
    {
        if(array[k]>=array[k-1])
        {}
        else 
            return 0;
            
    }
    return 1;
}
unsigned long long lastTedy(unsigned long long n)
{
    //int last_tedy;
    while(n>0)
    {
        if(isTedy(n)==1)
            return n;
        else
            n--;
    }
}
int main()
{
    int n;
    int i;
    unsigned long long num;
    unsigned long long res;
   
    cin>>n;

    for(i=1;i<=n;i++)
    {
      
        cin>>num;
        res=lastTedy(num);
      
        cout<<"Case #"<<i<<": "<<res<<"\n";
    }
    return 0;
}