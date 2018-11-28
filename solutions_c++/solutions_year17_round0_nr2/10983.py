#include <iostream>

int main (int argc, char** argv)
{
  int test;
  std::cin >> test;
  for (int i = 0; i < test; i++)
  {
    int num;
    std::cin >> num;
    int cp = num;
    int a = cp % 10;
    cp /= 10;
    int b = cp % 10;
    cp /= 10;
    int c = cp % 10;
    cp /= 10;
    int d = cp % 10;
    
    while (!(a >= b && b >= c && c >= d))
    {
      num--;
      cp = num;
      a = cp % 10;
      cp /= 10;
      b = cp % 10;
      cp /= 10;
      c = cp % 10;
    }
    std::cout << "Case #" << (i+1) << ": " << num << std::endl;
  }
}