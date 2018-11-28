#include<iostream>
#include<set>
#include<map>
using namespace std;

string myswap(string str, int start ,int end)
{
  for(int i = start ; i<= end ; ++i)
  {
    if(str[i] == '+')
      str[i] = '-';
    else
      str[i] = '+';
  }
  return str;
}

bool isCorrect(string& c, int n)
{
  for(int i = 0 ; i < n ; ++i)
  {
    if(c[i] == '-')
      return false;
  }
  return true;
}

int fun(string& str, int n, int k, set<string>& visited, map<string,int>& ansmap)
{
  visited.insert(str);

  if(isCorrect(str,n))
  {
    ansmap[str] = 0;
    return 0;
  }

  int count = -1;
  int currans = -1;

  for(int i = 0 ; i <=n-k; ++i)
  {
    string temp = myswap(str, i, i + k -1);

    if(visited.find(temp) == visited.end())
    {
      currans = fun(temp, n , k, visited, ansmap);
    }
    else
    {
      map<string,int>::iterator ss = ansmap.find(temp);
      if(ss == ansmap.end())
        continue;
      else
        currans = ss->second;
    }

    if(currans != -1 )
    {
      if(count == -1)
        count = currans;
      else if(count > currans)
        count = currans;
    }
  }

  if(count != -1)
    ++count;

  ansmap[str] = count;
  return count;
}

void solve(int test)
{
  string str;
  int k;
  cin>>str;
  cin>>k;

  set<string> visited;
  map<string,int> ansmap;
  int ans = fun(str, str.size(), k, visited, ansmap);

  if(ans != -1)
  cout<<"Case #"<<test<<": "<<ans;
  else
  cout<<"Case #"<<test<<": IMPOSSIBLE";

  cout<<"\n";
}

int main()
{
  int t;
  cin>>t;
  for(int i =0 ; i < t ; ++i)
  {
  solve(i+1);
  }
  return 0;
}