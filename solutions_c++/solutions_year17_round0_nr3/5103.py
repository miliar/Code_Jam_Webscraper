#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
using namespace std;

int v[1000010];

int main () {
  ofstream myfile;
  ifstream input;
  input.open("input.txt");
  myfile.open ("output.txt");
  int t;
  input>>t;
  for(int i=1; i<=t; i++){
    int n, k;
		input>>n>>k;

    std::priority_queue<int> stallIntervals;
    stallIntervals.push(n);

    int bestInterval, halfBest, countmax;
		for(int j=0; j<k; j++) {
      bestInterval = stallIntervals.top();
      if (bestInterval == 1) {
        countmax = 0;
        halfBest = 0;
        break;
      }
      bestInterval--;
      stallIntervals.pop();
      halfBest = bestInterval/2;
      stallIntervals.push(halfBest);
      if (halfBest*2 == bestInterval) {
        stallIntervals.push(halfBest);
        countmax = halfBest;
      } else {
        countmax = halfBest + 1;
        stallIntervals.push(countmax);
      }
		}
    myfile<<"Case #"<<i<<": "<<countmax<<" "<<halfBest<<endl;
  }
  myfile.close();
  input.close();
  return 0;
}
