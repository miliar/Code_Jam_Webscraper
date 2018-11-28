#include <iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<iomanip>
#include<map>
#include<vector>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    int t; cin>>t;
    for(int w=1;w<=t;w++){
            cout<<"Case #"<<w<<":"<<" ";
    double d,n; cin>>d>>n; double pos[1001],v[1001],time[1001];
    for(int i=0;i<n;i++)cin>>pos[i]>>v[i];
    for(int i=0;i<n;i++)
    {
        time[i]=(double)abs(pos[i]-d)/v[i];
    }
    double mi=-20,ans=0; for(int i=0;i<n;i++)mi=max(mi,time[i]);
    cout<<setprecision(20)<<d/mi<<endl;
    }
}
