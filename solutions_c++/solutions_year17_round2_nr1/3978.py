#include<iostream>
#include <iomanip>
using namespace std;
int main()
{


long long int t;
cin>>t;long long int j=1;
while(t>0)
{



    double d,n,i;
    cin>>d>>n;
    double maximum=0;
    for(i=0;i<n;i++)
    {
        double k,s,ans;
        cin>>k>>s;
        ans=(d-k)/s;
        if(ans>maximum)
        {
            maximum=ans;
        }
    }
    cout<<"Case #"<<j<<": ";
    std::cout << std::fixed;
    std::cout << std::setprecision(6);
    cout<<d/maximum<<"\n";







j++;

    t--;
}








}
