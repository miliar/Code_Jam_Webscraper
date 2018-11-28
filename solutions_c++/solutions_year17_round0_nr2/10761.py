#include <iostream>
using namespace std;

long int tidy(long int n)
{
    if(n==1000) return 999;
    int a[3];
    int x;
    do
    {
    x=n;
    a[0]=x/100;
    a[1]=(x%100)/10;
    a[2]=x%10;
    
    if(a[0]<=a[1] && a[1]<=a[2]) return n;
    else n--;
    }while(n>=1);
}

int main() {
    long int n=0,t=0;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>n;
        long int x=tidy(n);
        cout<<"case #"<<i<<"  "<<x<<"\n";
        
    }
    return 0;
}
