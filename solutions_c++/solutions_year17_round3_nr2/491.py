//
// google codejam - 2017 - round 1c - B
// John Smith
//

#include <bits/stdc++.h>
//#include <gmpxx.h>

using namespace std;

struct Activity {
     uint32_t start;
     uint32_t end;
     uint32_t who;

     Activity( uint32_t start=0, uint32_t end=0, uint32_t who=0 ) : start(start), end(end), who(who) {}
};

struct State {
     uint32_t A_time_min;
     uint32_t A_time_max;
     uint32_t who;
     uint32_t who0;
     uint32_t changes;

     State( uint32_t t0=0, uint32_t t1=0, uint32_t w=0, uint32_t changes=0 ) : A_time_min(t0),
                                                                               A_time_max(t1),
                                                                               who(w),
                                                                               who0(w),
                                                                               changes(changes) {}
};

bool operator<(State &s1, State &s2)
{
     return s1.changes < s2.changes;
}

bool operator<( Activity &a1, Activity &a2 )
{
     return a1.start < a2.start;
}

void show( vector<State> v )
{
     for (auto x : v)
     {
          cerr << setw(3) << x.A_time_min << " ";
          cerr << setw(3) << x.A_time_max << " ";
          cerr << setw(3) << x.changes << " ";
          cerr << endl;
     }
     cerr << "===========" << endl;
}

vector<State> simplify2( vector<State> v )
{
     sort(v.begin(), v.end());
     vector<State> v2;

     for (auto x : v)
     {
          bool reject = false;
          for (auto y : v2)
          {
               if (x.A_time_min >= y.A_time_min &&
                   x.A_time_max <= y.A_time_max)
               {
                    reject = true;
                    break;
               }
          }
          if (!reject)
          {
               v2.push_back(x);
          }
     }
     if (0) {
          show(v);
          show(v2);
          cerr << "================================================" << endl;
     }
     return v2;
}

vector<State> simplify( vector<State> v )
{
     vector<uint32_t> m(v.size());
     vector<State> v1;
     for (auto &x : m) x = 0;

     for (uint32_t i=0; i<v.size(); i++)
     {
          if (m.at(i) == 0)
          {
               vector<State> v2;
               for (uint32_t j=0; j<v.size(); j++)
               {
                    if (m.at(j) == 0 &&
                        v.at(j).who == v.at(i).who &&
                        v.at(j).who0 == v.at(i).who0 )
                    {
                         v2.push_back(v.at(j));
                         m.at(j) = 1;
                    }
               }

               v2 = simplify2( v2 );
               for (auto &x : v2) v1.push_back(x);
          }
     }
     return v1;
}

uint64_t solve( vector<Activity> v )
{
     sort (v.begin(), v.end());
     Activity a(1440,1440,2);
     v.push_back(a);

     vector<State> w;
     State s0(0,0, 0);
     State s1(0,0, 1);

     w.push_back(s0);
     w.push_back(s1);

     uint32_t t0=0;
     for (auto e : v)
     {
          w = simplify(w);
          //cerr << "Event " << setw(3) << e.start << " " << setw(3) << e.end << "  who " << e.who << endl;
          vector<State> w1;
          uint32_t dt = e.start - t0;

          for (auto s : w)
          {
               State s1;
               s1 = s;
               if (s1.who == 0) {
                    s1.A_time_min += dt;
                    s1.A_time_max += dt;
               }

               w1.push_back(s1);

               // with a single change
               s1 = s;
               s1.changes++;
               s1.A_time_max += dt;
               s1.who = 1-s1.who;
               w1.push_back(s1);

               // with two changes
               s1 = s;
               s1.changes++;
               s1.changes++;
               s1.A_time_max += dt;
               w1.push_back(s1);
          }
          t0 += dt;
          w = w1;
          w1.resize(0);

          if (e.who == 2) break;

          dt = e.end - t0;

          for (auto s : w)
          {
               if (s.who == e.who)
               {
                    State s1 = s;
                    if (s1.who == 0) {
                         s1.A_time_min += dt;
                         s1.A_time_max += dt;
                    }

                    w1.push_back(s1);
               }
          }
          t0 += dt;
          w = w1;
          w1.resize(0);
     }

     for (auto &s : w)
     {
          if (s.who != s.who0) s.changes++;
     }
     // Now choose the best

     uint32_t best = 1000000;
     for (auto s : w)
     {
          if (0) {
               cerr << setw(3) << s.A_time_min << " ";
               cerr << setw(3) << s.A_time_max << "   ";
               cerr << setw(3) << s.changes << endl;
          }

          if (s.A_time_min <= 720 &&
              s.A_time_max >= 720)
          {
               best = min(best,s.changes);
          }
     }

     return best;
}

int main(int argc, char ** argv)
{
     uint32_t T;
     cin >> T;
     for (uint32_t j=1; j<=T; j++)
     {
          uint32_t Ac, Aj;

          cin >> Ac >> Aj;

          vector<Activity> v(Ac+Aj);
          for (uint32_t i=0; i<Ac+Aj; i++)
          {
               cin >> v.at(i).start;
               cin >> v.at(i).end;
               v.at(i).who = (uint32_t) (i >= Ac);
          }

          auto a = solve( v );

          cout << "Case #" << j << ": ";
          cout << a;

          cout << endl;
     }

     return 0;
}
