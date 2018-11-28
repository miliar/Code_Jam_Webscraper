#include <bits/stdc++.h>

using namespace std;


typedef long long ll;
typedef long double ld;



int main()
{
  ll t;
  cin >>t;
 for(ll k=0;k<t;k++)
  {
 ll d,n;
 cin >> d>>n;
 ll a[n][2];
 ld max=0;
 for(ll i =0;i< n;i++)

{
  cin >> a[i][0]>>a[i][1];
  a[i][0]=d-a[i][0];
  if(max<(ld(a[i][0])/a[i][1]))
  max =(ld(a[i][0])/a[i][1]);

}


float q= (d/max);

cout <<"Case #"<<k+1<<": ";
printf("%.7f\n",q);


    }


    return 0;
}