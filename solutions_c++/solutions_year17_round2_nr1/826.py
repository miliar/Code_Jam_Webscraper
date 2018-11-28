#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("be.txt","r",stdin);
    freopen("ki.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=0;tc<t;tc++) {
        int d, n;
        cin>>d>>n;
        long double t_max=0;
        for(int i=0;i<n;i++) {
            int poz, speed;
            cin>>poz>>speed;
            int s=d-poz;
            t_max=max(t_max,(long double)s/(long double)speed);
        }
        long double v=(long double)d/t_max;
        cout<<"Case #"<<tc+1<<": "<<fixed<<setprecision(10)<<v<<endl;
    }
    return 0;
}
