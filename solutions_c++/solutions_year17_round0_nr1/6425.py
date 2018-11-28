#include <bits/stdc++.h>
using namespace std ;

long long int gcd(long long int a, long long int b)
  {
      return b == 0 ? a : gcd(b, a % b);
  }

int main()
  {
    ios_base::sync_with_stdio (false) ;
    long long int a, b, c, i, ans=0 ;
    cin>> a >> b ;
    c=gcd(a, b) ;
    for(i=1 ; i<=sqrt(c) ; i++)
        if(c%i==0)
          {
            if(c/i==i) ans+=1 ;
            else ans+=2 ;
          }
    cout<< ans ;
  }
