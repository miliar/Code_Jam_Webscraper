#include <bits/stdc++.h>
#include <boost/range/irange.hpp>
#include <boost/range.hpp>
#include "../../prettyprint.hpp"
using namespace std;
using boost::irange;
using boost::make_iterator_range;

#ifdef NDEBUG
#include <boost/iostreams/stream.hpp>
#include <boost/iostreams/device/null.hpp>
boost::iostreams::stream<boost::iostreams::null_sink> logs((boost::iostreams::null_sink()));
#else
auto& logs = cerr;
#endif

using int_ = int;
#define int int_fast64_t

bool isok(string const& s) {
  auto res = s + s[0];
  int last = 0;
  for (char c : res) {
    int curr;
    switch (c) {
    case 'R': curr = 0b100; break;
    case 'O': curr = 0b110; break;
    case 'Y': curr = 0b010; break;
    case 'G': curr = 0b011; break;
    case 'B': curr = 0b001; break;
    case 'V': curr = 0b101; break;
    default: assert(false);
    }
    if ((last&curr) != 0)
      return false;
    last = curr;
  }
  return true;
}

string pop(vector<string>& v) {
  auto res = move(v.back());
  v.pop_back();
  return res;
}

string safepop(vector<string>& v) {
  if (v.empty())
    return string();
  auto res = move(v.back());
  v.pop_back();
  return res;
}

string solve() {
  int n, r, o, y, g, b, v;

  cin >> n >> r >> o >> y >> g >> b >> v;

  bool possible = false;

  // string bf = (string(r, 'R') +
  //              string(o, 'O') +
  //              string(y, 'Y') +
  //              string(g, 'G') +
  //              string(b, 'B') +
  //              string(v, 'V'));
  // sort(bf.begin(), bf.end());
  // do {
  //   if (isok(bf)) {
  //     possible=true;
  //     break;
  //   }
  // } while (next_permutation(bf.begin(), bf.end()));

  auto check = [r, o, y, g, b, v](string const& res) {
    assert(count(res.begin(), res.end(), 'R')==r);
    //assert(count(res.begin(), res.end(), 'O')==o);
    assert(count(res.begin(), res.end(), 'Y')==y);
    //assert(count(res.begin(), res.end(), 'G')==g);
    assert(count(res.begin(), res.end(), 'B')==b);
    //assert(count(res.begin(), res.end(), 'V')==v);
    assert(isok(res));
    for (size_t i=0; i+1 < res.size(); ++i) {
      assert(res[i] != res[i+1]);
    }
  };

  array<vector<string>, 3> groups;
  {
    auto& rs = groups[0] = vector<string>(r, "R");
    auto& ys = groups[1] = vector<string>(y, "Y");
    auto& bs = groups[2] = vector<string>(b, "B");
    while (o > 0 && bs.size() >= 2) {
      bs.push_back(pop(bs) + "O" + pop(bs));
      --o;
      --b;
    }
    while (g > 0 && rs.size() >= 2) {
      rs.push_back(pop(rs) + "G" + pop(rs));
      --g;
      --r;
    }
    while (v > 0 && ys.size() >= 2) {
      ys.push_back(pop(ys) + "V" + pop(ys));
      --v;
      --y;
    }

    if (o+g+v > 0) {
      if (o+g+v > 1 || r+y+b != 1) {
        assert(!possible);
        return "IMPOSSIBLE";
      }
      if (o==b && g==r && v==y) {
        string res;
        if (o) res += "O" + pop(bs);
        if (g) res += "G" + pop(rs);
        if (v) res += "V" + pop(ys);
        check(res);
        return res;
      }
      assert(!possible);
      return "IMPOSSIBLE";
    }
  }

  for (;;) {
    array<int, 3> abc{0,1,2};
    sort(abc.begin(), abc.end(),
         [&](int i, int j) { return groups[i].size() < groups[j].size(); });
    int a = groups[abc[0]].size();
    int b = groups[abc[1]].size();
    int c = groups[abc[2]].size();

    assert(a <= b && b <= c);

    auto& ga = groups[abc[0]];
    auto& gb = groups[abc[1]];
    auto& gc = groups[abc[2]];

    // cout << "current state: " << ga << gb <<gc<<'\n';

    if (a + b < c) {
      assert(!possible);
      return "IMPOSSIBLE";
    }

    if ((a + b) == c) {
      string res;
      while (!gc.empty()) {
        // cout << "a+b close to c: " << res << "  + " << ga<<gb<<gc<<'\n';
        if (ga.empty())
          res += pop(gb) + pop(gc);
        else
          res += pop(ga) + pop(gc);
      }
      assert(ga.empty());
      assert(gb.empty());
      check(res);
      return res;
    }

    if (c <= 1) {
      auto res = safepop(ga) + safepop(gb) + safepop(gc);
      check(res);
      return res;
    }

    gc.push_back(pop(gc) + pop(ga) + pop(gb) + pop(gc));
  }
}

int_ main() {
  int testcases; cin >> testcases;
  for (auto i : irange(int(1), testcases+1)) {;
    cout << "Case #" << i << ": " << solve() << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 b.cc -o b && for f in *.in; do echo \"--- $f -------------\"; ./b <$f; done"
 * end:
 */
