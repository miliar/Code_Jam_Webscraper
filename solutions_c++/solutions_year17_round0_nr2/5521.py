#include<stdio.h>
#define MAX_T 100
using namespace std;

int length;
long long int N = 0;

int getLength(){
	length = 1;	
	long long int tmp = N;
	while(tmp/10>0){
		length++;
		tmp/=10;
	}
	return length;
}

int getNumber(int index){
	long long int tmp = N;
	for( int i = 1; i < length-index; ++i ){
		tmp/=10;
	}
	return tmp%10;
}

int setNumber(int index, int num ){
	long long int a = 1;
	long long int current = getNumber(index);
	for( int i = 1; i < length-index; ++i ){
		a*=10;
	}
	if( current > num ){
		N -= (current-num)*a;
	} else if( num > current ){
		N += (num-current)*a;
	}
}

int main(){
	int T;
	freopen("B_input.txt","r",stdin);
	freopen("B_output.txt","w",stdout);
	scanf("%d", &T);
    for( int i = 0; i < T; ++i ){
		scanf("%lld",&N);
		getLength();
		while(true){
			int index = 0;
			long long int tmp = N;
			while( index < length-1){
				int a = getNumber(index);
				int b = getNumber(index+1);
				int flag = 0;
				if( a > b ){
					setNumber(index,a-1);
					for( int i = index+1; i < length; ++i ){
						setNumber(i,9);
					}
					break;
				}
				index++;
			}
			if( N == tmp ){
				printf("Case #%d: %lld\n",i+1,N);
				break;
			}
		}
    }
	
    return 0;
}

