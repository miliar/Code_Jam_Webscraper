#include<bits/stdc++.h>
#define INF LONG_MAX-100
#define for(p,x,y) for(int p=x;p<y;p++)
#define in(a) scanf("%d",&a);
#define INPUT
typedef long long ll;
using namespace std;
	bool isvalid(string s)
	{
		int l=s.length();
		for(i,0,(l-1))
		{
			if(s[i]>s[i+1])
             return false;
		}
		return true;	
		}
	string tidy(string s)
	{
		int l=s.length();
		for(i,0,(l-1))
		{
		if(s[i]>s[i+1])
		{
			s[i]--;
			int p=i+1;
			for(j,p,l)
			s[j]='9';
			break;
		}
		}
		if(isvalid(s))
			return s;
		else
		return tidy(s);
	}

int main()
{

    #ifdef INPUT
       freopen("input.cpp", "r", stdin);
       freopen("output.cpp", "w",stdout);
   	#endif
    int t;
    cin>>t;
    string s1;
    for(i,0,t)
    {
    	string s;
    	cin>>s;
    	s1=tidy(s);
    	if(s1[0]=='0')
    	{
    	cout<<"Case #"<<(i+1)<<": ";
    	for(j,1,s1.length())
    	cout<<s1[j];
    	cout<<endl;
    }
    else
    	cout<<"Case #"<<(i+1)<<": "<< s1<<endl;
	}
	return 0;
}

