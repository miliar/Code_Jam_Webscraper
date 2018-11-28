#include<iostream>
#include<math.h>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
vector<int> vect(unsigned long long int tidy)
{
  unsigned long long int tT = tidy;
  vector<int> tV;
  while (tT > 0)
    {
      tV.insert(tV.begin(), tT % 10);
      tT /= 10;
    }
  return tV;
}
int main()
{
  int T;
  cin >> T;
  vector<unsigned long long int> ti(T);
  for (int i = 0; i < T; i++)
    cin >> ti[i];
  for (int k = 0; k < T; k++)
    {
      vector<int> tV = vect(ti[k]);
      for (size_t i = 1; i < tV.size(); )
	{
	  if (tV[i] >= tV[i-1])
	    {
	      i++;
	    }
	  else
	    {
	      tV[i - 1] -= 1;
	      for (size_t j = i; j < tV.size(); j++)
		{
		  tV[j] = 9;
		}
	      i = 0;
	    }
	}
      cout << "Case #" << k + 1 << ": ";
      for (size_t i = 0; i < tV.size(); i++)
	  if (tV[i] != 0)
	    cout << tV[i];
      cout << endl;
    }
}
