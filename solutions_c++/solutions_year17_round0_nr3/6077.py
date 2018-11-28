#include <stdio.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

void printMaxMinDP(long long int num);
FILE *ipf, *opf;
priority_queue<long long int> q;
int main(){
	

	ipf = fopen("abc.in","r");
	opf = fopen("stalls2.out", "w");
	int T;

	fscanf(ipf, "%ld", &T);

	
	int origT = T;

	// int N, K;
	long long int N, K;
	N=10000;
	while(T--){	
	
		fprintf(opf, "Case #%d: ", origT-T);
		int j;
		
		q= priority_queue<long long int>();
		fscanf(ipf,  "%lld %lld", &N, &K);
		q.push(N);
		printMaxMinDP( K);
		
		
	}

	
}

void printMaxMinDP(long long int num){
	long long int free;
	for (int i =1;i<num;i++){
		 free = q.top();
		q.pop();


		////
		if (free==2){
			q.push(1);
		}else {
			if(free>2){
				if (free%2==0){
					q.push(free/2);
					q.push((free-2)/2);

					// return;
				}else{
					q.push((free-1)/2);
					q.push((free-1)/2);
					// return;
				}
			}else{
				if(free==1){
				}
			}

		////
		}
	}
	free = q.top();
	if (free==1){
			fprintf(opf,"%d %d\n", 0,0);
	}
	else{
			if (free%2==0){
				fprintf(opf,"%lld %lld\n", free/2, (free-2)/2);
				return;
			}else{
				fprintf(opf,"%lld %lld\n", (free-1)/2, (free-1)/2);
				return;
			}
	}

}

void printMaxMin(long long int n){
	long long int free = q.top();
	// cout<<q.size()<<endl;
	// cout<<free<<endl;
	q.pop();	
	if (n==1){
		
		if (free==1){
			fprintf(opf,"%d %d\n", 0,0);
		}else{
			if (free%2==0){
				fprintf(opf,"%lld %lld\n", free/2, (free-2)/2);
				return;
			}else{
				fprintf(opf,"%lld %lld\n", (free-1)/2, (free-1)/2);
				return;
			}
		}
	}else{
		// cout<<"CALLED WITH "<<n<<endl;
		if (free==2){
			q.push(1);
			printMaxMin(n-1);
		}else {
			if(free>2){
				if (free%2==0){
					q.push(free/2);
					q.push((free-2)/2);

					printMaxMin(n-1);
					// return;
				}else{
					q.push((free-1)/2);
					q.push((free-1)/2);
					printMaxMin(n-1);
					// return;
				}
			}else{
				if(free==1){
					printMaxMin(n-1);
				}
			}
		}
	}
}