#include <iostream>
#include <algorithm>
using namespace std;
int T,K;
string S,a,b;
int flip1 = 0, flip2 = 0;

void getAns(string &inp, string &S, int &flip)
{
	for(int i = 0; i < S.length(); i++)
	{
		if(inp[i] == '-' && i + K <= S.length())
		{
			int ctr = 0;
			int k = i;
			while(ctr < K)
			{
				if(inp[k] == '-')
					inp[k] = '+';
				else
					inp[k] = '-';
				k++;
				ctr++;
			}
			
			//cout << inp << endl;
			flip++;
		}
	}
}

bool isPositive(string inp)
{
	for(int i = 0; i < inp.length(); i++)
	{
		if(inp[i] == '-')
			return false;
	}
	return true;
}

int main()
{
	
	int cs = 1;
	cin >> T;
	
	while(T--)
	{
		cout << "Case #" << cs++ << ": ";
		flip1 = 0;
		 flip2 = 0;
		cin >> S >> K;
		a = b = S;
		reverse(b.begin(),b.end());
		int ans = 9999;
		getAns(a,S,flip1);
		if(isPositive(a))
			ans = flip1;
		getAns(b,S,flip2);
		if(isPositive(b))
			ans = min(flip1,flip2);
		
		if(ans == 9999)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
}
