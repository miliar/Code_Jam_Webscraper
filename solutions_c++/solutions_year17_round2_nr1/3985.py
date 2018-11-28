#include<iostream>
#include <iomanip>
#define ll long long int 
using namespace std;
// tushar kumar dtu
int main()
{


ll  x;
cin>>x;
ll j=1;
while(x--)
{



    double d,n,i;
    cin>>d>>n;
    double ma=0;
    for(i=0;i<n;i++)
    {
        double k,s,ans;
        cin>>k>>s;
        ans=(d-k)/s;
        if(ans>ma)
        {
            ma=ans;
        }
    }
    cout<<"Case #"<<j<<": ";
    std::cout << std::fixed;
    std::cout << std::setprecision(6);
    cout<<d/ma<<"\n";

j++;
}
return 0;
}