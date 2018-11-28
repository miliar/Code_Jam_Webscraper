// g++ -std=c++0x -o C C.cpp

#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <tuple>

struct Config
{
  int Hd;
  int B;
  int D;
};

struct State
{
  int Hd;
  int Ad;
  int Hk;
  int Ak;
};

bool
operator<(const State& x, const State& y)
{
  return std::tie(x.Hd, x.Ad, x.Hk, x.Ak) <
         std::tie(y.Hd, y.Ad, y.Hk, y.Ak);
}

typedef char DragonAction;
const DragonAction ATTACK = 'A';
const DragonAction BUFF = 'B';
const DragonAction CURE = 'C';
const DragonAction DEBUFF = 'D';

State
battleRound(const Config& c, State s, DragonAction a)
{
  switch (a) {
    case ATTACK:
      s.Hk -= s.Ad;
      break;
    case BUFF:
      s.Ad += c.B;
      break;
    case CURE:
      s.Hd = c.Hd;
      break;
    case DEBUFF:
      s.Ak = std::max(0, s.Ak - c.D);
      break;
  }
  if (s.Hk > 0) {
    s.Hd -= s.Ak;
  }
  return s;
};

void
solve()
{
  Config c;
  State s;
  std::cin >> s.Hd >> s.Ad >> s.Hk >> s.Ak >> c.B >> c.D;
  c.Hd = s.Hd;

  std::string defaultAttempts;
  defaultAttempts += ATTACK;
  if (c.B > 0) {
    defaultAttempts += BUFF;
  }
  if (c.D > 0) {
    defaultAttempts += DEBUFF;
  }

  int maxRounds = static_cast<int>(ceil(static_cast<float>(s.Hk) / static_cast<float>(s.Ad))) * 2; // A-C

  std::set<State> reachedStates; // states we've reached
  std::map<std::string, State> lastRound;
  lastRound[""] = s;
  for (int nRounds = 1; nRounds <= maxRounds; ++nRounds) {
    std::map<std::string, State> thisRound;
    for (const auto& p : lastRound) {
      std::string attempts = defaultAttempts;
      if (p.second.Hd <= p.second.Ak && nRounds > 1 && p.first[nRounds - 2] != CURE) { // cure only if dragon might die, and don't cure twice in a row
        attempts += CURE;
      }
      for (DragonAction a : attempts) {
        State s = battleRound(c, p.second, a);
        if (s.Hk <= 0) { // dragon wins
          std::cout << nRounds;
          return;
        }
        else if (s.Hd <= 0) { // dragon loses, don't continue
        }
        else {
          bool isNewState = reachedStates.insert(s).second;
          if (isNewState) {
            thisRound[p.first + a] = s;
            //std::cerr << (p.first + a) << ' ' << s.Hd << ' ' << s.Ad << ' ' << s.Hk << ' ' << s.Ak << '\n';
          }
          else { // state reached with same or lesser rounds, don't continue
          }
        }
      }
    }
    lastRound.swap(thisRound);
  }
  std::cout << "IMPOSSIBLE";
}

int
main()
{
  int T;
  std::cin >> T;
  for (int CASE = 1; CASE <= T; ++CASE) {
    std::cout << "Case #" << CASE << ": ";
    solve();
    std::cout << '\n';
  }
}
