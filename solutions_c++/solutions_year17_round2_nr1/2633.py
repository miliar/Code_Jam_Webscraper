#include <iostream>
#include <string>
#include <iomanip>
#include <fstream>
using namespace std;
int main()
{
    ofstream file("Ali.txt");
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        file<<"Case #"<<i<<": ";
        int d,n;
        cin>>d>>n;
        double m=0;
        for(int j=0;j<n;j++)
        {
            int a,b;
            cin>>a>>b;
            double c = (double)(d-a)/b;
            if(c>m)
            {
                m=c;
            }
        }
        file<<fixed<<setprecision(6)<<d/m<<endl;
    }
    return 0;
}
