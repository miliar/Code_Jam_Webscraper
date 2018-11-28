#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

void flip(std::string &s, int pos, int k)
{
  for(int i = pos; i < pos + k; i++)
  {
    if(s[i] == '-')
    {
      s[i] = '+';
    }
    else
    {
      s[i] = '-';
    }
  }
}

int main(int argc, char* argv[])
{
  int ncases = 0;
  std::cin >> ncases;
  std::string s;
  int K = 0;
  std::ofstream out;
  out.open("result.txt");
  for(int kase = 0; kase < ncases; kase++)
  {
    std::cin >> s >> K;
    std::cout << s <<  " " << K << " --> ";
    int nflips = 0;
    for(int pos = 0; pos <= s.length() - K; pos++)
    {
      if(s[pos] == '-')
      {
        flip(s,pos,K);
        nflips++;
      }
    }
    bool possible = true;
    for(int pos = 0; pos < s.length(); pos++)
    {
      if(s[pos] == '-')
      {
        possible = false;
        break;
      }
    }

    std::cout << s << " ";
    out << "Case #" << (kase + 1) << ": ";
  
    if (possible)
    {
      std::cout << nflips << std::endl;
      out << nflips << std::endl;
    }
    else
    {
      std::cout << "IMPOSSIBLE" << std::endl;
      out << "IMPOSSIBLE" << std::endl;
    }
   
  }
  out.close();
  return 0; 
}
