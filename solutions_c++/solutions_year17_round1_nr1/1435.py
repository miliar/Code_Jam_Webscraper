//In the name of Allah
#include <bits/stdc++.h>
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
const int N=3e5+1;

int main()
{
	ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	freopen ("i.in","r",stdin);
	freopen ("out.txt","w",stdout);

	int t, r, c, x=-1;
	char m[55][55];

	cin >> t;

	for(int ii=1 ; ii<=t ; ii++, x=-1)
	{
		cout << "Case #" << ii << ":\n";

		cin >> r >> c;

		for(int i=0 ; i<r ; i++)
		{
			m[i][c]='?';

			for(int j=0 ; j<c ; j++)
			{
				cin >> m[i][j];

				if(x==-1 && m[i][j]!='?')
					x = i;

				if(m[i][c]=='?' && m[i][j]!='?')
					m[i][c] = m[i][j];
			}
		}

		for(int i=x ; i<r ; i++)
		{
			if(m[i][c]=='?')
				for(int j=0 ; j<c ; j++)
					m[i][j] = m[i-1][j];

			else
				for(int j=0 ; j<c ; j++)
					if(m[i][j]=='?')
						m[i][j] = (j ? m[i][j-1] : m[i][c]);
		}

		for(int i=x-1 ; i>=0 ; i--)
		{
			if(m[i][c]=='?')
				for(int j=0 ; j<c ; j++)
					m[i][j] = m[i+1][j];

			else
				for(int j=0 ; j<c ; j++)
					if(m[i][j]=='?')
						m[i][j] = (j ? m[i][j-1] : m[i][c]);
		}

		for(int i=0 ; i<r ; i++)
		{
			for(int j=0 ; j<c ; j++)
				cout << m[i][j];

			cout << '\n';
		}
	}

	return 0;
}
