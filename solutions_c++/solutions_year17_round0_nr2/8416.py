#include <iostream>
#include <vector>
using namespace std;
vector<int> myvec;

void propagateBack() {
  for (int i = 0; i < myvec.size(); i++)
    myvec[i] = 9;
}

void printvec() {
  for (int i = 0; i < myvec.size(); i++)
    cout << myvec[i] << " " << endl;
  cout << endl;
}

void getLastTidyNum(unsigned long long num) {
  while (num) {
    int lastdig = num % 10;
    unsigned long long divten = num / 10;
    if (!myvec.empty() && (lastdig > myvec.back())) {
      propagateBack();
      myvec.push_back(--lastdig);
    }
    else myvec.push_back(lastdig);
    num = divten;
  }
}



int main() {
  int TC;
  scanf("%d",&TC); // number of test cases
  for (int tc = 1; tc <= TC; tc++) {
    unsigned long long num, result;
    scanf("%llu", &num);
    getLastTidyNum(num);
    cout << "Case #" << tc << ": ";
    if (myvec.back() == 0) myvec.pop_back();
    while (!myvec.empty()) {
      cout << myvec.back();
      myvec.pop_back();
    }
    if (tc != TC) cout << endl;
  }
}
