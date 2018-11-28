//solves small input
#include <iostream>
#include <vector>
using namespace std;

void convert(const string & S, vector<bool> & v)
{
  v.resize(S.size());
  for(int i = 0; i < S.size(); i++)
  {
    if(S[i] == '+')
    {
      v[i] = true;
    }
    else
    {
      v[i] = false;
    }
  }
}

void flip(vector<bool> & v, const int & i, const int & K)
{
  for(int j = i; j < i + K; j++)
  {
    v[j] = !v[j];
  }
}

bool done(const vector<bool> & v)
{
  for(const auto & e: v)
  {
    if(e == false)
    {
      return false;
    }
  }
  return true;
}

void findSol(const string & S, const int & K, bool & possible, int & answer)
{
  vector<bool> v;
  answer = 0;
  convert(S, v);
  for(int i = 0; i <= S.size() - K; i++)
  {
    if(!v[i])
    {
      flip(v, i, K);
      answer++;
    }
  }
  possible = done(v);
}

int main()
{
  int T;
  int K;
  int ans;
  bool possible;
  string S;
  cin >> T;
  for(int i = 1; i <= T; i++)
  {
    cin >> S >> K;
    findSol(S, K, possible, ans);
    cout << "Case #" << i << ": ";
    if(possible)
    {
      cout << ans << endl;
    }
    else
    {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}