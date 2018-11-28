/*
Ayush Goyal
IIT Guwahati
*/
#include<fstream>
#include <iostream>
#include <queue>
#include <vector>
#include <math.h>
#include <climits>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iomanip>
#include <limits.h>
typedef long long int lli;
#define INF 1e18L + 5
using namespace std;
int main()
{
    ofstream myfile;
    myfile.open ("output.txt");

    int t,k=1;
    cin>>t;
    while(t--)
    {

        lli n,d,temp1,temp2,pos;
        cin>>d>>n;
        vector<lli>a,b;
        double time,ans,maxi=0;
        for (int i=0;i<n;i++)
        {
            cin>>temp1>>temp2;
            time=double(d-temp1)/temp2;

            if(time > maxi)
            {
                maxi=time;
                pos=i;
            }
            a.push_back(temp1);
            b.push_back(temp2);
        }

        ans = double(a[pos])/maxi;
       // cout<<maxi<<endl;
        ans = ans + float(b[pos]);
        //cout<<ans<<endl;

        myfile<<fixed;
        myfile<<"Case #"<<k<<": "<<setprecision(6)<<ans<<endl;
        k++;
    }
    return 0;
}
