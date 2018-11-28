#include <iostream>
#include <math.h>
using namespace std;
typedef pair<int,int> ii;

ii process(int num){
	num--;
	int s = num/2;
	int l = num-s;
	return make_pair(s,l);
}

ii count(int num, int ppl){
	//printf("%d %d\n", num,ppl);
	ii ans = process(num);
	if (ppl==0) return ans;
	ppl--;
	
		ii smaller = count(ans.first, ppl/2);
		ii larger = count(ans.second, ppl-ppl/2);
		if (smaller.first>larger.first ) return smaller;
		else if (smaller.first==larger.first && smaller.second>larger.second) return smaller;
		else return larger;
	
}
int main(){
	int t;
	int k,n,s,l;
	scanf("%d\n", &t);
	for (int _=1; _<=t; _++){
		scanf("%d %d\n", &n, &k);

		// ans = n/k;
		// ans--;
		// s = ans/2;
		// l = ans-s;
		ii ans = count(n,k-1);
		printf("Case #%d: %d %d\n", _, ans.second,ans.first); 
	}
}