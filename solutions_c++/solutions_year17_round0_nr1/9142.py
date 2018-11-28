#include<iostream> 
#include<vector>
#include <fstream>
using namespace std;
bool check(string s)
{
	int i=0;
	while(s[i])
	{
		if(s[i]=='-')
		return false;
		i++;
	}
	return true;
}
main()
{
FILE *fp=freopen("A-large.in","r",stdin);
   freopen("output_file_name3.txt","w",stdout);
long long int x;

while(!feof(fp))
{
string n;
int k;
int count,c;
cin>>x;
for(int i=0;i<x;i++)
{
	c=0;
	count=0;
	cin>>n>>k;
	while(n[c])
	{
		if(n[c]=='-')
		{
				for(int j=0;j<k;j++)
				{
					if(k+c<=n.length())
					{
		         if(n[j+c]=='-'	)
				 n[j+c]='+';
				 else
				 n[j+c]='-';
			}
			
				}
				count++;
	}
	c++;
//	cout<<endl;
}
if(check(n))
	cout<<"Case #"<<i+1<<":"<<" "<<count<<endl;
else
	cout<<"Case #"<<i+1<<":"<<" "<<"IMPOSSIBLE"<<endl;

}
cin>>x;
	
}
//myfile.close();
	//return 0;
}
