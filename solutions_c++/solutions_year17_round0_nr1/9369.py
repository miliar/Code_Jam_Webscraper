#include <string>
#include <iostream>

using namespace std;

int numberOfFlips(string s, int amount);

int main(){
	int cases;
	cin >> cases;
	for(int i=1; i<=cases; i++)
	{
	  string s = "";
	  cin >> s;
	  int amount = 0;
	  cin >> amount;
	  int solution = numberOfFlips(s, amount);
	  if(solution == -1)
		cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	   else
		cout << "Case #" << i << ": " << solution << endl;   
	}
		
	return 0;
}

int numberOfFlips(string s, int amount)
{
  
  int flips = 0;
  
  // base case (all +)
  std::size_t found = s.find("-");
  if (found==std::string::npos)
    return flips;

  for(int i=0; i< s.size(); i++)
  {
	  if(s[i] == '-' && (i + amount) <= s.size())
	  {
		int tempAmount = amount;
		while(tempAmount != 0)
		{
		  if(s[(i + tempAmount) - 1] == '-')
			  s[(i + tempAmount) - 1] = '+';
		  else if(s[(i + tempAmount) - 1] == '+')
			  s[(i + tempAmount) - 1] = '-';
		  tempAmount--;
		}
		flips++;  
	  }
  }
  
  // base case (all +)
  found = s.find("-");
  if (found==std::string::npos)
    return flips;
  else
	return -1;

}