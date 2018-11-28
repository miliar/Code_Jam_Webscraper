/*
#include <bits/stdc++.h>

using namespace std;
#define F first
#define S second
int arr[] = {5,10,20,50,100,200,500,1000,2000,5000,10000};
//{10000,5000,2000,1000,500,200,100,50,20,10,5};
long long memo[12][30001];
long long dp(int i , int x , int cur){
	if (cur == x)
		return 1;
	if (cur > x || i == 11)
		return 0;
	long long &ans = memo[i][cur];
	if(ans != -1)return ans;
	ans=0;
	ans += dp(i+1 , x , cur) + dp(i , x , cur + arr[i]);
	return ans;
}

int main() {
	while(true){
		memset(memo,-1,sizeof memo);
		double x;
		cin >> x;
		if( (int)(x*100.0) == 0)return 0;
		printf("%6.2f%17lld\n", x, dp (0,round(x*100.0),0));
	}
	return 0;
}
*/
#include <bits/stdc++.h>

using namespace std;
#define F first
#define S second

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int j = 1 ; j <= t ; ++j){
		string s;
		cin >> s;
		int x = 20;
		int first = 0 , nothing=s.size();
		while(x--){
			for(int i = s.size()-1 ; i > 0 ; --i){
				if(s[i] < s[i-1] && s[i-1]!='0'){
					s[i]='9';
					if(first <= nothing-i){
						s[i-1]--;
						first=nothing-i;
					}

				}
			}
		}
		int b=0;
		cout << "Case #"<<j<<": ";
		for(int i = 0 ; i < s.size() ; ++i){
			if(s[i] != '0')b=1;
			if(b)cout << s[i];
		}
		cout << endl;
	}
	return 0;
}
