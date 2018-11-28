#include <iostream>
#include <string>

std::string getLastTidyNum(std::string n)
{
  int l = n.length();
  
  int i;
  
  for (i = 0; i < l; i++)
  {
    if (n[i] == '0')
    {
      std::string result(l - 1, '9');
      
      return result;
    }
    
    if (n[i] != '1')
    {
      break;
    }
  }
  
  std::string result(1, n[0]);
  
  for (i = 1; i < l; i++)
  {
    char next = n[i];
    char last = result[i - 1];
    
    if (next < last)
    {
      int j;
      
      for (j = (i - 1); j >= 0; j--)
      {
        result[j] = result[j] - 1;
        
        if (j > 0)
        {
          if (result[j] >= result[j - 1])
          {
            break;
          }
          
          result[j] = '9';
        }
      }
      
      result.append(l - i, '9');
      
      return result;
    }
    
    result += next;
  }
  
  return result;
}

int main(int argc, char** argv)
{
  int t;
  
  std::cin >> t;
  
  int i;
  
  for (i = 0; i < t; i++)
  {
    std::string n;
    
    std::cin >> n;
    
    std::cout << "Case #" << (i + 1) << ": " << getLastTidyNum(n) << std::endl;
  }
}
