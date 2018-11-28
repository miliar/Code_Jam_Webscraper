#include <bits/stdc++.h>
using namespace std;

bool check(string s)
{
	for(int i = 0 ; i < s.size() ; i++) if(s[i] == '-') return false;
	return true;
}

string move(string s, int k, int pos)
{
	for(int i = 0 ; i < k; i++)
		s[i + pos] = (s[i + pos] =='+'?'-':'+');
	return s;
}

int main()
{
	int t, ca = 1;;
	cin>>t;
	while(t--)
	{
		int k;
		string s;
		cin>>s>>k;

		map<string,bool> sec;

		bool flag = true;
		int count =0;
		if(!check(s))
		{
			flag = false;
			for(int i = 0 ; i < (s.size() - (k - 1) ); i++)
			{
				
				if(s[i] == '-')
				{

					count++;
					s = move(s,k,i);
					//cout<<i<<' '<<s<<endl;
					if(check(s))
					{
						flag = true;
						break;
					}
				}
			}
		}

		cout<<"Case #"<<ca<<": ";
		if(!flag) cout<<"IMPOSSIBLE\n";
		else cout<<count<<'\n';
		ca++;
	}
	return 0;
}