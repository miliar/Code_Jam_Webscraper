#include <bits/stdc++.h>
#define N 36
using namespace std;

char mat[N][N];
int n,m,Case;

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	cin>>Case;

	for(int tt = 1; tt <= Case; tt++)
    {

	cin>>n>>m;

	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++) cin>> mat[i][j];

	for(int i = 0; i < n; i++)
	{
        for(int j = 0; j < m; j++)
        {
            if(mat[i][j] != '?')
            {
                for(int z = 0; z < m && (mat[i][z] == '?' || mat[i][z] == mat[i][j] || z < j); z++)
                {
                    if(z != j && mat[i][z] == '?')
                        mat[i][z] = mat[i][j];

                }
            }
        }
    }

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            if(mat[i][j] != '?')
            {
                for(int z = 0; z < n && (mat[z][j] == '?' || mat[z][j] == mat[i][j] || z < i); z++)
                {
                    if(z != i && mat[z][j] == '?')
                        mat[z][j] = mat[i][j];
                }
            }
        }
    }

	cout<<"Case #"<<tt<<":\n";

	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < m; j++)
			cout<<mat[i][j];

		cout<<"\n";
	}

    }
    return 0;
}
