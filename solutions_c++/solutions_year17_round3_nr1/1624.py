#include <bits/stdc++.h>
#define ll long long
#define pi 3.14159265358
#include <iostream>
#include <fstream>
using namespace std;
//double arr[1005];

struct s
{
    double r;
    double h;
    double area;
    double p;
    double c;
    int marked;
};
bool my(struct s a,struct s b)
{
        return (a.area>b.area);
}
bool ny(struct s a,struct s b)
{
        return (a.p>b.p);
}
struct s arr[1005];
int main()
{
    double a,b,c,d,ans=0,u,v,max;
    ll int i,j,k,l,t;
    ofstream myfile;
    myfile.open ("example.txt");
	    myfile.precision(25);
    cin>>t;
    i=1;
    while(i<=t)
    { max=0;
    u=0;
        ans=0;
    cin>>k>>l;
    for(j=0;j<k;j++)
    {
    cin>>arr[j].r;
    cin>>arr[j].h;
    arr[j].area=2*pi*arr[j].h*arr[j].r;
    arr[j].p=pi*arr[j].r*arr[j].r+2*pi*arr[j].h+arr[j].r;
    arr[j].c=pi*arr[j].r*arr[j].r;
    arr[j].marked=0;
   // if(u<arr[j].p)
   //   {
   //       u=arr[j].p;
   //     v=arr[j]
    }
    sort(&arr[0],&arr[j],my);
    for(j=0;j<l-1;j++)
    {
        ans+=arr[j].area;
        arr[j].marked=1;
        if(max<arr[j].c)
            max=arr[j].c;
    }
    u = arr[j].area;
    if(arr[j].c>max)
        max=arr[j].c;
    sort(&arr[0],&arr[k],ny);
    j=0;
    while(arr[j].marked==1)
      { j++;
          continue;
      }
   if(arr[j].c+arr[j].area>u+max)
    ans+=(arr[j].c+arr[j].area);
    else
        ans+=u+max;
    myfile<<"Case #"<<i<<": "<<ans<<endl;
    i++;
    }
    myfile.close();
    return 0;
}
