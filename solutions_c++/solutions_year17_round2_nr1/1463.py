#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
using namespace std;
ifstream infile("file.in");
ofstream outfile("file.out");
int t;
int n;
int num;
long long d;
long long horse[1001][2];
int main()
{
    while(infile>>t)
    {
        for(int i=0;i<t;++i)
        {
            infile>>d>>n;
            int zhishu=0;
            infile>>horse[0][0]>>horse[0][1];
            for(int j=1;j<n;++j)
            {
                infile>>horse[j][0]>>horse[j][1];
                if((d-horse[j][0])*horse[zhishu][1]>(d-horse[zhishu][0])*horse[j][1])
                {
                    zhishu=j;
                }
            }
            double v=double(horse[zhishu][1])/(1.0-double(horse[zhishu][0])/double(d));
            outfile<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<v<<endl;
        }
    }
}
