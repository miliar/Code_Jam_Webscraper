#include <iostream>
#include <map>
using namespace std;

void printStalls(map<int, int> stalls, int n){
	int j = 0;
	while(j <= n+1) {
		try {
			stalls.at(j);
			printf("o");
		} catch (const exception e) {
			printf("_");
		}
		j++;
	}
	printf("\n");
}


int main(){
	int t;
	scanf("%d", &t);
	int i = 0;
	while(i < t){
		long long n, k;
		scanf(" %lld %lld", &n, &k);
		//key thing to notice here is that the vast majority of the given information is actually irrelevant
		//Really, all that happens is that each person goes into the middle of the largest consecutive row of unoccupied stalls
		//we don't even need to know which stall they go into, so all we really need to know is how big the gap they go into is
		//so we keep track of the number of gaps of each size, and then when someone goes into each of those the number of gaps of smaller sizes increase
		
		//so we have a map where stalls[s] is the number of rows of size s
		//and we can take large chunks off k at a time since we don't care about which specific stall they go into
		
		map<long long, long long> stalls;
		stalls[n] = 1;
		while (k > 0){
			map<long long, long long>::iterator it = stalls.end();
			it--;
			long long s = it->first;
			long long j = it->second;
			long long l = (s-1)/2;
			long long r = s - l - 1;
			if(j >= k){
				//r is always >= l
				printf("Case #%d: %lld %lld\n", i+1, r, l);
				break;
			}	else {
				k = k - j;
				stalls[l] = stalls[l] + j;
				stalls[r] = stalls[r] + j;
				stalls.erase(s);
			}	
		}
		i++;
	}
}