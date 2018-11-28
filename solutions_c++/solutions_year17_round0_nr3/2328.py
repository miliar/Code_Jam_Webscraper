#include <iostream>
#include <fstream>
using namespace std;

void solve(int t)
{
	long long N,K;
	cin >> N >> K;
	long long vLow = N;
	long long numLow = 1;
	long long numHigh = 0;
	while(1)
	{
		if(K <= numHigh)
		{
			cout << "Case #" << t << ": " << (vLow+1)/2 << ' ' << (vLow+1+1)/2-1 << '\n';
			return;
		}
		else if(K <= numHigh + numLow)
		{
			cout << "Case #" << t << ": " << (vLow)/2 << ' ' << (vLow+1)/2-1 << '\n';
			return;
		}
		else
		{
			long long newLow,newNumLow,newNumHigh;
			if(vLow%2 == 0)
			{
				newLow = vLow/2 - 1;
				newNumLow = numLow;
				newNumHigh = numLow + 2*numHigh;
			}
			else
			{
				newLow = vLow/2;
				newNumLow = 2*numLow + numHigh;
				newNumHigh = numHigh;
			}
			K -= numHigh + numLow;
			vLow = newLow;
			numLow = newNumLow;
			numHigh = newNumHigh;
		}
	}
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
		solve(i);
}
