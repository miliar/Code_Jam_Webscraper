#include <bits/stdc++.h>
#define ll long long 
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define mod 1000000007
using namespace std;

int main()
{   
	freopen("Al.in","r",stdin);
	freopen("A.out","w",stdout);

	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		string str;
		cin >> str;
		int ar[20];
		for(int i=0; i< str.size(); i++)
			ar[i] = str[i]-'0';
		for(int i = str.size()-1; i > 0; i--)
		{
			if(ar[i] < ar[i-1])
			{
				ar[i-1]--;
				for(int j=i; j < str.size(); j++)
					ar[j]=9;
			}
		}			

		cout<<"Case #"<<t<<": ";//<<answer<<endl;
		int f=0;
		for(int i=0; i<str.size(); i++)
		{
			if(ar[i] == 0 && !f)
				continue;
			cout<<ar[i];
			f=1;
		}	
		cout<<endl;
	}
	return 0;
}