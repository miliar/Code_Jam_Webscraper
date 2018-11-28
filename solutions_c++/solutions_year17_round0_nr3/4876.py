#include <bits/stdc++.h>
using namespace std;

const int N = 0;
int n , t , k;

int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;

	for(int q=1;q<=t;q++)
	{
		cin >> n >> k;
		multiset < int > s;
		s.clear();
		s.insert(n);
		int mx = n  , mn = n;
		
		while(k--)
		{
			int potato = *(s.rbegin());
			
			if( (potato-1)%2 )
			{
				s.insert((potato-1)/2);
				s.insert((potato-1)/2 + 1);
				mn = (potato-1)/2;
				mx = (potato-1)/2 + 1;
			}
			else
			{
				s.insert((potato-1)/2);
				s.insert((potato-1)/2);
				mn = mx = (potato-1)/2;
			}
			
			multiset<int>::iterator it = s.find(potato);
			s.erase(it);
			
		}
		
		printf("Case #%d: %d %d\n",q,mx,mn);
	}
}