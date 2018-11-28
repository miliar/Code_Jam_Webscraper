#include <iostream>
using namespace std;
typedef unsigned int ui;
inline bool check(ui in)
{
	if(in%10==0)
		return false;
	ui end=in%10;
	in/=10;
	while(in>0)
	{
		ui new_end=in%10;
		if(!(new_end<=end))
			return false;
		end=new_end;
		in/=10;
	}
	return true;
}
int main()
{
	int ti;
	cin>>ti;
	for(int t=0;t!=ti;t++)
	{
		int num;
		cin>>num;
		cout<<"Case #"<<t+1<<": ";
		for(int k=num;k>0;k--)
			if(check(k))
			{
				cout<<k;
				break;
			}
		cout<<'\n';
	}
}
