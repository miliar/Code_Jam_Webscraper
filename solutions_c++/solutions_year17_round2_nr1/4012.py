#include<iostream>
#include <iomanip>
using namespace std;
int main()
{
 long long int t;
 cin>>t;
 long long int p=1;
 while(t>0)
 {
    double dd,n,i;
    cin>>dd>>n;
    double max=0;
    for(i=0;i<n;i++)
    {
        double r,u,answer;
        cin>>r>>u;
        answer=(dd-r)/u;
        if(answer>max)
        {
            max=answer;
        }
    }
    cout<<"Case #"<<p<<": ";
    std::cout << std::fixed;
    std::cout << std::setprecision(6);
    cout<<dd/max<<"\n";

   p++;
   t--;
 }
return 0;
}