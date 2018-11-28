#include <iostream>

using namespace std;

bool is_happy(const string &s)
{
  for(auto ch : s)
  {
	if(ch == '-') return false;
  }
  return true;
}

int main()
{
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
	string line;
	int k;
	cin >> line >> k;

	int flip_count = 0;
	for(int i = 0; i < line.length() - k + 1; i++)
	{
	  if(line[i] == '-')
	  {
		flip_count++;
		// flip
		for(int j = i; j < i + k; j++)
		{
		  line[j] = (line[j] == '-' ? '+' : '-');
		}
	  }
	}
	if(is_happy(line))
	{
	  cout << "Case #" << t << ": " << flip_count << endl;
	}
	else
	{
	  cout << "Case #" << t << ": IMPOSSIBLE" << endl;
	}
  }
}
