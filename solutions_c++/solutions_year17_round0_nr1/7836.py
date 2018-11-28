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
	int m;
	int ans ;
	for(int i=0;i<T;i++){
		ans = 0;
		cin>>s>>m;
		while( m <= s.size() ){
			if(s[0] == '-' )
				{
					for(int j = 0 ; j < m ; j++)
					{
						if( s[j] == '-' )
							s[j] = '+';
						else 
							s[j]='-';
					}
					ans++;
				}
			s = s.substr(1,s.size());
		}
		bool flag = true;
		for(int j=0;j<s.size();j++)
			if(s[j]=='-')
			{
				flag = false;
				break;
			}
		if(flag)
			cout<<"Case #" << i+1 <<": "<<ans<<endl;
		else
			cout<<"Case #" << i+1 <<": "<<"IMPOSSIBLE"<<endl;

	}
	return 0;
}

