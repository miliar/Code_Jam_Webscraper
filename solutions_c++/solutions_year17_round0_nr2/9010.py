#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main(){
	int t;
	scanf("%d", &t);

	for(int n = 1; n <= t; n++){
		printf("Case #%d: ", n);

		char in[20];
		scanf("%s", in);

		char last = '0';
		for(int i = 0; in[i]; i++){
			if(last > in[i]){
				for(int j = i; in[j]; j++){
					in[j] = '9';
				}

				last = --in[i - 1];
				if(last == '0') {
					last = in[i - 1] = '9';
				}
				for(int j = i - 2; j >= 0; j--){
					if(last == '9' || in[j] > last){
						in[j] = last;
					}
					else{
						break;
					}
				}
				
				if(last == '9'){
					in[0] = '0';
				}
				break;
			}
			last = in[i];
		}

		printf("%s\n", *in == '0' ? in + 1 : in);
	}
}
