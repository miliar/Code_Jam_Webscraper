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

	int T, ans;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		int r,c;
		cin >> r >> c;
		char str[30][30];
		for(int i=0; i<r; i++)
			cin >> str[i];
		
		//if(t == 56)
		//	for(int i=0; i<r; i++)
		//		cout << str[i] << endl;
			

		char s;
		for(int i=0; i<r; i++)
		{
			int prev = -1;
			for(int j=0; j<c-1; j++)
			{
				if(str[i][j+1] == '?')
					str[i][j+1] = str[i][j];
			}
			for(int j=c-1; j>0; j--)
			{
				if(str[i][j-1] == '?')
					str[i][j-1] = str[i][j];
			}
			for(int j=0; j<c; j++)
			{
				if(str[i][j] == '?' && i > 0)
					str[i][j] = str[i-1][j];
			}
			/*for(int j=0; j<c; j++)
			{
				if(str[i][j] == '?' && i < r-1)
					str[i][j] = str[i+1][j];
			}*/

		}

		
		for(int i=r-2; i>=0; i--)
		{
			for(int j=0; j<c; j++)
				if(str[i][j] == '?' && i < r-1)
					str[i][j] = str[i+1][j];
		}
		//if(t == 56) {
		cout<<"Case #"<<t<<": "<< endl;
		for(int i=0; i<r; i++)
			cout << str[i] << endl;
		//}
	}
	return 0;
}