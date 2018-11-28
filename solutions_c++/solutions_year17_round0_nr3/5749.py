#include<stdio.h>

long long int N = 0;
int arr[1000000] = {};

int getEmpty(int index){
	int cnt = 0;
	for( int i = index; i < N; ++i ){
		if( arr[i] == 0 ){
			cnt++;
		} else {
			break;
		}
	}
	return cnt;
}

int main(){
	int T;
	long long int K;
	freopen("C_input.txt","r",stdin);
	freopen("C_output.txt","w",stdout);
	scanf("%d", &T);
    for( int i = 0; i < T; ++i ){
		scanf("%d %d",&N,&K);
		for( int j = 0; j < N; ++j ){
			arr[j] = 0;
		}
		int Ls,Rs,max,max_index,push_index;
		for( int j = 0; j < K; ++j ){
			max = 0;
			max_index = -1;
			push_index = -1;
			for( int k = 0; k < N; ++k ){
				if( arr[k] == 1 ){
					continue;
				} 
				int empty = getEmpty(k);
				if( max < empty ){
					max = empty;
					max_index = k;
				}
				k += empty;
			}
			if( max % 2 == 1 ){
				push_index = max_index + (max/2);
				Ls = push_index - max_index;
				Rs = Ls;
			} else {
				push_index = max_index + (max/2) - 1;
				Ls = push_index - max_index;
				Rs = Ls + 1;
			}
			arr[push_index] = 1;
		}
		printf("Case #%d: %d %d\n",i+1,Rs,Ls);
    }
	
    return 0;
}

