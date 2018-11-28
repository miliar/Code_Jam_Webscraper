#include <iostream>
#include <sstream>

using namespace std;


// Decreases x to the nearest tidy number
// Returns the tidy number
string tidy(unsigned long int num)
{
  bool isTidy = true;
  string x;

  do
  {
    x = "";
    ostringstream xin;
    xin << num;
    x += xin.str();

    isTidy = true;
    
    // Check tidyness
    for(int i = 0; i < x.length() - 1; i ++)
    {
      // Not tidy
      if(x.at(i) > x.at(i + 1))
      {
        isTidy = false;
        break;
      }
    }

    if(!isTidy)
    {
      num --;
    }
  }while(!isTidy);

  return x;
}

int main()
{
  int numTrials = 0;
  unsigned long int num = 0;
  // Get input
  cin >> numTrials;
  // Repeat number of cases
  for(int i = 0; i < numTrials; i ++)
  {
    // Get number
    cin >> num;
    // Output tidy number
    cout << "Case #" << i+1 << ": " << tidy(num) << endl;
  }
}
