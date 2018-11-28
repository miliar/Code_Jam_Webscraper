#include <iostream>
#include <cstdio>
#include <cstring>
#define maxn 1009
using namespace std;
int n, m;
bool vis[maxn];
int l[maxn], r[maxn];
int findpos(){
	int last = 0;
	for(int i = 1; i <= n; i++){
		if(!vis[i]){
			l[i] = i - last;
		}
		else{
			last = i;
		}
	}
	last = n + 1;
	for(int i = n ;i >= 1; i--){
		if(!vis[i]){
			r[i]  = last - i;
		}
		else{
			last = i;
		}
	}
	
	
	int mi = -1, mx = -1;
	int ans = 0;
	for(int i = 1; i <= n; i++){
		if(vis[i])
			continue;
		if(min(l[i],r[i]) > mi){
			mi = min(l[i],r[i]);
			mx = max(l[i],r[i]);
			ans = i;
		}
		else if(min(l[i],r[i]) == mi && max(l[i],r[i]) > mx){
			mi = min(l[i],r[i]);
			mx = max(l[i],r[i]);	
			ans = i;		
		}
	}
	return ans;
}
int main(){
	freopen("D:\\a.in","r",stdin);
    freopen("D:\\a.out","w",stdout); 
	int tt, cot = 1;
	scanf("%d", &tt);
	while(tt--){
		memset(vis, 0, sizeof(vis));
		scanf("%d%d", &n, &m);
		vis[0] = vis[n + 1] = 1;
		int pos = 0;
		for(int i = 1; i <= m; i++){
			pos = findpos();
			vis[pos] = 1;
			//cout << pos <<endl;
		}
		printf("Case #%d: %d %d\n", cot++, max(l[pos], r[pos]) - 1, min(l[pos],r[pos]) - 1);
	}
	return 0;
}
