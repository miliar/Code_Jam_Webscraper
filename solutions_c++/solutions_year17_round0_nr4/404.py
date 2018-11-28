// Qualification Round 2017, Problem D.  Fashion Show
// Copyright 2017 Christian Brechbuehler alias Quigi
// using gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1)

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>


class In {                      // const int, initialized from std::cin
public:
  In() {std::cin >> i_;}
  operator int() {return i_;}
private:
  int i_;
};

enum Style {kNone, kPlus, kX, kBoth};   // bit set
static const char Symbol[] = ".+xo";    // indexed by Style

struct Model {
  int style;                    // actually Style, but allow sloppier |=
  bool added;
};

typedef std::pair<int, int> Position;
typedef std::map<Position, Model> Arrangement;
typedef std::vector<bool> VB;   // the quirky specialization

bool add(Model *model, const Style style, const char symbol,
         VB::reference taken0, VB::reference taken1) {
  if (symbol == Symbol[kBoth ^ style] || taken0 || taken1) return false;
  taken0 = taken1 = true;
  model->style |= style;
  model->added = symbol == '?';   // first assistant's (false), then mine (true)
  return true;
}

int add2(const int R, const int C, Arrangement *arr,
         VB* t_row, VB* t_col, VB* t_down, VB* t_up, const char symbol = '?') {
  Model &model = (*arr)[Position{R,C}];
  const int N = t_row->size();
  return add(&model, kX   , symbol, (*t_row )[R-1    ], (*t_col)[C-1  ])
    +    add(&model, kPlus, symbol, (*t_down)[R-C+N-1], (*t_up )[R+C-2]);
}
  

static int do_case() {
  In N, M;
  VB t_row(N), t_col(N), t_down(2*N-1), t_up(2*N-1);
  Arrangement model;
  int score = 0;
  for (int j = M; j--; ) {
    char symbol;
    std::cin >> symbol;
    In R, C;
    score += add2(R, C, &model,  &t_row, &t_col, &t_down, &t_up, symbol);
  }

  for (int r = 1; 2*r <= N; ++r) // work from outside in.  For odd N, no center
    for (int c = r; c <= N-r; ++c) {
      score += add2(r, c    , &model, &t_row, &t_col, &t_down, &t_up)
        + add2(c     , N+1-r , &model, &t_row, &t_col, &t_down, &t_up)
        + add2(N+1-r , N+1-c , &model, &t_row, &t_col, &t_down, &t_up)
        + add2(N+1-c , r     , &model, &t_row, &t_col, &t_down, &t_up);
    }

  if (N%2)
    score += add2((N+1)/2, (N+1)/2, &model, &t_row, &t_col, &t_down, &t_up);
  
  int n_added = 0;
  for (auto placement : model) n_added += placement.second.added;
  std::cout << score << " " << n_added << std::endl;

  for (auto placement : model)
    if (placement.second.added) {
      std::cout << Symbol[placement.second.style] << " "
                << placement.first.first << " " << placement.first.second
                << std::endl;
    }
}

        
int main() {
  In T;
  for (int j = 1; j <= T; ++j) {
    std::cout << "Case #" << j << ": ";
    do_case();
  }
  return 0;
}
