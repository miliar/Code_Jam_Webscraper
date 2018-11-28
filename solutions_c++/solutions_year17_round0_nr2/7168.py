#include <bits/stdc++.h>
using namespace std;

int main(int arc,char * argv[]){

	 freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
	int  t;
	cin >> t;
	for (int k = 0; k < t; ++k)
	{    ios::sync_with_stdio(false);
         cin.tie(NULL);
		string s;
		
		cin >> s;
		for (int j = s.size()-1; j > 0 ; --j)
		{ 	
			if (s[j] < s[j-1])
			{	s[j-1]--;	
				int i=j;
				 while ((i < s.size()) && ( s[i]!= '9'))
				{				
					s[i] = '9';
				    i++;
				}
			}
		}
		if (s[0]=='0')
			s.erase(0,1);
		
		
		cout << "Case #" << (k+1) << ": " << s << endl;
	}
}