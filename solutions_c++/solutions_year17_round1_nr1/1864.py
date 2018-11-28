#include <bits/stdc++.h>
#define N 30
using namespace std;

int n, m, dx[8] = {1, -1, 0, 0, 1, 1, -1, -1}, dy[8] = {0, 0, 1, -1, -1, 1, -1, 1}, linha[N], coluna[N];

char mat[N][N];

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	int T;

	cin>>T;

	for(int t = 1; t <= T; t++) {

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
                        {
                            mat[i][z] = mat[i][j];
                        }
   
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
                    for(int z = 0; z < n && (mat[z][j] == '?' || mat[z][j] == mat[i][j] || z < i); z++){

                        if(z != i && mat[z][j] == '?')
                        {
                            mat[z][j] = mat[i][j];
                        }
                    }
                }
            }
        }

	cout<<"Case #"<<t<<":\n";

	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < m; j++)
		{
			cout<<mat[i][j];
		}
		cout<<"\n";
	}

}
}