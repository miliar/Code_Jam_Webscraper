// Cure vs Debuff?

#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;
typedef long long ll;
typedef tuple<ll, ll, ll, ll> state;

constexpr ll p10(ll n) { return n==0 ? 1LL : 10LL*p10(n-1); }
ll INF = p10(10);

// min # of turns to to H dmg given initial attack A and buff B
ll min_turns(ll A, ll B, ll H) {
  // b buff, a attack -> (A+b*B)*a => a*A + a*b*B
  ll lo = 0;
  ll hi = H/B+1;
  // a*(A+b*B) >= H
  // a >= H
  auto score = [A,B,H](ll b) {
    ll atk = A+b*B;
    return b + ((H+atk-1)/atk);
  };
  while(lo+5 < hi) {
    ll m1 = (2*lo+hi)/3;
    ll m2 = (lo+2*hi)/3;
    ll s1 = score(m1);
    ll s2 = score(m2);
    if(s1 <= s2) {
      lo = m1;
    } else {
      hi = m2;
    }
  }
  ll best = score(lo);
  for(ll b=lo; b<=lo+5; b++) {
    best = min(best, score(b));
  }
  return best;
}

ll min_turns2(ll A, ll B, ll H, ll AK, ll HD) {
  ll as = min_turns(A, B, H);
  ll d = (HD+AK-1)/AK;
  if(as==1) { return 1; }
  if(d==1) { return INF; }
  if(as==2) { return 2; }
  if(d==2) { return INF; }
  as -= 2;
  d--;
  // cure on d, 2d, 3d, ...
  ll add = 0;
  while(true) {
    ll add2 = (as+add)/d;
    if(add2==add) { break; }
    add = add2;
  }
  return as+add+2;
}

ll solve(ll HD, ll AD, ll HK, ll AK, ll B, ll D) {
  ll ans = min_turns2(AD, B, HK, AK, HD);
  for(ll d=0; d<=100; d++) {

  }
  // d debuffs
  // if would die:
  //   cure
  // else:
  //   debuff
  //   buff
  //   attack
  return 0;
}

int main() {
  ll T;
  cin >> T;
  for(ll cas=1; cas<=T; cas++) {
    ll HD, AD, HK, AK, B, D;
    cin >> HD >> AD >> HK >> AK >> B >> D;

    bool done = false;
    queue<tuple<ll, ll, ll, ll, ll>> Q;
    Q.push(make_tuple(0, HD, HK, AD, AK));
    set<state> SEEN;
    while(!Q.empty()) {
      ll d, hd, hk, ad, ak;
      std::tie(d, hd, hk, ad, ak) = Q.front();
      if(ad>=hk) { ad=hk; }
      if(ak<=0) { ak=0; }
      if(hd<=0) { hd=0; }
      if(hk<=0) { hk=0; }

      Q.pop();
      state key = make_tuple(hd, hk, ad, ak);
      if(SEEN.count(key)==1) {
        continue;
      }
      SEEN.insert(key);
      if(hk<=0) {
        done = true;
        cout << "Case #" << cas << ": " << d << endl;
        break;
      }
      if(hd<=0) {
        continue;
      }
      Q.push(make_tuple(d+1, hd-ak, hk-ad, ad, ak));
      Q.push(make_tuple(d+1, hd-ak, hk, ad+B, ak));
      Q.push(make_tuple(d+1, HD-ak, hk, ad, ak));
      Q.push(make_tuple(d+1, hd-(ak-D), hk, ad, ak-D));
    }
    if(!done) {
      cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
    }
  }
}
