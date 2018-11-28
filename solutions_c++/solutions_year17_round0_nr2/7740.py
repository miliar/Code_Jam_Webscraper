#include <bits/stdc++.h>
#include <string>
using namespace std;

bool tidy(string s,int len)
{
	for(int i=0;i<len-1;i++)
	{
		if(s[i]>s[i+1])
			return false;
	}
	return true;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	int count=1;
	while(count<=t)
	{
		cout << "Case #" << count << ": ";
		long long int n;
		cin >> n;
		string s="";
		while(n>0)
		{
			int val=n%10;
			if(val==0)
				s+='0';
			else if(val==1)
				s+='1';
			else if(val==2)
				s+='2';
			else if(val==3)
				s+='3';
			else if(val==4)
				s+='4';
			else if(val==5)
				s+='5';
			else if(val==6)
				s+='6';
			else if(val==7)
				s+='7';
			else if(val==8)
				s+='8';
			else if(val==9)
				s+='9';
			n/=10;
		}
		reverse(s.begin(),s.end());
		int len=s.size();
		if(len==1)
		{
			cout << s << "\n";
		}
		else
		{
			bool flag=false;
			bool val[len];
			memset(val,false,sizeof(val));
			while(!flag)
			{
				if(tidy(s,len))
					flag=true;
				else
				{
					for(int i=0;i<len-1;)
					{
						if(s[i]>s[i+1])
						{
							if(val[i]==true)
							{
								if(s[i+1]=='0')
									s[i+1]='9';
								else if(s[i+1]=='1')
									s[i+1]='0';
								else if(s[i+1]=='2')
									s[i+1]='1';
								else if(s[i+1]=='3')
									s[i+1]='2';
								else if(s[i+1]=='4')
									s[i+1]='3';
								else if(s[i+1]=='5')
									s[i+1]='4';
								else if(s[i+1]=='6')
									s[i+1]='5';
								else if(s[i+1]=='7')
									s[i+1]='6';
								else if(s[i+1]=='8')
									s[i+1]='7';
								else if(s[i+1]=='9')
									s[i+1]='8';
							}
							else
							{
								val[i]=true;
								val[i+1]=true;

								if(s[i+1]=='0')
									s[i+1]='9';
								else if(s[i+1]=='1')
									s[i+1]='0';
								else if(s[i+1]=='2')
									s[i+1]='1';
								else if(s[i+1]=='3')
									s[i+1]='2';
								else if(s[i+1]=='4')
									s[i+1]='3';
								else if(s[i+1]=='5')
									s[i+1]='4';
								else if(s[i+1]=='6')
									s[i+1]='5';
								else if(s[i+1]=='7')
									s[i+1]='6';
								else if(s[i+1]=='8')
									s[i+1]='7';
								else if(s[i+1]=='9')
									s[i+1]='8';	

								if(s[i]=='0')
									s[i]='9';
								else if(s[i]=='1')
									s[i]='0';
								else if(s[i]=='2')
									s[i]='1';
								else if(s[i]=='3')
									s[i]='2';
								else if(s[i]=='4')
									s[i]='3';
								else if(s[i]=='5')
									s[i]='4';
								else if(s[i]=='6')
									s[i]='5';
								else if(s[i]=='7')
									s[i]='6';
								else if(s[i]=='8')
									s[i]='7';
								else if(s[i]=='9')
									s[i]='8';

							}
						}
						else
							i++;
					}
				}
			}
			bool flag1=false;
			for(int i=0;i<len;i++)
			{
				if(s[i]=='0' && flag1==false)
					continue;
				else
					cout << s[i];
			}
			cout << endl;
		}

		cerr << "Test Case " << count << " Solved in " << double(clock())/double(CLOCKS_PER_SEC) << endl;
		count++;
	}
	return 0;
}