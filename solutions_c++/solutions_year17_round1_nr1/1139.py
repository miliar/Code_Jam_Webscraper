#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define sz size()
#define pii pair<int,int>
#define mp make_pair
#define ff first
#define ss second
#define all(v) (v).begin(),(v).end()

string s[30];

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	//std::ios_base::sync_with_stdio(false);
	
	int t,r,c;

	cin >> t;

	for(int cases = 1;cases <= t;cases++){

		cin >> r >> c;

		cin.ignore();

		for(int i = 0;i < r;i++){

			cin >> s[i];
		}

		int op = 0;

		std::vector<char> v;

		for(int i = 0;i < r;i++){

			bool flag=1;

			for(int j = 0;j < c;j++){

				if(s[i][j] != '?'){
					flag=0;
					v.pb(s[i][j]);
					continue;
				}
			}
			if(flag)op++;
			else {

				int k = 0;
				int j = 0;
				while(k < c){

					while(s[i][j] == '?' || s[i][j] == v[k]){
						s[i][j] = v[k];
						j++;
					}
					k++;
				}
				v.clear();

				for(int j = 1;j <= op;j++){

					for(int k = 0;k < c;k++){

						s[i-j][k] = s[i][k];
					}
				}
				op = 0;
			}
		}
		if(op){

			for(int i = r-op;i < r;i++){

				for(int j = 0;j < c;j++){

					s[i][j] = s[r-op-1][j];
				}
			}			
		}
		cout << "Case #"<< cases <<":" << endl;
		for(int i = 0;i < r;i++){

			cout << s[i] << endl;
		}
	}
	return 0;
}