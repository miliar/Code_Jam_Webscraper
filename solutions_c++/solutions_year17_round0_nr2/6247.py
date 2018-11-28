#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
	ll n,t;
	string s;
	cin>>t;
	for (int i = 1; i <= t; ++i)
	{
		cin>>n;
		
		s = to_string(n);
		//cout<<s[0]-'1'<<endl;;

		int temp =s.length();
		if(temp==1){
			cout<<"Case #"<<i<<": "<<n<<endl;
			continue;
		}
		
		while(temp--){
			int j=0;

		for (j= 0; j <= s.length()-2; ++j)
		{
		//	cout<<s[j]<<endl;
			if(s[j]-s[j+1] >0){
				
				s[j]= (s[j]-1);
				
				for (int k = j+1; k < s.length(); ++k)
				{
					s[k]='9';
					//cout<<s;
				}

			}
		}

	}
	
	ll ans=strtoll(s.c_str(), NULL, 10);
	cout<<"Case #"<<i<<": "<<ans<<endl;

	}
	return 0;
}
