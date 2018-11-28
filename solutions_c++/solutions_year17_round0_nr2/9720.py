#include <bits/stdc++.h>
using namespace std;

string s ;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("redir.txt", "w", stdout);
	int t , h ;
	cin >> t ;
	h=t;
	while(t--) 
	{
		cin >> s ;
		int counter = 0 ;
		for(int i = 1 ; i < s.size() ;i++ )
		{
			if(s[i-1] == s[i])
			{
				counter++;
			}
			else if(s[i-1]< s[i] )
				counter=0;
			else
			{
				for(int j = s.size()-1  ; j > i - (counter+1) ; j--)
					s[j]='9';
				s[i-counter-1]--;
				break;
			}
		}
		cout << "Case #" << h-t << ": " ;
		int flag = 0 ;
		for(int i = 0 ; i < s.size() ; i++ )
		{
			if(!flag&&s[i]=='0')
				continue;
			else
			{
				flag = 1 ;
				cout << s[i] ;
			}
		}
		cout << endl;
	}
}
