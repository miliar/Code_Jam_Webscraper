#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define f(i,st,en)for(int i=st;i<en;i++)
#define fi(i,st,en)for(int i=st;i<=en;i++)
typedef vector<int>vi;
typedef long long int ll;

int conv(string str)
{
  stringstream ss(str);
  int i;
  ss >> i;
  return i;
}

string con(int a){
     stringstream ss;
     ss << a;
     string str = ss.str();
     return str;
}


int main()
{
   freopen("in_large","r",stdin);
  freopen("out_large","w",stdout);


    int t;
    scanf("%d",&t);
    double d;
     int n;
    for(int test=1;test<=t;test++)
    {
      printf("Case #%d: ",test);
      cin>>d>>n;
      double k[n],s[n];
      for(int i=0;i<n;i++){
           cin>>k[i];
           cin>>s[i];
      }

      double mina=0;
      for(int i=0;i<n;i++){
           mina=max(mina,((d-k[i])/s[i]));
      }

      printf("%lf",d/mina);
      printf("\n");
    }
    return 0;
}
