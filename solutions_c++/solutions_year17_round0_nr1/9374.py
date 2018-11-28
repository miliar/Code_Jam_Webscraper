#include <iostream>
#include <string>
using namespace std;

bool only_one(string str)
{
	for(int i=0;i<=str.size();i++) if (str[i]=='-') return 0;
	return 1;
}

int search(string str)
{
	for(int i=0;i<=str.size();i++) if (str[i]=='-') return i+1;
	return 0;
}

int answer(string str,int size)
{
	int steps=0,index=0;
	for(;;)
	{
		if (search(str)) index=search(str)-1;
		else return steps;
		if (index+size<=str.size())
		{
			for(int i=index;i<index+size;i++)
			{
				if (str[i]=='+') str[i]='-';
				else str[i]='+';
			}
			steps++;
		}
		else return 0;
	}
}
struct row
{
	string str;
	int n;		
};
int main()
{
	int n;	
	cin>>n;
	row arr[n];
	for(int i=0;i<n;i++) cin>>arr[i].str>>arr[i].n;
	for(int i=0;i<n;i++)
	{
		if (only_one(arr[i].str)) cout<<"Case #"<<i+1<<": "<<0<<endl;
		else
		{
			int result=answer(arr[i].str,arr[i].n);
			if (result==0) cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
			else cout<<"Case #"<<i+1<<": "<<result<<endl;
		}
	}
	return 0;
}