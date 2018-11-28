#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	ios::sync_with_stdio(false);cin.tie(NULL);
	cout << fixed << showpoint;
	cout << setprecision(3);
	int T;
	cin  >> T;
	for(int t = 1; t <= T; t++){
		string str;
		cin >> str;
		int n = str.size();
		for(int i = n - 1; i > 0; i--){
			if(str[i - 1] > str[i]){
				for(int j = i; j < n; j++){
					str[j] = '9';
				}
				str[i - 1]--;
			}
		}
		int k = 0;
		while(str[k] == '0'){
			k++;
		}
		cout << "Case #" << t << ": ";		
		for(int i = k; i < str.size(); i++){
			cout << str[i];
		}cout <<'\n';
		
	}
	
	return 0;
}
