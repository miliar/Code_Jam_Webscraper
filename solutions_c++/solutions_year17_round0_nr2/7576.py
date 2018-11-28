#include <bits/stdc++.h>
#define pb push_back
using namespace std;
typedef long long int ll;

int main(int argc, char const *argv[])
{
	int t,c=1;
	cin>>t;
	ofstream ofile;
	ofile.open("out.txt",ios::out);
	while(t--)
	{
		string s;
		cin>>s;

		int p=-1;
		for(int i=1;i<s.size();i++)
		{
			if(s[i]<s[i-1])
			{
				p=i-1;
				break;
			}
		}
		if(p==-1)
			ofile<<"Case #"<<c<<": "<<s<<endl;
		else
		{
			char c1=s[p];
			s[p]--;
			p--;
			while(s[p]==c1 && p>=0)
			{
				s[p]--;
				p--;
			}
			if(p==-1)
			{
				if(s[0]=='0')
				{
					string s1="";
					for(int z=0;z<s.size()-1;z++)
						s1+="9";
					s=s1;
				}
			}

			for(int z=p+2;z<s.size();z++)
				s[z]='9';

			// s[p]-=1;
			// // cout<<" here for case "<<c<<" string "<<s<<" and p "<<p<<endl;
			// if(p>0 && s[p-1]==(s[p]+1))
			// {
			// 	p--;
			// 	while(s[p]==s[p-1] && p>0)
			// 	{
			// 		s[p]--;
			// 		p--;
			// 		if(p==1)
			// 			s[0]--;
			// 	}
			// 	string s1="";

			// 	if(p==0)
			// 	{
			// 		for(int l=0;l<s.size()-1;l++)
			// 			s1+="9";
			// 		s=s1;
			// 	}
			// 	else
			// 		s[p]-=1;
			// }
			// // cout<<" here for case "<<c<<" string "<<s<<" and p "<<p<<endl;
			// for(int z=p+1;z<s.size();z++)
			// 	s[z]='9';


			// while(s[p]=='1' && p>0)
			// {
			// 	s[p]='0';
			// 	p--;
			// }
			// if(p==0)
			// {
			// 	string s1="";
			// 	for(int z=0;z<s.size()-1;z++)
			// 		s1+="9";
			// 	ofile<<"Case #"<<c<<": "<<s1<<endl;
			// }
			// else
			// {
			// 	s[p]-=1;
			// 	for(int z=p+1;z<s.size();z++)
			// 		s[z]='9';
			// 	ofile<<"Case #"<<c<<": "<<s<<endl;
			// }

			ofile<<"Case #"<<c<<": "<<s<<endl;

		}
		c++;
	}
	return 0;
}