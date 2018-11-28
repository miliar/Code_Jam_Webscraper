#include <bits/stdc++.h>
#include <math.h>
using namespace std;

int main(){
	int T, n, k, C=0, mini, maxi, front, half;
	scanf("%d", &T);
	while(C++ < T){
		scanf("%d %d", &n, &k);
		vector<int> v;
		v.push_back(n);
		make_heap(v.begin(), v.end());
		int left, right;
		for(int i=0; i<k; i++){
			front = v.front();

			pop_heap(v.begin(),v.end()); 
			v.pop_back();
			
			half = front/2;
			if(front%2 == 1) half++;
			left = half - 1;
			right = front - half;
			
			v.push_back(left); v.push_back(right); 
			push_heap (v.begin(),v.end());
		}



		// int divs = floor(log2(k)) + 1;

		// while(divs--) n/=2;
		// if(n%2 == 0 && n != 0){
		// 	mini = n - 1;
		// 	maxi = n;
		// }else if(n == 0){
		// 	mini = 0;
		// 	maxi = 0;
		// }else{
		// 	mini = n;
		// 	maxi = n;
		// }
		maxi = right;
		mini = left;
		printf("Case #%d: %d %d\n", C, maxi, mini);
	}
	return 0;
}