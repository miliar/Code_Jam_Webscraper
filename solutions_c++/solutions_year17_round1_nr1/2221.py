#if 0==0

#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<iostream>

using std::vector;
using std::string;
using std::cin;
using std::cout;

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int n;

	cin>>n;
	for (int i_case = 1 ; i_case <= n ; i_case++)
	{
		printf("Case #%d:\n", i_case);
		char cake[100][100];
		int visited[100][100];
		string s;
		int r, c;
		cin>>r>>c;
		//cout<<r<<" "<<c<<"\n";

		for (int i = 0 ; i < r ; i++) {
			//scanf("%s", str);
			//cake.push_back(str);
			cin>>s;
			if (s.size() < c) cout<<"NOooooo!\n";
			for (int j = 0 ; j < c ; j++) {
				visited[i][j] = 0;
				cake[i][j] = s[j];
			}
			//printf("s = %s\n", s.c_str());
		}

		for (int j = 0 ; j < c ; j++) {
			for (int i = 0 ; i < r ; i++) {
				//cout<<"i="<<i<<"j="<<j<<"\n";
				if (visited[i][j]) continue;

				if (cake[i][j] == '?') {

				} else {
					visited[i][j] = 1;
					char ch = cake[i][j];
					//cout<<"ch="<<ch<<"\n";
					int top = i - 1;
					while (top >= 0) {
						if (cake[top][j] == '?') top--; else break;
					}
					//cout<<"top="<<top<<"\n";
					int bottom = i + 1;
					while (bottom < r) {
						if (cake[bottom][j] == '?') bottom++; else break;
					}
					//cout<<"bottom="<<bottom<<"\n";
					int left = j - 1;
					while (left >= 0) {
						if (cake[i][left] == '?') {
							//cout<<"l="<<left<<"\n";
							left--;
						} else break;
					}
					//cout<<"left="<<left<<"\n";
					int right = j + 1;
					bool ok = true;
					while (right < c) {
						for (int k = top + 1 ; k < bottom ; k++)
							if (cake[k][right] != '?') {
								ok = false;
								break;
							}
						if (!ok) break; else right++;
					}
					//cout<<"right="<<right<<"\n";

					for (int ii = top + 1 ; ii < bottom ; ii++) {
						for (int jj = left + 1 ; jj < right ; jj++) {
							cake[ii][jj] = ch;
							visited[ii][jj] = 1;
						}
					}


				}
			}
		}

		for (int i = 0 ; i < r ; i++) {
			for (int j = 0 ; j < c ; j++) {
				cout<<cake[i][j];
			}
			cout<<"\n";
		}
	}

	return 0;
}

#endif
