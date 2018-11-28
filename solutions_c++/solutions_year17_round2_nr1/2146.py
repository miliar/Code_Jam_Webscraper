// Programmer: Tanner Winkelman
// 4/22/2017
// Purpose: Google Code Jam Round 1B 2017 Problem A


#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main()
{
  
  long T;
  cin >> T;
  
  for( long k = 0; k < T; k++ )
  {
    long D;
    long N;
    
    cin >> D >> N;
    
    long Ki;
    long Si;
    
    double latestFinishTime = 0;
    
    for( long i = 0; i < N; i++ )
    {
      cin >> Ki >> Si;
      if( static_cast<double>(D - Ki) / Si > latestFinishTime )
        latestFinishTime = static_cast<double>(D - Ki) / Si;
    }
    
    double maxSpeed = (D / latestFinishTime);
    
    cout.setf(ios::fixed);
    cout.setf(ios::showpoint);
    cout.precision(6);
    cout << "Case #" << (k+1) << ": " << maxSpeed << endl;
    
  }
  
  return 0;
}
