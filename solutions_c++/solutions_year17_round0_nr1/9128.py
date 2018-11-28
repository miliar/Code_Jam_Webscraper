#include<iostream>
#include<algorithm>
#include<vector>
#include <fstream>
using namespace std;

int check(string s, int k)
{	int cnt=0;
	//string s1="+", s2="-";
	for(int i=0;i<s.size();i++)
	{	//cout << s[i] << endl;
		if(s[i]=='-')
		{	cnt++;
			//cout << "m " << endl;
			for(int j=i;j<i+k && (i+k)<=s.size();j++)
			{   
				if(s[j]=='-')
				{
					s[j]='+';
				}
				else
				{
					s[j]='-';
				}

			}
			/*for(int i1=0;i1<s.size();i1++)
				{
					cout << s[i1];
				}cout << endl;*/
		}
	}
	
	int fl=1;
	for(int i=0;i<s.size() && fl==1;i++)
	{	//cout << s[i];
		if(s[i]=='-')
		{
			fl=-1;
		}	
	}	
	//cout << endl;
	if(fl==-1)
		return fl;
	else
		return cnt;
}

int main()
{
	int t;
	cin >> t;
	int k1=1;
	while(t--)
	{
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans;
		ans=check(s, k);
		
		if(ans==-1)
		{
			cout << "Case #" << k1++ << ": " <<"IMPOSSIBLE" << endl;
		}
		else
		{
			cout <<	"Case #" << k1++ << ": " << ans << endl;
		}
		
	}
	
	return 0;
}
