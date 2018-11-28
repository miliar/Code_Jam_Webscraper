#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int T, N, M, K, D, S;
struct Node{
	char t;
	int n;
	int first;

	int n2;
	char t2;
} arr[3];


int cmp(const Node& lhs, const Node& rhs){
	return lhs.n < rhs.n;
}
enum{ R, O, Y, G, B, V};
int E[] = {2, 0, 1};
char sss[] = "ROYGBV";

void myput(int n){
	// printf("%d",n);
	if(arr[n].first){
		arr[n].first = 0;
		putchar(arr[n].t);
		for(int i=0; i < arr[n].n2; ++i){
			putchar(arr[n].t2);
			putchar(arr[n].t);
		}
	}else{
		putchar(arr[n].t);
	}
	// putchar(' ');
}

int zeroI(int a){
	return arr[a].n == 0 && arr[a].n2 == 0;
}

int zero(int a, int b){
	return zeroI(a) && zeroI(b);
}

void spe(int a, int cs){
	if(arr[a].n == arr[a].n2){
		printf("Case #%d: ", cs);
		for(int i =0; i< arr[a].n; ++i){
			putchar(arr[a].t);
			putchar(arr[a].t2);
		}
		putchar('\n');
	}else{
		printf("Case #%d: IMPOSSIBLE\n", cs);
	}
}

int main(){
	cin>>T;
	for(int cs=1; cs<=T; ++cs){
		cin>>N;
		for (int i = 0; i< 3; ++i){
			arr[i].t = sss[2*i];
			arr[i].first = 1;
			cin>>arr[i].n;

			arr[E[i]].t2 = sss[2*i|1];
			cin>>arr[E[i]].n2;
		}
		// for(int i =0; i< 3; ++i){
			// printf("%c %c\n", arr[i].t, arr[i].t2);
			// printf("%d %d\n", arr[i].n, arr[i].n2);
		// }
		if (zero(0, 1)){
			spe(2, cs);
			continue;
		}
		if (zero(1, 2)){
			spe(0, cs);
			continue;
		}
		if (zero(0, 2)){
			spe(1, cs);
			continue;
		}
		int kk = zeroI(0)+zeroI(1) + zeroI(2);
		// cout<<kk<<endl;
		arr[0].n -= arr[0].n2;
		arr[1].n -= arr[1].n2;
		arr[2].n -= arr[2].n2;
		std::sort(arr, arr+3, cmp);
		// cout<<arr[kk].n<<endl;
		if (arr[kk].n < 1){
			printf("Case #%d: IMPOSSIBLE\n", cs);
			continue;
		}
		if (arr[1].n + arr[0].n < arr[2].n)
			printf("Case #%d: IMPOSSIBLE\n", cs);
		else{
			printf("Case #%d: ", cs);
			int i;
			for(i = 0; i< (arr[1].n - arr[0].n); ++i){
				myput(2);
				myput(1);
			}
			arr[1].n -= i;
			while(i<arr[2].n){
				myput(2);
				++i;
				if(i & 1){
					myput(1);
					--arr[1].n;
				}else{
					myput(0);
					--arr[0].n;
				}
			}
			while(arr[0].n || arr[1].n){
				if(i&1){
					--arr[0].n;
					myput(0);
					++i;
				}else{
					--arr[1].n;
					myput(1);
					++i;
				}
			}
			putchar('\n');
		}
	}
	return 0;
}
