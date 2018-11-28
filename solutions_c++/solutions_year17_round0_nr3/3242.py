#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>



using namespace std;

struct triple {
	long long int L;
	long long int R;
	long long int order;
};

vector <triple> bath;


bool comp (triple i, triple j){
	if ( (i.R - i.L) <= (j.R - j.L) ) return true;
	return false;
	
}









void funcaaaao ( long long int problem_count, long long int k) {
	long long int interval, ans_min, ans_max;
	
	
	while (k > 0ll) {
			
			if (bath[bath.size() - 1].R - bath[bath.size() - 1].L == bath[bath.size() - 2].R - bath[bath.size() - 2].L) {
				bath[bath.size() - 2].order += bath[bath.size() - 1].order;
				bath.pop_back();
			} else {
				
					
//printf("\nentrei!\n");
					interval = bath[bath.size() - 1].R - bath[bath.size() - 1].L;
		//printf("interval: %d\n", interval);
					if (interval == 0) {
						bath.pop_back();
						
						ans_max = 0;
						
						ans_min = 0;
					}
					else if (interval % 2 == 0 ) {
						k -= bath[ bath.size() - 1 ].order;
		//printf("k = %d\n", k);				
						ans_max = interval/2;
						ans_min = interval/2;
						
						bath[ bath.size() - 1 ].R = bath[bath.size() - 1].L + interval/2;
						bath[ bath.size() - 1 ].order *= 2;
					} else {
						k -= bath[ bath.size() - 1 ].order;
		//printf("k = %d\n", k);
						ans_min = interval/2;
						ans_max = ans_min + 1;
						
						bath.push_back(triple());
						
						bath[ bath.size() - 1].R = bath[ bath.size() - 2].R;
						bath[ bath.size() - 2].R = (bath[bath.size() - 2].R + bath[bath.size() - 2].L)/2;
						bath[ bath.size() - 1].L = bath[ bath.size() - 2].R;
						bath[ bath.size() - 1].order = bath[ bath.size() - 2].order;
					}
			}
			sort (&bath[0], &bath[ bath.size() ], comp);
			
		}	
		

		
		printf("Case #%lld: %lld %lld\n", problem_count, ans_max-1, ans_min-1);
}

























main () {
	
	long long int t, problem_count, n;
	long long int k;

	scanf("%lld", &t);
//printf("testes: %d\n\n", t);	
	problem_count = 0;
	
	while (t--) {
		problem_count ++;
		bath.clear();
	
		scanf("%lld %lld", &n, &k);
//printf("%d %d", n, k);		
		bath.push_back(triple());
		
		bath[0].L = 0;
		bath[0].R = n+1;
		bath[0].order = 1;
		
		funcaaaao (problem_count, k);
		
	}
	
	return 0;
}
