#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<queue>
#include<iomanip>
using namespace std;

int main()
{
   freopen("input.in","r",stdin);
   freopen("output.out","w",stdout);
   // std::ios::sync_with_stdio(false);
    int x=0;
    int t;
    long long int n,d,temp,ki,si,KI,SI;
    double dis,sp,time,T=0;
    cin>>t;
    while(x++ < t){
        T=0;
        cin>>d>>n;
        temp=n;
        while(temp--){
            cin>>ki>>si;
            time = ((d-ki)*1.0)/si;
            if(time > T){
                T = time;
            }
        }

        double ans = (d*1.0)/T;
        cout<<"Case #"<<x<<": ";
        printf("%.6f\n",ans);

        }
}

