#include<stdio.h>
#define MAX_N 1000
#define MAX_T 100
using namespace std;

int K;
char C[MAX_N];
int A[MAX_N];
int length;
int cnt;

int clear(){
	length = 0;
	cnt = 0;
	for( int i = 0; i < MAX_N; ++i ){
		C[i] = 'X';
		A[i] = -1;
	}
}

int flip( int start ){
	cnt++;
	for( int i = start; i < start+K; ++i ){
		if( A[i] == 0 ){
			A[i] = 1;
		} else {
			A[i] = 0;
		}
	}
	return 0;
}

int main(){
	int T;
	freopen("A_input.txt","r",stdin);
	freopen("A_output.txt","w",stdout);
	scanf("%d", &T);
    for( int i = 0; i < T; ++i ){
		clear();
		scanf("%s %d",C,&K);
        for( int j = 0; j < MAX_N; ++j ){
            if( C[j] == '+' ){
				length++;
                A[j] = 1;
            } else if( C[j] == '-' ){
				length++;
                A[j] = 0;
            } else {
				break;
			}
		}
		for( int j = 0; j < length; ++j ){
			if( A[j] == 0 && j + K <= length ){
				flip(j);
			}
		}
		int flag = 0;
		for( int j = 0; j < length; ++j ){
			if( A[j] == 0 ){
				flag = 1;
				break;
			}
		}
		if( flag == 1 ){
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		} else {
			printf("Case #%d: %d\n",i+1,cnt);
		}
    }
	
    return 0;
}

