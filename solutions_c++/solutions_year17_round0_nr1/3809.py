#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;
vector<int> flipped;

int main()
{
  int T;
  scanf("%d\n", &T);
  for(int i=1; i<=T; i++) {
    string S;
    int K;
    cin >> S >> K;

    flipped.clear();
    flipped.resize(S.size());
    int n=0;
    for(int j=0; j<S.size()-K+1; j++) {
      if((S[j]=='-' && flipped[j]==0) || (S[j]=='+' && flipped[j]==1)) {
        for(int k=0; k<K; k++) flipped[j+k] ^= 1;
        n++;
      }
    }

    int done = true;
    for(int j=S.size()-K+1; j<S.size(); j++)
      if((S[j]=='-' && flipped[j]==0) || (S[j]=='+' && flipped[j]==1)) {
        done = false;
        break;
      }

    if(done)
      cout << "Case #" << i << ": " << n << endl;
    else
      cout << "Case #" << i << ": IMPOSSIBLE"<< endl;
  }
  return 0;
}
