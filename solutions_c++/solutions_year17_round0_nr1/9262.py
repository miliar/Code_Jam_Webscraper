#include <iostream>
#include <climits>
#include <vector>
#include <queue>
using namespace std;

int solve(vector<bool> bits, int N)
{
  queue<int> flips;
  int moves = 0;

  for (int i = 0; i < bits.size(); ++i)
  {
    if (!flips.empty() && flips.front() <= i - N)
      flips.pop();

    if ((bits[i] ^ (flips.size() % 2 == 0)) == 1)
    {
      if (i > bits.size() - N)
        return -1; // IMPOSSIBLE

      moves++;
      flips.push(i);
    } 
  }
  return moves;
}


int main() {
    long tc;
    cin>>tc;
    for(int i = 0; i<tc; i++)
    {        
        string s; int N;
        cin>>s>>N;
        vector<bool> bits;
        int M = s.length();
        for(int j = 0;j < M;j++)
        {
            if(s[j] == '+')
            {
              bits.push_back(true);
              //cout<<endl<<"true"<<endl;
            }
            else
            {
              bits.push_back(false);
              //cout<<endl<<"false"<<endl;
            }
        }
        cout<< "Case #"<<(i+1)<<": ";
        int res = solve(bits, N);
        if(res >= 0)
            cout<<res<<endl;
        else
            cout<<"Impossible"<<endl;
    }
    return 0;
}

