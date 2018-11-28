#include <algorithm>
#include <stdio.h>
#include <iostream>
#include <stack>
#include <utility>
#include <math.h>
#include <map>
#include <vector>
#include <queue>
using namespace std;

#define loop(i,a,b) for(i=a;i<b;i++)
#define lp(i,n) for(i=0;i<n;i++)
#define lli long long int
#define us unsigned
#define tup2 pair <int,int>
#define tup3 pair <tup2,int>
#define MAX(a,b) ((a)>=(b)?a:b)
#define MIN(a,b) ((a)<=(b)?a:b)
#define X first
#define Y second
#define pb push_back
#define pob pop_back
#define iter(v) for(auto it = v.begin(); it != v.end(); it++)
#define abs(x) (x>0?(x):(-(x)))
#define maxn 100005

int main()
{
	std::ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for( int ii = 1; ii<=t; ii++)
	{
		lli n,k;
		cin >> n >> k;
		k--;

		map<lli,lli> mymap;
		mymap.insert(make_pair(n,1));
		lli ar[2];
		while(1)
		{
			auto it = mymap.end();
			it--;
			//cout << it->X <<" " << it->Y<<" " << k << endl;
			ar[0] = (it->X)/2; ar[1] = (it->X - 1)/2;

			if(k >= it->Y)
			{
				k -= it->Y;
				int i;
				lp(i,2)
				{
					auto it2 = mymap.find(ar[i]);
					if(it2!=mymap.end())
						it2->Y +=it->Y;
					else
						mymap.insert(make_pair(ar[i], it->Y));
				}
				mymap.erase(it);
				
			}
			else
			{
				cout << "Case #" << ii <<": " << ar[0] <<" " << ar[1];
				cout << endl;
				break;
			}
		}
	}
	return 0;
}