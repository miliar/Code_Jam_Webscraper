#include<iostream>
#include<string>
#include<climits>
using namespace std;
void solve()
{
	int num;
	cin>>num;
	int flag = 0;
	while(num>0 && flag == 0)
	{
		int temp = num;
		int prev = INT_MAX;
		int fflag = 0;
		while(temp>0)
		{
			int dig = temp%10;
			temp = temp/10;
			if(dig <= prev)
			{
				prev = dig;
			}
			else
			{
				fflag++;
				break;
			}
		}
		if(fflag == 0)
		{
			flag = 1;
			cout<<num;
		}
		num--;
	}
}

int main()
{
	int tc;
	cin>>tc;
	for(int i = 0; i<tc; i++)
	{
		cout<< "Case #"<<(i+1)<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}