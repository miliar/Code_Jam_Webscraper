
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl

#define ones(x) __builtin_popcount(x)

using namespace std;


int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
		
	while(tc--){
		
		int N, R, O, Y, G, B, V;
		scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
		
		vector<pair<int, char> >v;
		v.pb(make_pair(R, 'R'));
		v.pb(make_pair(Y, 'Y'));
		v.pb(make_pair(B, 'B'));

		sort(all(v));
		reverse(all(v));
		
		vector<char>ans, aux;
		if(v[0].first > v[1].first + v[2].first)printf("Case #%d: IMPOSSIBLE\n", caso++);
		else{
			
			for(int i = 0; i < v[0].first; i++){
				
				ans.pb(v[0].second);	
				if(v[1].first > 0)ans.pb(v[1].second), v[1].first--;
				else if(v[2].first > 0)ans.pb(v[2].second), v[2].first--;
			}
			
			for(int i = 0; i < ans.size(); i++){
				
				aux.pb(ans[i]);
				if(v[2].first > 0)aux.pb(v[2].second), v[2].first--;
			}
			
			ans = aux;
			int len = ans.size();
			bool ok = true;
			
			for(int i = 0; i <= len; i++){
			
				if(ans[i%len] == ans[(i + 1)%len])ok = false;	
			}
			
			if(!ok)printf("Case #%d: IMPOSSIBLE\n", caso++);
			else{
				
				printf("Case #%d: ", caso++);
				for(int i = 0; i < len; i++)putchar(ans[i]);
				puts("");
			}
		}
		
	}


}

