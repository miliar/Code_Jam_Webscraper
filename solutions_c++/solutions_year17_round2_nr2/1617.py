#include<bits/stdc++.h>
#define ll long long int
using namespace std;
FILE *in=freopen("in.txt","r",stdin);
FILE *out=freopen("out.txt","w",stdout);

int main()
{
	int t;
	cin>>t;
    for(int m=1;m<=t;m++)
    {
    	int n,r,o,y,g,b,v;
    	cin>>n>>r>>o>>y>>g>>b>>v;
    	vector<string> vec;
		while(n>0)
    	{
    		if(r>=b&&r>=y&&r!=0)
    		{
    			vec.push_back("R");
    			r--;
    			if(y>=b&&y!=0)
    			{
    				vec.push_back("Y");
    				y--;
				}
				else if(b>y&&b!=0)
    			{
    				vec.push_back("B");
    				b--;
				}
			}
			else if(y>=b&&y>r)
			{
				vec.push_back("Y");
				y--;
				if(r>=b&&r!=0)
    			{
    				vec.push_back("R");
    				r--;
				}
				else if(b>r&&b!=0)
    			{
    				vec.push_back("B");
    				b--;
				}
			}
			else if(b>y&&b>r)
			{
				vec.push_back("B");
				b--;
				if(r>=y&&r!=0)
    			{
    				vec.push_back("R");
    				r--;
				}
				else if(y>r&&y!=0)
    			{
    				vec.push_back("Y");
    				y--;
				}
			}
			n=n-2;
    	}
    	if(r!=0)
    	vec.push_back("R");
    	if(y!=0)
    	vec.push_back("Y");
    	if(b!=0)
    	vec.push_back("B");
    	
    	if(vec[0]==vec[vec.size()-1]&&vec[vec.size()-1]!=vec[vec.size()-3])
    	{
    		string temp;
    		temp=vec[vec.size()-2];
    		vec[vec.size()-2]=vec[vec.size()-1];
    		vec[vec.size()-1]=temp;
		}
    	cout<<"Case #"<<m<<": ";
    	if(vec[0]==vec[vec.size()-1]||(r+b+y)!=0)
    		cout<<"IMPOSSIBLE";
    	 	
    	else
		{
		for(int i=0;i<vec.size();i++)
		cout<<vec[i];
		}
		
		cout<<endl;
	
	}
	return 0;
}
