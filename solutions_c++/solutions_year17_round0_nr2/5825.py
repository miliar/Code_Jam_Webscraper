#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(int argc, char const *argv[])
{
	
	
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);


	cin.sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int T;
	cin >> T;

	int test = 1;


	while(T--){

		ll n;
		cin >> n;

		string s = to_string(n);
		int len = s.size();

		if(n < 10)
			goto fin;
		
		for(int i = len - 2; i >= 0; --i){
			if(s[i] > s[i + 1]){
				--s[i];
				for(int j = i + 1; j < len; ++j)
					s[j] = '9';
			}
		}

		fin:
			cout << "Case #" << test++ << ": " << stoll(s) << endl;

	}

	return 0;
}