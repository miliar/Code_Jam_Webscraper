#include <cstring>

#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

struct Ticket {
  int position;
  int buyer;

};

istream& operator >> (istream& is, Ticket& ticket) {
  is >> ticket.position >> ticket.buyer;
  ticket.position -= 1;
  ticket.buyer -= 1;
  return is;
}

void solve() {
  int n, c, m;
  cin >> n >> c >> m;
  vector<int> bought(c, 0);
  vector<Ticket> tickets(m);
  int rides = 0;
  for(int i = 0; i < m; ++i){
    cin >> tickets[i];
    bought[tickets[i].buyer] += 1;
    rides = max(rides, bought[tickets[i].buyer]);
  }
  vector<int> occupied(n, 0);
  vector<int> over(n, 0);
  for(int i = 0; i < m; ++i){
    int position = tickets[i].position;
    if(occupied[position] < rides){
      occupied[position] += 1;
    }else{
      over[position] += 1;
    }
  }
  int left = 0;
  for(int i = 0; i < n; ++i){
    left += rides - occupied[i];
    left -= over[i];
    while(left < 0){
      rides += 1;
      left += i + 1;
    }
  }
  left = 0;
  occupied.assign(n, 0);
  for(int i = 0; i < m; ++i){
    int position = tickets[i].position;
    if(occupied[position] < rides){
      occupied[position] += 1;
    }else{
      left += 1;
    }
  }
  cout << rides << ' ' << left << endl;
}

int main() {
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test){
    cout << "Case #" << test << ": ";
    solve();
  }
}
