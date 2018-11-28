#include<iostream>
using namespace std;
int main()
{
    long long int N;
    int T,i,m,l,n;
    cin>>T;
    for(i=1;i<=T;i++)
    {
    cin>>N;
    n=N;
    do
    {

        l=n%10;
        n=n/10;
        m=n%10;
        if(l>=m)
        {
        continue;
        }

        else
        {
            N=N-1;
            n=N;
        }
    }while(n!=0);
    cout<<"Case #"<<i<<": "<<N<<endl;
    }
return 0;
}
