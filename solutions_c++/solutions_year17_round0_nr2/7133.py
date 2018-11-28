#include <bits/stdc++.h>
using namespace std;
 
#define fl(i,a,n) 	for(int i=a;i<n;i++)
#define pi(a)		printf("%d\n",a)
#define plli(a) 	printf("%lld\n",a)
#define si(a) 		scanf("%d",&a)
#define sii(a,b) 	scanf("%d%d",&a,&b)
#define siii(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define slli(a) 	scanf("%lld",&a)
#define pb 			push_back
#define fi 			first
#define se 			second
#define mp 			make_pair
#define pii 		pair<int,int>
#define vi			vector<int>
#define vvi			vector< vector<int> >
#define vpii		vector< pair<int,int> >
#define ll 			long long
#define mod			1000000007
 
 
 
 int main() {
	#ifndef ONLINE_JUDGE 
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
		
	int t;si(t);fl(_, 1, t + 1){
			
		string s;cin >> s;
		int cnt = 0;
		int n = s.size(), i = 0;
		
		while(i < n - 1 && s[i] <= s[i + 1]){
			i++;
		}
		if(i == n - 1){
			cout << "Case #" << _ << ": " << s << "\n";
			continue;
		}
		
		while(i >= 1 && s[i - 1] == s[i]){
			i--;
		}
		
		s[i] = (char)(s[i] - 1);
		i++;
		while(i < n){
			s[i] = '9';
			i++;
		}
		if(s[0] == '0')
			s = s.substr(1);
		
		cout << "Case #" << _ << ": " << s << "\n";
		
	}
	 
	return 0;
}
