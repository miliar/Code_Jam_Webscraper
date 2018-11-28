#include<iostream>
#include<cmath>
using namespace std;
int digits(unsigned long long int n)
{
    int ctr=0;
    do{
        ctr++;
    }while((n=n/10)!=0);
    return ctr;
}
inline unsigned long long int powe(int i)
{
    unsigned long long int y=1;
    for(;i>0;i--)
        y*=10;
    return y;
}
int main()
{
    int T,j=1;
    cin>>T;
    unsigned long long int N;
    while(cin>>N)
    {   int len=digits(N);
        for(int i=1;i<len;i++)
        {
            unsigned long long int x=powe(i+1);
            unsigned long long int y=powe(i);
            unsigned long long int z=powe(i-1);
            if((N%x)/y>(N%y)/z)
                N=N-(N%y)-1;
        }
        cout<<"Case #"<<j++<<": "<<N<<endl;
    }
}
