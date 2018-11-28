#include<bits/stdc++.h>
using namespace std;
int sorted(unsigned long long k);
int main()
{
	int t;
	string s;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		
  unsigned long long n=std::stoll(s,0,10);

	//cout<<"string"<<s1;
	for(unsigned long long k=n;k>=0;k--)
	{
	   if(sorted(k))
	   {
	       cout<<"Case #"<<i<<": "<<k<<endl;
	       break;
	   }
	}
	
		
	}
}
int sorted(unsigned long long k)
{
    
	string s1=to_string(k);
	string s2=s1;
	sort(s1.begin(),s1.end());
	if(s2==s1)
	{
	    return 1;
	}
	else
	{
	    return 0;
	}
}

