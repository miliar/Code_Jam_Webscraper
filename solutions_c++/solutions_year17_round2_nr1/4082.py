#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{int t,p;
cin>>t;p=1;
    while(p<=t)
    {int n,i;
    double d;
    cin>>d>>n;
    int k[n],s[n];
    double x[n],sp;
    for(i=0;i<n;i++)
    {cin>>k[i]>>s[i];
      x[i]=(d-k[i])/s[i];
    }
    sort(x,x+n);
    sp=d/x[n-1];
    printf("Case #%d: %0.6lf\n",p,sp);
    p++;
    }
		return 0;
}
