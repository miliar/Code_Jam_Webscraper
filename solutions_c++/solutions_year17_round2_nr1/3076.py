#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
  int c;

  cin >> c >> ws;

  for (int i = 0; i < c; i++)
  {
     long d, n;
     double slowest=0;
     double sd, spos;
     cin >> d >> ws >> n >> ws;
     for(long j=0; j < n; j++){
       double jpos, jspeed;
       cin >> jpos >> ws >> jspeed >> ws;

       double t = (d - jpos) / jspeed;
       if(t > slowest){
         slowest = t;
       }

     }
      cout << "Case #" << i + 1 << ": " << std::setprecision(6) << std::fixed <<  d / slowest << endl;
  }

  return 0;
}