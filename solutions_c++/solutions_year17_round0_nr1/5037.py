// ID: fatih
// PROB: pancake
// LANG: c++

// Greedy: O(N)
// Whenever position x is 1, flip x+1
// There are two possibilities:
//   start flipping at position 0 or 1
#include <iostream>

using namespace std;

int n,t,k;
string pancake;

// flip operation
void flip(int x)
{
	for (int i=x; i<x+k; i++)
		pancake[i]=pancake[i]=='-' ? '+' : '-';
}

// greedy solution
// whenever encounters 1 at position x, flips x+1
int greedy()
{
	int fcount=0;

	for (int i=0; i<n-k+1; i++)
		if (pancake[i]=='-')
		{
			flip(i);
//			cout << fcount << ": " << pancake << endl;
			fcount++;
		}

	for (int i=n-k+1; i<n; i++)
		if (pancake[i]=='-') return -1;	// invalid solution
	return fcount;
}

int main()
{
	cin >> t;


	for (int i=0; i<t; i++)
	{
		cin >> pancake >> k;
		n=pancake.length();

		int ans=greedy();
		cout << "Case #" << i+1 << ": ";
		if (ans==-1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
}
