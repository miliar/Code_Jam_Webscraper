#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
#include <math.h>

#define ll long long
using namespace std;

int main(){

	int T;
	cin >>T;
	int res;
	int N;
	int num_flips;
	for (int t=0;t<T;++t){
		res = 0;
		string pancakes;
		cin>>pancakes>>N;
		num_flips = 0;

		int pancake_len = pancakes.length();

		for (int i=0;i<pancake_len-N+1;++i){
			if (pancakes[i]=='-'){
				num_flips++;
				for (int j=0;j<N;++j){
					if(pancakes[i+j]=='-'){
						pancakes[i+j]='+';
					}else{
						pancakes[i+j]='-';
					}
				}
			}
		}
		for (int i=0;i<pancake_len;++i){
			if (pancakes[i]=='-'){
				res = 1;
			}
		}
		if (res==1){
			cout <<"Case #"<<t+1<<": "<<"IMPOSSIBLE"<<endl;

		}
		else
		{
			cout <<"Case #"<<t+1<<": "<<num_flips<<endl;
		}
	}
	return 0;
}
