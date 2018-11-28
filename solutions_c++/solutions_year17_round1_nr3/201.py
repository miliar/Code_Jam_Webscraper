#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef long long int lli;

lli hd, ad, hk, ak, b, d;

const lli INF = 10000000000000;

lli simulate(lli buffs, lli debuffs) {
  lli hdc=hd, adc=ad, hkc=hk, akc=ak;
  lli turnsPassed = 0;
  while(debuffs > 0) {
    if (hdc-(akc-d) <= 0) {
      turnsPassed++;
      hdc = hd-akc;
      if (hdc-(akc-d) <= 0)
        return INF;
    } else {
      turnsPassed++;
      debuffs--;
      akc-=d;
      hdc-=akc;
    }
  }
  while(buffs > 0) {
    if (hdc-akc <= 0) {
      turnsPassed++;
      hdc = hd-akc;
      if (hdc-akc <= 0)
        return INF;
    } else {
      turnsPassed++;
      buffs--;
      adc+=b;
      hdc-=akc;
    }
  }
  while(hkc > 0) {
    if (hkc-adc <= 0) {
      return turnsPassed+1;
    } else if (hdc-akc <= 0) {
      turnsPassed++;
      hdc = hd-akc;
      if (hdc-akc <= 0)
        return INF;
    } else {
      turnsPassed++;
      hkc-=adc;
      hdc-=akc;
    }
  }
  return turnsPassed;
  /*
  lli turnsPerCure = (hd-1)/akc;
  lli usefulTurnsLeft = buffs + (hkc-1)/(adc+buffs*b);
  lli turnsToCure = (hdc-1)/akc;
  if (usefulTurnsLeft <= turnsToCure+1)
    return turnsPassed + usefulTurnsLeft;
  if (turnsPerCure < 1)
    return INF;
  turnsPassed += turnsToCure+1;
  usefulTurnsLeft -= turnsToCure;
  return turnsPassed + usefulTurnsLeft + (usefulTurnsLeft-1)/turnsPerCure;
  */
}

lli buffTernarySearch(lli debuffs) {
  lli dl = 0, dr = hk;
  while (dr-dl > 5) {
    lli dm1 = (dl*2+dr)/3, dm2 = (dl+dr*2)/3;
    lli r1 = simulate(dm1, debuffs), r2 = simulate(dm2, debuffs);
    if (r1<r2) {
      dl = dm1;
    } else if (r1>r2) {
      dr = dm2;
    } else {
      cout << "BUFFS FAILED" << endl;
    }
  }
  lli ret = simulate(dl, debuffs);
  for(lli di=dl+1;di<=dr;++di) {
    ret = max(ret, simulate(di, debuffs));
  }
  return ret;
}

lli debuffTernarySearch() {
  lli dl = 0, dr = ak;
  while (dr-dl > 10) {
    lli dm1 = (dl*2+dr)/3, dm2 = (dl+dr*2)/3;
    lli r1 = buffTernarySearch(dm1), r2 = buffTernarySearch(dm2);
    if (r1<r2) {
      dl = dm1;
    } else if (r1>r2) {
      dr = dm2;
    } else {
      cout << "DEBUFFS FAILED" << endl;
    }
  }
  lli ret = buffTernarySearch(dl);
  for(lli di=dl+1;di<=dr;++di) {
    ret = max(ret, buffTernarySearch(di));
  }
  return ret;
}

int main() {
  int numCases;
  cin >> numCases;
  for (int testCase=1; testCase<=numCases; ++testCase) {
    cout << "Case #" << testCase << ": ";
    cin >> hd >> ad >> hk >> ak >> b >> d;
    lli best=INF;
    for(lli debuffs=0;debuffs<=100;++debuffs)
      for(lli buffs=0;buffs<=100;++buffs) {
        best = min(best, simulate(debuffs, buffs));
      }
    if (best==INF) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << best << endl;
    }
  }
}