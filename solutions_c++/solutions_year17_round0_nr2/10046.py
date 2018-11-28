#include <bits/stdc++.h>
#define ll long long

using namespace std;
ifstream fin("C:\\Users\\ASUS\\Desktop\\B-small-attempt0.in");
ofstream fout("C:\\Users\\ASUS\\Desktop\\B-small-attempt0.txt");

int main()
  {
    ll tc;
    fin>>tc;
    for(int w=1;w<=tc;w++)
    {
      ll n;
      fin>>n;
      ll k;
      bool tidy=0;
      n++;
      while (--n &&!tidy)
      {
        k=n;
        ll x=n%10;
        n/=10;
        while(x>=n%10 && n)
        {
          x=n%10;
          n/=10;
        }
        if (!n)
          tidy=1;
       n=k;
      }
      if (tidy)
        fout<<"Case #"<<w<<": "<<k<<endl;
    }
  }
