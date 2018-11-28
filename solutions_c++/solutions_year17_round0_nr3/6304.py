#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <math.h>
#include <cmath>
using namespace std;
//bool is_integer(float k)
//{
//  return std::floor(k) == k;
//}
void solve(int test) {
	int n,k,max,min,val,maxval,point,num,maxpt,testval;	
	cin >> n;
	cin >> k;
	if(n==k){
		printf("Case #%d: %d %d\n", test, 0, 0);
	}
	else if(k==1){
		if(n%2==0){
			printf("Case #%d: %d %d\n", test, n/2, (n/2)-1);
		}
		else{
			printf("Case #%d: %d %d\n", test, n/2, (n/2));
		}
	}
	else{
		int level = log2(k);
		point = (pow(2,level));
		maxpt = n/point;
		
		n = n-(point-1);
		int maxval = maxpt*point;
		int num = maxval-n;
		
		if((pow(2,level+1)-k)<=num){
			val = maxpt-1;
		}
		else
		{
			val = maxpt;
		}	

	
		if((val%2)!=0){
				max =val/2;
				min =val/2;
				
			}
			else
			{
				max = val/2;
				min = max-1;
			}
	
		printf("Case #%d: %d %d\n", test, max, min);	
	}
	
}
int main() {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int testNumber;
	cin >> testNumber;
	for (int test = 1; test <= testNumber; ++test) {
		solve(test);
	}
}
