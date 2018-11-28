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
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
		
	int t;si(t);fl(_, 1, t + 1){
			
		string s;cin >> s;
		int k; cin >> k;
		int n = s.size();
		
		int ans = 0;
		bool tr = true;
		fl(i, 0, n){
			if(s[i] == '-'){
				if(i + k - 1 > n - 1){
					tr = false;
					break;
				}
				fl(j, i, i + k){
					s[j] = (s[j] == '+')?'-':'+';
				}
				ans++;
			}
		}
		
		if(tr){
			cout << "Case #" << _ << ": " << ans << "\n";
			continue;
		}
		
		ans = 0;
		tr = true;
		for(int i = n - 1;i >= 0;i--){
			if(s[i] == '-'){
				if(i - k + 1 < 0){
					tr = false;
					break;
				}
				for(int j = i;j > i - k;j--){
					s[j] = (s[j] == '+')?'-':'+';
				}
				ans++;
			}
		}
		if(tr){
			cout << "Case #" << _ << ": " << ans << "\n";
			continue;
		}
		else{
			cout << "Case #" << _ << ": " << "IMPOSSIBLE" << "\n";
		}		
		
	}
	 
	return 0;
}
