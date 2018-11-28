#include <iostream>
#include <string>

using namespace std;

string num;
string ans;
int mem;
int n;

int main()
{
  cin >> n;
  for (int x=0; x<n; x++)
  {
    mem = -1;
    cin >> num;
    if (num.length() == 1)
    {
      cout << "Case #" << x+1 << ": " << num << endl;
      continue;
    }

    for (int i=0; i<num.length()-1; i++)
    {    
      if (num[i] > num[i+1])
      {
        int p = mem != -1 ? mem : i;
        if (num[p] != '1')
        {
          ans.push_back(num[p] - 1);
        }
        for (int j=p+1; j<num.length(); j++)
          ans.push_back('9');
        break;    
      }
      else if (num[i] == num[i+1])
      {
        mem = mem == -1 ? i : mem;
      }
      else 
      {
        if (mem != -1)
        {
          for (int j=mem; j<i; j++)
            ans.push_back(num[j]);
        }
        mem = -1;  
        ans.push_back(num[i]);
      }

      if (i == num.length() - 2)
      { 
        if (mem != -1)
        {
          for (int j=mem; j<i+1; j++)
            ans.push_back(num[j]);
        }
        ans.push_back(num[i+1]);
      }
    }
    cout << "Case #" << x+1 << ": " << ans << endl;
    ans.clear();
  }
  return 0;
}