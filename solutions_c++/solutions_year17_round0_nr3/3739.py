#include <iostream>
#include <fstream>
#include <cmath>

#define LL long long

using namespace std;

int main()
{
    LL n,k,T;
    ofstream fileo;
    ifstream filei;
    filei.open("2.in");
    fileo.open("2.out");
    //cin>>T;
    filei>>T;
    for (LL i=0;i<T;i++)
    {
       //cin>>n>>k;
       filei>>n>>k;
       //cout<<"Case #"<<i+1<<": ";
       fileo<<"Case #"<<i+1<<": ";
       if (n==k)
            //cout<<0<<" "<<0<<endl;
            fileo<<0<<" "<<0<<endl;
       else
       if (k==1)
            //cout<<n/2<<" "<<(n-1)/2<<endl;
            fileo<<n/2<<" "<<(n-1)/2<<endl;
       else
       {
           LL logcut=floor(log(k*1.0)/log(2.0)+0.0000001);
           LL cut=pow(2,logcut);
           LL avg=(n-(cut-1))/cut;LL more=(n-(cut-1))-cut*avg;
           //cout<<k<<" "<<log(k*1.0)/log(2.0)<<" "<<logcut<<" "<<"cut="<<cut<<" "<<"avg="<<avg<<endl;
           if (more>=(k-cut+1))
                //cout<<(avg+1)/2<<" "<<avg/2<<endl;
                fileo<<(avg+1)/2<<" "<<avg/2<<endl;
           else
                //cout<<avg/2<<" "<<(avg-1)/2<<endl;
                fileo<<avg/2<<" "<<(avg-1)/2<<endl;
       }
    }
    return 0;
}
