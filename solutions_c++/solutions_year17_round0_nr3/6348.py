#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class PairNode {
public:
  int index1;
  int index2;

  //constructor
  PairNode(int first, int second) : index1(first), index2(second) {};
};
class PairComparator {
public:
  bool operator()(PairNode *& n1, PairNode *& n2) const {
    //return larger min
    int loc1 =(n1->index2 + n1->index1)/2;
    int loc2 = (n2->index2 + n2->index1)/2;

    int min1 = min(loc1-(n1->index1), n1->index2-loc1);
    int min2 = min(loc2-(n2->index1), n2->index2-loc2);
    if (min1 < min2) {
      return true;
    }    
    else if (min1 == min2) {
      int max1 = max(loc1-(n1->index1), n1->index2-loc1);
      int max2 = max(loc2-(n2->index1), n2->index2-loc2);
      if (max1 < max2) {
        return true;
      }
      else if (max1 == max2) {
        if (loc1 > loc2) {
          return true;
        }
      }
    }
    return false;
  }
};

int main() {
  int numTests, numStalls, people;
  //for each test
  cin >> numTests;
  for (int i = 1; i < numTests+1; i++) {
    cin >> numStalls;
    cin >> people;
    priority_queue<PairNode*, vector<PairNode*>, PairComparator> gaps;

    //vector to represent stalls, with guards on each end
    vector<int> stalls (numStalls+2, 0);
    stalls.at(0) = 1;
    stalls.at(stalls.size()-1) = 1;

    PairNode* first = new PairNode(0, stalls.size()-1);    
    gaps.push(first);
    PairNode* curr;
    for (int j = 0; j < people; j++) {
      curr = gaps.top();
      gaps.pop();
      int index = ( (curr->index2) + (curr->index1))/2;
      stalls.at(index) = 1;
      PairNode * half = new PairNode(curr->index1, index);
      PairNode * half2 = new PairNode(index, curr->index2);
      gaps.push(half);
      gaps.push(half2);
    }
    int loc = (curr->index2 + curr->index1)/2;
    cout << "Case #" << i << ": " << max(loc - curr->index1, curr->index2 - loc)-1 
                           << " " << min(loc - curr->index1, curr->index2 - loc)-1 << endl;
  }
return 0;
}
