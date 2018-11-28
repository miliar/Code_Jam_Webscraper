# include <bits/stdc++.h>
using namespace std;

void eval()
{
	string str;
	int k,i,j;
	cin>>str>>k;
	int len = str.length();
	int no_of_flips = 0;
	for(i=0 ; i<(len-k+1) ; i++)
	{
		if(str[i] == '-')
		{
			no_of_flips++;
			for(j=i ; j<(i+k) ; j++)
			{
				if(str[j] == '-')
					str[j] = '+';
				else
					str[j] = '-';
			}
		}
	}
	int flag = 0;
	for(i=0 ; i<len ; i++)
	{
		if(str[i] == '-')
		{
			flag = 1;
			break;
		}
	}
	if(flag)
	{
		cout<<"IMPOSSIBLE"<<endl;
	}
	else
	{
		cout<<no_of_flips<<endl;
	}
}

int main()
{
    #ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int t;
	cin >> t;
	for(int tt=1;tt<=t;tt++)
	{
		cout << "Case #" << tt << ": ";
		eval();
	}
    return 0;
}
