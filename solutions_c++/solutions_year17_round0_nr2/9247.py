#include<bits/stdc++.h>
using namespace std;

int tidynum(int tmp[],int ct);

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	int cs  = 1;
	long long int n;
	int tmp[100] = {0};
	cin >> t;
	while(t--)
	{
		int ct = -1;
		cin >> n;
		while(n!=0)
		{
			int r = n%10;
			ct++;
			tmp[ct] = r;
			n = n/10;
		}
		int status = tidynum(tmp,ct);
		if(status == 0)
			ct--;
		for(int i = ct;;)
		{
			if(tmp[ct] == 0)
			ct--;
			else
			break;
		}
		cout<<"Case #"<<cs<<": ";
		cs++;
		for(int i = ct;i > -1;i--)
		{
			cout<<tmp[i];
        }
		cout<<"\n";
	}
}

int tidynum(int tmp[],int ct)
{
	int flag = 0;
	int pos = -1;
	for(int i = ct;i >= 0;i--)
	{
		if(flag == 0 && i!=0)
		{
			if(tmp[i] == tmp[i-1])
			{
				pos = i;
			}
			if(tmp[i]>tmp[i-1])
			{
				if(tmp[i] == 1)
				{
					i = ct;
					flag = 2;
					continue;
				}
				if(pos == -1)
					tmp[i] -= 1;
				else
				{
					tmp[pos] -= 1;
					i = pos;
				}
				flag =1;
			}
		}
		else if(flag==1 || flag == 2)
		{
			tmp[i] = 9;
		}
	}
	if(flag == 2)
	{
		return 0;
	}
	return 1;
}

