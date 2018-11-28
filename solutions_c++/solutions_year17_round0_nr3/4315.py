#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdlib>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
  {
    unsigned long long int N;
    cin >> N;
    unsigned long long int K;
    cin >> K;

    unsigned long long int numRounds_ = 0;
    unsigned long long int K_ = 0;
    while(K_ + pow(2, numRounds_) < K) {
      K_ = K_ + pow(2, numRounds_);
      numRounds_++;
    }
    unsigned long long int numGroups = (unsigned long long int) pow(2, numRounds_);


    double numPerGroup = (N - K_)/(double)numGroups;
    double numPerGroupLeft = (unsigned long long int) numPerGroup;
    double numPerGroupRight = (unsigned long long int) numPerGroup + 1;
    unsigned long long int numGroupsRight = (N - K_)%numGroups;
    unsigned long long int numGroupsLeft = numGroups - numGroupsRight;

    unsigned long long int finalNumPerGroup;
    if ((K - K_) <= numGroupsRight) finalNumPerGroup = numPerGroupRight;
    else finalNumPerGroup = numPerGroupLeft;

    unsigned long long int minS = (unsigned long long int) ((finalNumPerGroup - 1)/2.0);
    unsigned long long int maxS = (unsigned long long int) ((finalNumPerGroup -1 )/2.0) + (finalNumPerGroup -1 )%2;

    cout << "Case #" << t << ": " << maxS << " " << minS << endl;
  }
  return 0;
}
