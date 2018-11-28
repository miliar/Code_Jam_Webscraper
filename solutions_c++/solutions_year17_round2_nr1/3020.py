#include <iostream>
#include <iomanip>

int main(int argc, char** argv)
{
  int t;
  
  std::cin >> t;
  
  int i;
  
  for (i = 0; i < t; i++)
  {
    int d;
    int n;
    
    std::cin >> d >> n;
    
    double longestTime = 0.0;
    
    int j;
    
    for (j = 0; j < n; j++)
    {
      int k;
      int s;
      
      std::cin >> k >> s;
      
      double distanceToGo = (double)(d - k);
      double speed = (double) s;
      
      double timeTaken = distanceToGo / speed;
      
      if (timeTaken > longestTime)
      {
        longestTime = timeTaken;
      }
    }
    
    double distance = (double) d;
    double requiredSpeed = distance / longestTime;
    
    std::cout << "Case #" << (i + 1) << ": " << std::setprecision(17) << requiredSpeed << std::endl;
  }
}
