#include <iostream>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int t;
	cin>>t;
	int case_no = 1;
	while(t--)
	{
		string s;

		cin >> s;
		int k,ans=0,i;
		cin >>k;
		for(i=0;i<=s.size()-k; i++)
		{
			if(s[i] == '+')
				continue;
			ans++;
			for(int j=i; j-i<k; ++j)
			{
				if(s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
		}
		cout << "Case #" << case_no++ <<": ";
		auto it = s.find_first_of('-');
		if(it==s.npos)
			cout<<ans<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
	}
}
