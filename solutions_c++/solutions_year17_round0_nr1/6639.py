#include <iostream>
#include <string>

int main(int argc, char** argv)
{
  int t;
  
  std::cin >> t;
  
  int i;
  
  for (i = 0; i < t; i++)
  {
    std::string s;
    int k;
    
    std::cin >> s >> k;
    
    int n = s.length();
    
    int numFlips = 0;
    
    int j;
    
    for (j = 0; j < (n - k + 1); j++)
    {
      if (s[j] == '-')
      {
        numFlips++;
        
        int l;
        
        for (l = 0; l < k; l++)
        {
          s[j + l] = ((s[j + l] == '+') ? '-' : '+');
        }
      }
    }
    
    bool success = true;
    
    for (j = (n - k + 1); j < n; j++)
    {
      if (s[j] == '-')
      {
        success = false;
      }
    }
    
    if (success)
    {
      std::cout << "Case #" << (i + 1) << ": " << numFlips << std::endl;
    }
    
    else
    {
      std::cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << std::endl;
    }
  }
}
