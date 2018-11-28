
#include <bits/stdc++.h>

using namespace std;
int R,C; 
char kk[256]={0};
void check(int a, int b, int x, int y, vector<string> &v)
{
	int cnt = 0;
	char c;
	for(int i = a; i <= x; i++ )
		for(int j = b; j <= y; j++)
			if (v[i][j] != '?'){
				cnt ++;
				c = v[i][j];
			}
			
				

	if (cnt  == 1 && kk[c] == 0){
		kk[c] = 1;
		for(int i = a; i <= x; i++ )
			for(int j = b; j <= y; j++)
				v[i][j] = c;
		}

}

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cout <<"Case #"<<t <<": \n";
	
		cin >> R>> C;
		vector<string> table;
		table.clear();
		memset(kk, 0, sizeof(kk));
		for(int i = 0; i < R; i++)
		{
			string temp; cin >> temp;
			table.push_back(temp);
		}
		
		for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++){
				
				if (kk[table[i][j]]) continue;
				for(int p = R-1; p >= i; p--)
					for(int q = C-1; q >= j; q--)
						 check(i, j, p, q, table);
		}	
		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
				cout << table[i][j];
			cout << endl;
		}
		
	}
	return 0;
}