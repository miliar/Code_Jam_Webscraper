#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

void solve(int i ,ll n , ll k)
{
  ll parfst=n,parsnd=0,parpair,parimpair,fst = n/2,snd=n/2-1,cnt=0,pair,impair,prob=1,left,right;
  if(n % 2 == 0)
    {
      parpair = 1;
      parimpair=0;
      pair = 1;
      impair = 1;
    }
  else
  {
    parpair=0;
    parimpair=1;
    if( (n/2) % 2  == 0)
      {
        pair = 2;
        impair=0;
      }
    else
      {
        impair = 2;
        pair=0;
      }
  }
  cnt = 1;
  while(cnt < k)
    {
      ll espar;
      ll aux = fst/2;
      if(fst % 2)
        if((fst/2) % 2 == 0)
          espar = 1;
        else
          espar = 0;
      if (snd % 2)
        if( (snd/2) %2 == 0)
          espar = 1;
        else
          espar = 0;
      parfst = fst;
      parsnd = snd;
      fst = aux;
      snd = aux-1;
      parpair = pair;
      parimpair = impair;
      ll guard = impair;
      pair = pair;
      impair = pair;
      if(espar)
        pair += guard*2;
      else
        impair += guard*2;
      prob*=2;
      cnt += prob;
    }
  // cout << "fst : " << fst << " snd: " << snd << " cnt: " << cnt << " prob: " << prob <<
  //   " pair: " << pair << " impair : " << impair << "\n";
  if(fst < 0) fst = 0;
  if(snd < 0) snd = 0;
  if(parfst % 2 == 0)
    {
      if(prob - (cnt - k) <= parpair)
        left = fst, right = snd;
      else
        left = snd, right = snd;
    }
  else
    {
      if( prob- (cnt - k) <= parimpair)
        left = fst , right = fst;
      else
        left = fst , right = snd;
    }
  cout << "Case #" << i << ": " << left << " " << right << "\n";
}


int main(int argc, char *argv[])
{
  ll n,k;
  int t,tot; cin >> t;
  tot = t;
  while(t--)
    {
      cin >> n >> k;
      solve(tot-t,n,k);
    }
  return 0;
}
