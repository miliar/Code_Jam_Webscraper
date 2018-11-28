#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <list>
#include <cmath>
#include <climits>
#include <map>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cfloat>
#include <cmath>

using namespace std;
typedef long long lli;

int main(){
//    ios_base::sync_with_stdio(0);
//    cin.tie(0);
//    cout.tie(0);
    ofstream aout ( "a_out.txt" );
    lli t;
    cin>>t;
    lli cnt=1;
    while(t--)
    {
        lli d,n;
        cin>>d>>n;
        lli k,s;
//        int a[n+1][2];
        lli km=LLONG_MAX , sm=LLONG_MAX;
        double tm=-1,t;
        cout<<std::setprecision(20);
        for(int i =1; i<=n ; i++)
        {
            cin>>k>>s;
            t=(double)(d-k)/s;
            if(t>tm)
                tm=t;
        }
//        cout<<tm;
        double ans=(double)(d)/(tm);
//        cout<<setprecision()<<ans;
//        ans=(ans*1000000)/1000000.0;
//        ans=ans/1.0;
        cout<<"Case #"<<cnt<<": ";
        aout<<"Case #"<<cnt<<": ";
        cout<<fixed<<std::setprecision(6) <<ans;
        aout<<fixed <<std::setprecision(6)<<ans;
        cout<<endl;
        aout<<endl;
        cnt++;
    }
}
/*

1
1000000000 2
999999998 3
999999999 2

*/
