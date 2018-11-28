#include <cstdio>
#include <algorithm>
using namespace std;
#define ll long long
#define t_max 100
#define n_max 1000000000

ll tree[n_max/2];
int t;

void p(int line){printf("line: %d\n", line);}

bool cmp(int a, int b){return a > b;}

int main(){
	scanf("%d", &t);

	for(int i = 0; i < t ; i ++){
		ll n,k;
		scanf("%lld %lld", &n, &k);
		printf("Case #%d: ", i + 1);
		
		tree[1] = n;
		ll begin = 1;

		for(ll j = 2; j <= k; j *= 2){
			for(ll s = j; s < j * 2; s+=2){
				if(tree[s/2] % 2){
					tree[s] = tree[s+1] = tree[s/2] / 2;
				}
				else{
					tree[s] = tree[s/2] / 2;
					tree[s+1] = tree[s/2] / 2 - 1;
				}
			}
			begin = j;
		}
		
		sort(tree + begin, tree + begin*2, cmp);

		ll choose = tree[k];

		if(choose % 2){
			printf("%lld %lld", choose/2, choose/2);
		}
		else{
			printf("%lld %lld", choose/2, choose/2 -1);
		}
		printf("\n");
	}
}


