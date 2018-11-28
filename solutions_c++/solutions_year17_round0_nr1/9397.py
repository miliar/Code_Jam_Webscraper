#include<bits/stdc++.h>
using namespace std;
#define ll long long
int fn(string t,int k)
{
	string s=t;
	int n = s.length();
	int ans1=0,ans2=0;
	for(int i=0;i<n;)
	{
		while(s[i]=='+')
			i++;
		int flag2=0;
		for(int j=i;j<i+k && i+k-1<n;j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else if(s[j]=='+')
						s[j]='-';
					flag2=1;
				}
				ans1+=flag2;
				i++;
	}
	// int flag=0;
	// for(int i=n-k;i<n;i++)
	// 		{
	// 			if(s[i]=='-')
	// 				flag=1;
	// 			s[i]='+';
	// 		}
	// ans1+=flag;
	for(int i=0;i<n;i++)
		{
			if(s[i]!='+')
				ans1 = -1;
		}
		//cout<<s<<endl;
	
	s=t;
	for(int i=n-1;i>=0;)
	{
		while(s[i]=='+')
		{
			i--;
		}
		int flag2=0;
		// cout<<i<<endl;
		// cout<<s<<endl;
		for(int j=i;j>i-k && i-k+1>=0;j--)
		{
			if(s[j]=='-')
				s[j]='+';
			else if(s[j]=='+')
				s[j]='-';
			flag2=1;
		}
		ans2+=flag2;
		i--;
	}
			// flag=0;
			// for(int i=0;i<k;i++)
			// {
			// 	if(s[i]=='-')
			// 		flag=1;
			// 	s[i]='+';
			// }
			// ans2 += flag;
		
	for(int i=0;i<n;i++)
		{
			if(s[i]!='+')
				ans2 = -1;
		}
		//cout<<s<<endl;
		if(ans1==-1 && ans2==-1)
			return -1;
		else if(ans1==-1)
			return ans2;
		else if(ans2==-1)
			return ans1;
		else
			return min(ans1,ans2);
}
int main()
{
	int t=1,lim;
	cin>>lim;
	while(t<=lim)
	{
    	//Enter your code here
    	string s;
		int n;
		cin>>s>>n;
		cout<<"Case #"<<t<<": ";
		int ans = fn(s,n);
		if(ans==-1)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<ans<<endl;
		t++;
	}

}

//How to compile & run
//	g++ readme.cpp 
//	./a.out <in.txt> out.txt
