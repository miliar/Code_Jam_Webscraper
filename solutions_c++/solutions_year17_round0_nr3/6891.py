#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <limits.h>
#include <set>
#include <functional>
using namespace std;

#define all(v)     (((v).begin()),((v).end()))
#define sz(v)      ((int)((v).size()))
#define clr(v,d)   memset(v,d,sizeof(v))
#define rep(i,v)   for(int i=0;i<sz(v);++i)
#define lp(i, n)   for (int i = 0; i < (int)(n);++i)
#define lpi(i,j,n) for(int i=(j);i<(int)(n);++i)
#define lpd(i,j,n) for(i=(j);i>=(int)(n);--i)

typedef long long ll;


int main()
{

	ifstream fin("C-small-1-attempt0.in");
	ofstream fout("C-small-1-attempt0.out");
	 
	int T;
	ll kUsers,N,minL,maxL;
	unsigned int j;
	int * stalls;
	fin >> T;
	std::multiset <ll, std::greater<ll>> consectiveUnoccupied;
 	lp(i, T)
	{

		fin >> N >> kUsers;
		if(N==kUsers)
			fout << "Case #" << i + 1 << ": 0 0" << endl;
		else if (kUsers == 1)
		{
				if (N % 2 == 0)
					fout << "Case #" << i + 1 << ": " << N / 2 << " " << N / 2 - 1 << endl;
				else
					fout << "Case #" << i + 1 << ": " << N / 2 << " " << N / 2 << endl;
		}
		else
		{

			consectiveUnoccupied.clear();
			//Init the stalls
			/*stalls = new int[N + 2];
			for (int stCount = 0; stCount < N + 2; stCount++)
				stalls[stCount] = 0;
			stalls[0] = 1;
			stalls[N + 1] = 1;
			*/
			////
			//choose the half of the largest consecutive zeros area 
			ll free;
			consectiveUnoccupied.insert(N);//initially all are free

			for (int users = 0; users < kUsers; users++)
			{
				free =* consectiveUnoccupied.begin();
			
				consectiveUnoccupied.erase(consectiveUnoccupied.begin());
				if (free % 2 == 0)
				{
					consectiveUnoccupied.insert(free / 2 - 1);
				}
				else
				{
					consectiveUnoccupied.insert(free / 2);
				}
				consectiveUnoccupied.insert(free / 2);
			}
			//last free 
			maxL = free / 2; 
			if(free%2==0)
				minL = free / 2-1;
			else
				minL = free / 2;

			fout << "Case #" << i + 1 << ": " << maxL << " " << minL << endl;
		}
	}
	return 0;
}