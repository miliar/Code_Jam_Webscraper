#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
	int n;
	cin >> n;
	vector<int> vs(6);
	for(int i = 0; i < 6; i++)
	{
	  cin >> vs[i];
	}
	int r = vs[0];
	int b = vs[4];
	int y = vs[2];

	vector<pair<int, char>> ss = {make_pair(r, 'R'), make_pair(b, 'B'), make_pair(y, 'Y')};
	sort(ss.begin(), ss.end(), greater<pair<int, char>>());
	
	if(ss[0].first * 2 > (r + b + y))
	{
	  cout << "Case #" << t << ": IMPOSSIBLE" << endl;
	}
	else
	{
	  cout << "Case #" << t << ": ";
	  while(ss[0].first > ss[1].first)
	  {
		cout << ss[0].second << ss[1].second;
		ss[0].first--; ss[1].first--;
		
		if(ss[0].first > 0 && ss[2].first > 0){
		  cout << ss[0].second << ss[2].second;
		  ss[0].first--; ss[2].first--;
		}
	  }
	  const int count = ss[2].first;
	  for(int i = 0; i < count; i++)
	  {
		cout << ss[0].second << ss[1].second << ss[2].second;
		ss[0].first--;
		ss[1].first--;
		ss[2].first--;
	  }
	  const int count2 = ss[1].first;
	  for(int i = 0; i < count2; i++)
	  {
		cout << ss[0].second << ss[1].second;
		ss[0].first--;
		ss[1].first--;
	  }
	  cout << endl;
	}
  }
}
