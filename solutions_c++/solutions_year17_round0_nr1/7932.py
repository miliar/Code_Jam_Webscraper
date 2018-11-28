#include <iostream>
#include <vector>

using namespace std;

void flip(string &s, int i, int k);

void flip(string &s, int i, int k)
{
	while(k>0){
		s[i] = (s[i] == '+') ? '-' : '+';
		--k;
		++i;
	}
}

int main()
{
	int n, k;
	string s;
	cin >> n;
	for (int i = 0; i < n; ++i){
		cin >> s >> k;
		int l = (int)s.size(), j, ans = 0;
		for (j = 0; j <= l-k; j++){
			if (s[j] == '-'){
				flip(s, j, k);
				ans++;
			}
		}
		while (j < l){
			if (s[j] == '-')
				ans = -1;
			j++;
		}
		if (ans == -1)
			cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}
