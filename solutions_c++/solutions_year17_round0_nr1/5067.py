
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl
#define N 1003

using namespace std;

char s[N];
int subs[N];

int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
	
	while(tc--){
		
		int k;
		scanf("%s%d", s, &k);	
		
		int n = strlen(s);
		int cur = 0, ans = 0;
		
		memset(subs, 0, sizeof subs);
		
		for(int i = 0; i + k <= n; i++){
			
			if((s[i] == '+' && (cur&1)) || (s[i] == '-' && (cur&1) == 0)){
				
				ans++;
				cur++;
				subs[i + k - 1] = 1;
				s[i] = '+';	
			}
			cur -= subs[i];
		}
		
		bool ok = true;
		for(int i = n - k + 1; i < n; i++){
			
			if((s[i] == '+' && (cur&1)) || (s[i] == '-' && (cur&1) == 0)){
				
				ok = false;
				break;
			}
			cur -= subs[i];
		}
		
		if(ok)printf("Case #%d: %d\n", caso++, ans);
		else printf("Case #%d: IMPOSSIBLE\n", caso++);
	}


}

