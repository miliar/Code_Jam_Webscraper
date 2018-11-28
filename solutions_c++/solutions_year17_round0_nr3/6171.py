#include <bits/stdc++.h>
using namespace std;

int main(int arc,char * argv[]){
	ios::sync_with_stdio(false);
         cin.tie(NULL);
 freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
	int  t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{    
		long long n,k;
		cin >> n >> k;
		long long min,mymax;
		min= mymax =0;
		multiset<long long> s;
		
		for (long long j = 0; j < k; ++j)
		{	
			set<long long>::iterator it;
			mymax = n/2;
			min = n/2 -1 + n%2 ;
			s.insert(min);
			s.insert(mymax);
			it =  s.end();
			it--;
			n=*it;
			

			s.erase(it);
			
		
			if ((min == 0) &&( mymax == 0))
				break;

		}
	
		
		cout << "Case #" << (i+1) << ": " << mymax << " " << min << endl;
	}
}