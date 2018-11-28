#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<fstream>
using namespace std;
int main()
{

    ifstream infile ("jam1big.in");
    ofstream outfile ("jam1out.txt");
    outfile << fixed;
    outfile.precision(6);
    int test;
    infile>>test;
    for(int t=0;t<test;t++)
    {
        int distance,n;
        infile>>distance>>n;
        double ans=0;
        if(n>0)
        {
            double mytime=0;
            for(int i=0;i<n;i++)
            {
                int d,s;
                infile>>d>>s;
                double dist=1.0*(distance-d);
                double time = dist/s;
                if(time>mytime) mytime=time;

            }
            ans=distance/mytime;


        }
        //printf("Case #%d: %f\n",t+1,ans);
        outfile<<"Case #"<<t+1<<": "<<ans<<endl;
    }
    return 0;
}
