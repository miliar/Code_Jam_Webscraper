#include <bits/stdc++.h>
#define gc getchar_unlocked

using namespace std;

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

//use scanint(variable) for integer input instead of scanf
int main()
{
	int t;
	cin>>t;
	for (int i = 1; i <= t; ++i)
	{
		int r,c;
		cin>>r>>c;
		char mat[r][c];
		char p='?';
		for (int j = 0; j < r; ++j)
		{
			for (int k = 0; k < c; ++k)
			{
				cin>>mat[j][k];
			}
		}
		for (int j = 0; j < r; ++j)
		{
			int k = 0,qu=0,a=0;
			for (; k < c; ++k)
			{
				if (mat[j][k]!='?')
				{
					a++;
				}
				else
					qu++;
			}
			if (a&&qu)
			{
				k=0;
				for (; k < c; ++k)
				{
					if (mat[j][k]!='?')
					{
						p=mat[j][k];
						break;
					}
				}
				for (int o = 0; o < k; ++o)
				{
					mat[j][o]=p;
				}
				for (int o = k; o < c; ++o)
				{
					if (mat[j][o]=='?')
					{
						mat[j][o]=p;
					}
					else
						p=mat[j][o];
				}
			}
		}
			int k = 0,d=0;
			for (; k < r; ++k)
			{
				if (mat[k][0]!='?')
					{
						d=k;
						break;
					}
			}
			for (int o = k-1; o >=0; o--)
				{
					for (int l = 0; l < c; ++l)
					{
						mat[o][l]=mat[o+1][l];
					}
				}
				for (int o = k; o < r; ++o)
				{
					if (mat[o][0]=='?')
					{
						for (int l = 0; l < c; ++l)
						{
							mat[o][l]=mat[o-1][l];
						}
					}
				}
		cout<<"Case #"<<i<<":"<<endl;
		for (int j = 0; j < r; ++j)
		{
			for (int k = 0; k < c; ++k)
			{
				cout<<mat[j][k];
			}
			cout<<endl;
		}

	}
	return 0;
}