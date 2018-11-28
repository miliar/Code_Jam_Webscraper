#include <bits/stdc++.h>
#define ll long long 
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define mod 1000000007
using namespace std;

void flip(int *ar, int idx, int k)
{
	for(int i = 0; i <k; i++)
		ar[i+idx] ^= 1;
}

int check(int *ar, int n)
{
	for(int i=0; i<n; i++)
		if(ar[i] == 0)
			return 0;
	return 1;	
}

int main()
{   
	freopen("Bl.in","r",stdin);
	freopen("B.out","w",stdout);

	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		string str;
		int k, answer=0;
		cin >> str >> k;
		int ar[1009];
		for(int i=0; i<str.size(); i++)		
			ar[i] = str[i] == '+' ? 1 : 0;
		for(int i=0; i+k-1 <str.size(); i++)
		{
			if(ar[i] == 0)
			{
				flip(ar, i, k);
				answer++;
			}
		}
		if(check(ar, str.size()))
			cout<<"Case #"<<t<<": "<<answer<<endl;
		else
			cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}