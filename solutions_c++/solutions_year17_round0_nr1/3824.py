#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int T; cin >> T;
	string inp;
	int K;
	for(int a0=1;a0<=T;a0++){
		cin >> inp >> K;
		int len = inp.size();
		int count = 0;
		for(int a1=0;a1<=len-K;a1++){
			if(inp[a1]=='-'){
				for(int a2=a1;a2<a1+K;a2++){
					if(inp[a2]=='+'){
						inp[a2] = '-';
					}else{
						inp[a2] = '+';
					}
				}
				count++;
			}
		}
		bool flip = true;
		for(int a1=len-K+1;a1<len;a1++){
			if(inp[a1]=='-'){
				flip = false;
				break;
			}
		}
		if(flip){
			printf("Case #%d: %d\n",a0,count);
		}else{
			printf("Case #%d: IMPOSSIBLE\n",a0);
		}
	}
	return 0;
}