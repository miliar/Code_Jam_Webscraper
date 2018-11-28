/*
  @author Himanshu Dixit
  hudixt@gmail.com
 */

#include<iostream>
#include<math.h>
#include<vector>
#include<algorithm>
#include<string>
#include<stack>
using namespace std;

// Lets' vectorize the number using this function.

vector<int> vectorI(unsigned long long int tidyNo)
{
  unsigned long long int taT = tidyNo;
  vector<int> taV;
  while (taT > 0)
    {
      taV.insert(taV.begin(), taT % 10); taT /= 10;
    }
  return taV;
}

// Main function
int main()
{
  long long int TestCase;
  cin >> TestCase;
  vector<unsigned long long int> tai(TestCase);
  for (int i = 0; i < TestCase; i++)
    cin >> tai[i];
  for (int a = 0; a < TestCase; a++)
    {
      vector<int> taV = vectorI(tai[a]);
      for (size_t i = 1; i < taV.size(); )
	{
	  if (taV[i] >= taV[i-1])
	      i++;
	  else
	    {
	      taV[i - 1] -= 1;
	      for (size_t j = i; j < taV.size(); j++)
		  taV[j] = 9;
	      i = 0;
	    }
	}
      // Print in the standard format
      cout << "Case #" << a + 1 << ": ";
      // Run the loop
      for (size_t i = 0; i < taV.size(); i++) {
	if (taV[i] != 0){
	  cout << taV[i];
	}
      }

      cout << endl;
    }
}
