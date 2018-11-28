#include <bits/stdc++.h>
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
   freopen("in.txt","r",stdin);
    freopen("loveu2.txt","w",stdout);
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
  {int N;
    string s;
     cin>>s;
     cin>>N;
     int n=s.size();
     vector<bool>v;
    // int a[(int)s.size()];
     for(int i=0;i<s.size();i++)
        {


         if(s[i]=='+')
         v.push_back(1);
         else
          v.push_back(0);

        }
        if(solve(v,N)==-1)
         printf("Case #%d: IMPOSSIBLE\n",i);
         else
        printf("Case #%d: %d\n",i,solve(v,N));

}
}
