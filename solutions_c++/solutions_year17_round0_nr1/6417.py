#include <iostream>
#include <cstring>
using namespace std;
int set(char *ch)
{
	int flag = 1;
	int i;
	for(i = 0; ch[i]; i++)
	{
		if(ch[i] == '-')
		{
			flag = 0;
			break;
		}
	}
	return flag;
}
void flip(char *ch, int k, int p)
{
	int i, j = k;
	//cout<<p<<" times from "<<k<<endl;
	for(i = 0; i < p; i++)
	{
	    //cout<<"Toggling "<<ch[j]<<endl;
		if(ch[j] == '-')
			ch[j++] = '+';
		else if(ch[j] == '+')
			ch[j++] = '-';
	}
}
int main()
{
	int t, i, k;
	char str[1000];
	cin>>t;
	//cout<<t<<endl;
	for(i = 1; i <=t; i++)
	{
	    int p, j;
		cin>>str;
		//cout<<str<<endl;
		cin>>p;
		//cout<<"Length "<<p<<endl;
		int n = strlen(str);
		int ans = 0;
		for(k = 0; k < n - p + 1; k++)
		{
			if(set(str))
				break;
			else if(str[k] != '+')
			{
				flip(str, k, p);
				//cout<<str<<endl;
                ans++;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(set(str))
            cout<<ans<<endl;
		else
            cout<<"IMPOSSIBLE\n";
	}
	return 0;
}