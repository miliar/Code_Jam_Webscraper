#include <bits/stdc++.h>
#define ll long long 
using namespace std;

// Credits to: Peter Alexander for the improved code snippet
int solve(vector<bool> bits, int N)
{
  queue<int> flips;
  int moves = 0;

  for (int i = 0; i < bits.size(); ++i)
  {
    if (!flips.empty() && flips.front() <= i - N)
      flips.pop();

    if ((bits[i] ^ (flips.size() % 2 == 0)) == 1)
    {
      if (i > bits.size() - N)
        return -1; // IMPOSSIBLE

      moves++;
      flips.push(i);
    } 
  }

  return moves;
}
 
int main( ) {
   //freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
   
   int n, num;
   string s;
   cin >> n;
   for(int j=1; j<=n; j++){
   		cin >> s >> num;
   		vector<bool> bits;
   		for(int i=0; i<s.size(); i++){
   			if(s[i] == '-')
   				bits.push_back(false);
   			else
   				bits.push_back(true);
	   	}
	   	cout << "Case #" << j << ": ";
		int tmp = solve(bits, num);
		if(tmp == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << tmp << endl;		
	
   }
   
   return 0;
}
