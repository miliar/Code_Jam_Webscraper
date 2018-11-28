#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
// constructing priority queues
#include <iostream>       // std::cout
#include <queue>          // std::priority_queue
#include <vector>         // std::vector
#include <functional>     // std::greater
#include <algorithm>    // std::max

typedef pair<long, long> P;
typedef struct Order
{
    bool operator()(P const& a, P const& b) const
    {
        return (a.first < b.first) || (a.first == b.first && a.second > b.second);
    }
} Order;

int main() {
  int t, N, K;
  t = 1;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int x = 1; x <= t; ++x) {
    cin >> N >> K;  // read n and then m.
    //cout << "NewCase #" << x << ": " << N << " " << K << endl;
    priority_queue< P, vector<P>, Order > pq;

    //pq experiment: pq.push(std::make_pair(4,-1));
    //pq experiment: pq.push(std::make_pair(0,3));
    //pq experiment: pq.push(std::make_pair(2,3));
    //pq experiment: pq.push(std::make_pair(2,1));
    //pq experiment: pq.push(std::make_pair(0,2));
    //pq experiment: pq.push(std::make_pair(4,6));
    //pq experiment: pq.push(std::make_pair(0,1));
    //pq experiment: pq.push(std::make_pair(4,-2));
    //pq experiment: pq.push(std::make_pair(2,2));
    //pq experiment: pq.push(std::make_pair(4,1));
    //pq experiment: while(pq.size()>0) {
    //pq experiment: 	P gap = pq.top();
    //pq experiment:     pq.pop();
    //pq experiment:     cout << gap.first << " " << gap.second << endl;
    //pq experiment: }
    
    pq.push(std::make_pair((long)N,0));
    for (long i=0; i<K-1; i++)
    {
        P gap_tuple = pq.top();
        pq.pop();
        long gap = gap_tuple.first;
        long start = gap_tuple.second;
        pq.push(std::make_pair((gap-1)/2, start));
        pq.push(std::make_pair((gap-1-((gap-1)/2)), start+((gap-1)/2)+1));
    }

    P fg = pq.top();
    long gap = fg.first;
    long a = (gap-1)/2;
    long b = (gap-1-((gap-1)/2));
    cout << "Case #" << x << ": " << max(a,b)  << " " << min(a,b) << endl;

  } 
}
