#include <bits/stdc++.h>
#define inf 10000000000000000.0
using namespace std;
const int N = 1005;
int t,n,d;
int dis[N];
int vit[N];
double tmp[N];

//bool verif(double v)
//{
//   double temp = (double)d/v;
//   cout<<"vitesse temp "<<v<<" "<<temp<<endl;
//   for(int i=0;i<n;i++)
//   {
//        if(tmp[i] > temp) return false;
//   }
//   return true;
//}
//
//double fun(double l,double r)
//{
//    for(int i=0;i<1000;i++)
//    {
//        double mid = (l+r)/2;
//        if(verif(mid)) r = mid;
//        else l = mid;
//    }
//    return r;
//}


int main()
{
    ifstream cin("A-large.in");
    ofstream cout("out");
    cin>>t;
    int tc(1);
    while(t--)
    {
        cin>>d>>n;
        double maxi = 0;
        for(int i=0;i<n;++i)
        {
            int k,s;
            cin>>k>>s;
            dis[i] = d - k;
            vit[i] = s;
            tmp[i] = (double)dis[i]/vit[i];
            maxi = max(maxi,tmp[i]);
            //cout<<tmp[i]<<" ";
        }
        cout<<"Case #"<<tc++<<": "<<fixed<<setprecision(9)<<(double)d/maxi<<endl;

    }
    return 0;
}
