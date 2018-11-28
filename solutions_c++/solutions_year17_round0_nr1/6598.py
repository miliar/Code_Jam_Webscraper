#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;
int t,k;
string str;
int tab[100010];
int main()
{
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>str>>k;

		int atas=str.length();
		for (int j=0;j<atas;j++)
		{
			if (str[j]=='-') tab[j]=0; else tab[j]=1;
		}

		int cou=0;
		for (int j=0;j+k<=atas;j++)
		{
			if (tab[j]==0)
			{
				for(int l=j;l<j+k;l++)
				{
					tab[l]=tab[l]^1;
				}
				cou++;
			}
		}

		bool cek=1;
		for (int j=0;j<atas;j++) if (tab[j]==0) {cek=0; break;}

		cout<<"Case #"<<i<<": ";
		if (cek) cout<<cou; else cout<<"IMPOSSIBLE";
		cout<<"\n";
	}

	return 0;
}