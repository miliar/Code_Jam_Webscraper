#include<bits/stdc++.h>
using namespace std;

bitset<1010> p, mask;
int main(){
   int T; scanf("%d",&T);
   for(int cs=0; cs<T; cs++){
	   string s; cin >> s;
	   int n; scanf("%d",&n);
	   mask.reset();
	   p.reset();
	   for(int i = 0; i < n; i++) mask[s.size()-i-1] = 1;
	   for(int i = 0; i < s.size(); i++){
		   if (s[i] == '-') p[i] = 1;
		   else p[i] = 0;
	   }
	   
	   int ctr = 0;
	   for(int i = (int)s.size()-1; i >= n-1; i--){
		   // for(int j = 0; j < s.size(); j++) cout<<mask[j];
		   // cout<<endl;
		   if (p[i]){
			   ctr++;
			   p ^= mask;
		   }
		   mask >>= 1;
	   }
	   printf("Case #%d: ", cs + 1);
	   if (p.count() > 0) puts("IMPOSSIBLE");
	   else printf("%d\n", ctr);
   }
}