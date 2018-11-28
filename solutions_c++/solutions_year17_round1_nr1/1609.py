#include<iostream>
using namespace std;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out","w", stdout);
	int TC, TT, r, c, i, j, k;
	cin >> TC;
	for(TT=1; TT <= TC; ++TT)
	{
		cin >> r >> c;
		string cake[r];
		for(i=0; i<r; ++i)
			cin >> cake[i];
		for(k=0; k<r; ++k)
		{
			for(i=0; i<c; ++i)
			{
				if(cake[k][i]!='?')
				{
					j = i-1;
					while(j>=0 && cake[k][j]=='?')
						cake[k][j--] = cake[k][i];
					j = i+1;
					while(j<c && cake[k][j]=='?')
						cake[k][j++] = cake[k][i];
				}
			}
			if(cake[k].find("?")!=string::npos)
			{
				if(k!=0)
					for(i=0; i<c; ++i)
						cake[k][i] = cake[k-1][i];
			}
		}
		for(k=r-1; k>=0; --k)
		{
			if(cake[k].find("?")!=string::npos)
				for(i=0; i<c; ++i)
					cake[k][i] = cake[k+1][i];
		}
		cout << "Case #" << TT << ":" << endl;
		for(k=0; k<r; ++k)
			cout << cake[k] << endl;
	}
	return 0;
}

