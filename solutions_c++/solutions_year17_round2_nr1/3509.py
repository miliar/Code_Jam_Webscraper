#include <bits/stdc++.h>
#include <fstream>
#define lli long long int


using namespace std;

int main()
{
    ifstream input;
    input.open("input.in");
    ofstream output;
    output.open("output.txt");
    int t;
    input>>t;
    for(int tt=1 ; tt<=t ; tt++)
    {
     int d,n;
     input>>d>>n;
        double max=0;
        for(int i=0;i<n;i++)
        {
            double k,s;
            input>>k>>s;
            double div=(d-k)/(double)s;
            if(div>max)
                max=div;
        }
        double ans=d/max;
         output << std::fixed;
         output << setprecision(6);
         output<<"Case #" <<tt<< ": "<<ans<<endl;

}
return 0;
}
