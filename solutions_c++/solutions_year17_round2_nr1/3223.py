#include<bits/stdc++.h>
using namespace std;
int main()
{//freopen("a.txt","r",stdin);
//freopen("xxx.txt","w",stdout);
int n;cin>>n;
for(int xx=1;xx<=n;xx++)
{long  double d,si,di;
int horses;
cin>>d>>horses;
        long double a[horses];
        for(int i=0;i<horses;i++)
            {cin>>di>>si;
            a[i]=d-di;
            a[i]=d*si/a[i];
            //cout<<a[i];
            //a[i]=si;
            }
            sort(a,a+horses);
  cout<<"Case #"<<xx<<": " << fixed << setprecision(6)<<a[0]<<endl;
}
}
