#include<cstring>
#include<iostream>
#include<algorithm>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<cassert>
#include<numeric>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<deque>
using namespace std;

int getPromotions(const vector<int>& tickets, int rides) {
  int spill = 0, promotions = 0;
  for(int i = tickets.size()-1; i >= 0; --i) {
    if (tickets[i] < rides) {
      spill = max(0, spill - (rides - tickets[i]));
    }
    else {
      spill += tickets[i] - rides;
      promotions += tickets[i] - rides;
    }
  }
  if(spill) return -1;
  return promotions;
}

int main() {
  int cases;
  cin >> cases;
  for(int cc = 0; cc < cases; ++cc) {
    int seats, customers, tickets;
    cin >> seats >> customers >> tickets;
    vector<int> ticket_for_customer(customers);
    vector<int> ticket_for_position(seats);
    for(int i = 0; i < tickets; ++i) {
      int seat, customer;
      cin >> seat >> customer;
      --seat;
      --customer;
      ticket_for_customer[customer]++;
      ticket_for_position[seat]++;
    }

    int lo = *max_element(ticket_for_customer.begin(), ticket_for_customer.end()) - 1;
    int hi = tickets;
    int last = 0;
    while(lo + 1 < hi) {
      int mid = (lo + hi) / 2;
      int promotions = getPromotions(ticket_for_position, mid);
      if(promotions < 0) {
        lo = mid;
      }
      else {
        hi = mid;
        last = promotions;
      }
    }
    printf("Case #%d: %d %d\n", cc+1, hi, last);
  }
}
