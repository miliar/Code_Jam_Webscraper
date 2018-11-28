#include <bits/stdc++.h>
using namespace std;
#define fori(n) for(int i=0;i<n;i++)
#define for0(i,n) for(int i=0;i<n;i++)
#define forit(i, c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ll long long
ll k[1005];
ll s[1005];

int main()
{
  int T,t;
  cin >> T;
  t=T;
  ll d;
  int n;  
  while(T--)
  {
    cin >> d>>n;
    double tt=-1;
    for0(i,n){ cin>>k[i]>>s[i];
    if((double)(d-k[i])/(double)s[i] > tt) tt=(double)(d-k[i])/(double)s[i];
    
    }
  cout <<"Case #"<<t-T<<": ";
  printf("%f", (float)d/tt);
    if(t>0) cout <<endl;
  }

	
	return 0;
	
	
	
	
}
