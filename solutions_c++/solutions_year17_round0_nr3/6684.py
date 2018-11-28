#include<iostream>
#include<queue>
#include<vector>
#include <sstream>
#define MAX(x,y) x>y?x:y
#define MIN(x,y) x<y?x:y

using namespace std;

struct band {
  int left,right;
  int size() const {
    return right - left;
  }

  string str() const {
    stringstream ss;
    ss << left << "," << right;
    return ss.str();
  }
};


struct compareBand {
  bool operator()(const band &lhs, const band &rhs) {
    if (lhs.size() > rhs.size())
      return false;
    if (lhs.size() < rhs.size()) 
      return true;
    return lhs.left > rhs.left;
  }
};

int main() {
  int cases;
  cin >> cases;
  for (int c = 0; c < cases; ++c) {
    int n,k;
    cin >> n;
    n += 2;
    cin >> k;
    priority_queue<band,vector<band>,compareBand> pq;
    band first({1,n-2});
    pq.push(first);
    int max,min;
    for (int i = 0; i < k; ++i) {
      band top = pq.top();
      pq.pop();
      int pos;
      if (top.left +1 == top.right)
	pos = top.left;
      else
	pos = (top.right - top.left) / 2 + top.left;
      band b1,b2;
      b1.left = top.left;
      b1.right = pos-1;
      b2.left = pos + 1;
      b2.right = top.right;
      max = MAX(top.right-pos,pos-top.left);
      min = MIN(top.right-pos,pos-top.left);
      
      if (b1.size() >= 0)
	pq.push(b1);
      if (b2.size() >= 0) 
	pq.push(b2);
    }
    cout << "Case #" << c+1 << ": " << max << " " << min << endl;
    
  }
}
