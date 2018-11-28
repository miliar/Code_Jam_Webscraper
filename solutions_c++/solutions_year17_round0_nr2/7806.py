#include<bits/stdc++.h>
using namespace std;
int main()
{ freopen("B-large.in", "r", stdin);
  freopen("outLB.txt", "w", stdout);
  int T, s;
  long long n;
  int a[20];
  cin>>T;
  for(int I=1;I<=T;++I)
  { cin>>n;
    s=0;
    while(n)
    { a[s]=n%10; ++s;
      n=n/10;
    }
    if(s==1)
    { cout<<"Case #"<<I<<": "<<a[0]<<"\n";
      continue;
    }
    for(int i=s-1;i>0;--i)
    { if(a[i-1]<a[i])
      { int j;
        for(j=i;j<s-1;++j)
        { if(a[j+1]<a[j])break;
        }
        a[j]-=1;--j;
        for(;j>=0;--j)a[j]=9;

        break;
      }
    }
    cout<<"Case #"<<I<<": ";
    if(a[s-1]!=0)cout<<a[s-1];
    for(int i=s-2;i>=0;--i)cout<<a[i];

    cout<<"\n";

  }
}
