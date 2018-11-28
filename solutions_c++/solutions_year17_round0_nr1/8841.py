#include <cstdio>
#include <cstdlib>
#include <queue>

using namespace std;

int main(){
	int t;
	scanf("%d\n", &t);

	for(int n = 1; n <= t; n++){
		char in[1005];
		int k;
		scanf("%s %d", in, &k);

		bool flipping = false;
		queue<int> q;
		
		int out = 0;

		for(int i = 0; in[i]; i++){
			if(flipping == (in[i] == '+')){
				flipping = !flipping;
				q.push(i + k);
				out++;
			}
			
			if(!q.empty() && q.front() == i + 1){
				q.pop();
				flipping = !flipping;
			}
		}

		printf("Case #%d: ", n);

		if(!q.empty()){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n", out);
		}
	}
}
