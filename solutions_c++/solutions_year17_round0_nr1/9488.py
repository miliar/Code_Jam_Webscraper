#include <iostream>
#include <set>
#include <queue>
using namespace std;

string flip(string s, int start, int flipperSize)
{
  for(int i = start; i < start + flipperSize; i++)
  {
    if(s[i] == '+')
    {
      s[i] = '-';
    }
    else
    {
      s[i] = '+';
    }
  }
  
  return s;
}

bool isOk(string s)
{
  for(int i = 0; i < s.size(); i++)
  {
    if(s[i] != '+')
      return false;
  }
  return true;
}

void solve()
{
  // read-in
  string s; cin >> s;
  int flipperSize; cin >> flipperSize;

  //  mark first as done
  set<string> done;
  done.insert(s);
  
  // do queue stuff
  queue<pair<int, string>> Q;
  Q.push(make_pair(0,s));
  
  while(!Q.empty())
  {    
    int depth = Q.front().first;
    string cur = Q.front().second;
    Q.pop();
    
    if(isOk(cur))
    {
      cout << depth << endl;
      return;
    }

    // start at the first location
    for(int i = 0; i <= cur.size() - flipperSize; i++)
    {
      string next = flip(cur, i, flipperSize);
      
      // check if not already used
      if(done.find(next) == done.end())
      {
        done.insert(next);
        Q.push(make_pair(depth + 1, next));
      }
    }
  }
  
  
  cout << "IMPOSSIBLE" << endl;
}

int main()
{  
  int n; cin >> n;
  for(int i = 1; i <= n; i++)
  {
    cout << "Case #" << i << ": ";
    solve();
  }
}