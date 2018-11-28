#include<iostream>
using namespace std;
int main()
{
short int t,x;
cin>>t;
for(x=1; x<=t; x++)
{
unsigned long long int num, n,i,last_n;
bool flag=true;
cin>>num;
for(i=1 ; i<=num; i++) {
    n=i;
    int rem = n%10;// 0
    n=n/10;
    while(n!=0)
    {
        int rem1 = n%10; // 2
    if(rem>rem1 || rem ==rem1)
    {
        n=n/10;
        flag =true;
        rem=rem1;
    }
    else
    {
        flag=false;
        break;
    }
    }
if(flag)
    last_n =i;

 }
cout<<"Case #"<<x<<": "<<last_n<<endl;
}
return 0;
}
