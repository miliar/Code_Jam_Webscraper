#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("in.in");
    fout.open("out.txt");

    int t, i =0;

    fin>>t;


    while(i<t && ++i)
    {
        long long int d;
        int n;
        long double k, s;
        fin>>d>>n;

        long double maxi = 0;
        for(int j=0; j<n; j++)
        {
            fin>>k>>s;
            maxi = max(maxi, (d-k)/s);
        }

        long double ans = floor(1000000 * (d/maxi) ) / 1000000 ;
        fout<<"Case #"<<i<<": "<<fixed<<ans<<endl;
    }

}
