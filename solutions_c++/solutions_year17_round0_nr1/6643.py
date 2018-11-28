#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct PancakeStack
{
    vector<bool> stack;

    void FromStr(string str)
    {
        for(int i = 0; i < str.length(); ++i) {
            if(str[i] == '+')
                stack.push_back(true);
            else
                stack.push_back(false);
        }
    }

    void Print()
    {
        for(bool cake : stack)
            cout << cake? 1 : 0;

        cout << '\n'; 
    }

    void Flip(int index, int width)
    {
        for(int i = 0; i < width; ++i)
            stack[index + i] = !stack[index + i];
    }

    bool AllHappy()
    {
        for(bool cake : stack)
            if(!cake)
                return false;

        return true;
    }
};

int main()
{  
  int T, K;

  cin >> T;

  for(int i = 0; i < T; ++i) 
  {
      PancakeStack s;
      string str;
      int flips = 0;

      cin >> str >> K;

      s.FromStr(str);

      for(int j = 0; j < s.stack.size() - K + 1; ++j) {
          if(!s.stack[j]) {
            s.Flip(j,K);
            flips++;
          }
      }

      cout << "CASE #" << i+1 << ": " << (s.AllHappy()? to_string(flips) : "IMPOSSIBLE") << '\n';
  }

  return 0;
}