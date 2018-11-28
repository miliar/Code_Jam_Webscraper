#include <bits/stdc++.h>
#include <string>
using namespace std;

bool work(string s)
{
	for(int i = 0; i < s.size()-1; i++)
		if(s[i]>s[i+1]) return true;
	
	return false;
}

/*string to_string(int N)
{
	stringstream ss;
	ss<<N;
	return ss.str();
}*/

int main()
{
	int T = 0;	
	string N;
	cin>>T;
	for(int t = 1; t <= T ; t++)
	{
		long long unsigned inp;
		cin>>inp;
		N = std::to_string(inp);
		//cout<<work(N)<<endl;		
		cout<<"Case #"<<t<<": ";
		//printf("%3d : ",t);
		if(work(N))
		{
			string ans = "";
			bool nine = false;
		
			for(int i = 0, l = N.size(); i < l; i++)
			{
				if(nine) ans += '9';		
				else if(N[i] < N[i+1]) ans += N[i];
				else {
					
					if(N[i] != '1')
						ans += (N[i]-1);
					nine = true;
				}
			}	
			cout<<ans<<endl;
		
		}else cout<<N<<endl;
	
	}

	return 0;
}