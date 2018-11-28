#include<iostream>
#include<string>
#include<vector>
using namespace std;
void tidy(vector<int > &ar)
{
	int i=0;
		while(i<ar.size()-1)
		{
			if(ar[i]>ar[i+1])
			{
				ar[i]=ar[i]-1;
				break;
			}
			i++;
		}
		if(i!=0&&ar[i]<ar[i-1])
		{
			
			tidy(ar);
		}
			i++;
			while(i<ar.size())
			{	
			ar[i]=9;
			i++;
			}
	
}
int main()
{
	int tc,j;
	string str;
	cin>>tc;
	for(int i=0;i<tc;i++)
	{
			cin>>str;
			if(str.size()==1)
			{
				cout<<"Case #"<<i+1<<": "<<str[0]<<endl;
			}
			else			
			{
			vector <int > ar;
			j=0;
			while(j<str.size())
			{
		
				ar.push_back((str[j]-'0'));
				j++;
			}
			tidy(ar);
			cout<<"Case #"<<i+1<<": ";
			for(j=0;j<ar.size();j++)
			{
				if(ar[j]!=0)
					cout<<ar[j];
			}
			cout<<endl;
			}
	}
	return 0;
}