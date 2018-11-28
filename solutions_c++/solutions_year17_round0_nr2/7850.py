#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>


using namespace std;

int main()
{
	freopen("in" ,"r" , stdin);
	freopen("out", "w", stdout );
	int T;
	cin>>T;
	string s;
	for(int i=0;i<T;i++){
		cin>>s;
		int p=-1;
		for(int j=0;j<s.size()-1;j++)
			if(s[j] > s[j+1])
			{
				p = j;
				break;
			}
		cout << "Case #" << i+1 << ": "; 
		if( p == -1 )
			 cout << stoll (s)<<endl;
		else{
			bool flag = false;
			for(int j = p ; j>0 ; j--)
				if( s[j] > s[j-1] )
				{
					flag = true;
					p = j;
					break;
				}
			if ( flag ){
				s[p] = s[p] - 1 ;
				for(int j = p+1 ; j<s.size() ; j++)
					s[j] = '9' ;
				 cout << stoll (s)<<endl;

			}
			else
			{
				s[0] = s[0] - 1;
				for(int j = 1 ; j<s.size() ; j++)
					s[j] = '9' ;
				 cout << stoll (s)<<endl;
			}
		}

	}
	return 0;
}

