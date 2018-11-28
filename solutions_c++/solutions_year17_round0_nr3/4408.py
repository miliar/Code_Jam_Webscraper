#include <cstdio>
#include <queue>

using namespace std;

priority_queue<int> kolejka;

int main(){
	int t, pis, lud, p, l, r;
	
	scanf("%d", &t);
	for(int i=0; i<t; i++){
		while(!kolejka.empty())
			kolejka.pop();
		scanf("%d %d", &pis, &lud);
		kolejka.push(pis);
		for(int j=0; j<lud; j++){
			p = kolejka.top();
			kolejka.pop();
			if(p%2 == 1){
				l = p/2;
				r = l;
			}
			else {
				l = (p-1)/2;
				r = p/2;
			}
			kolejka.push(l);
			kolejka.push(r);
		}
		printf("Case #%d: %d %d\n", i+1, r, l);
	}
	return 0;
}
