#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<list>

using namespace std;

int ctoi(char c) {
	return (int)c - 48;
}

long jump(long num) {
	string str = std::to_string(num);
	for(int i = str.length() - 1; i > 0; i--) {
		if(ctoi(str[i]) < ctoi(str[i-1])) {
			for(int j = i; j < str.length(); j++) {
				str[j] = '0';
			}
			break;
		}
	}

	return std::stol(str);
}

bool isTidy(long num) {

	string str = std::to_string(num);
	
	if(str.length() == 1) {
		return true;
	}

	for(int i = str.length() - 1; i > 0; i--) {
		if(ctoi(str[i]) < ctoi(str[i-1])) {
			return false;
		}
	}
	
	return true;
}

int main(){
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;
    cin>>T;

    for(int t=1; t<=T; t++){
        printf("Case #%d: ",t);
        long input;
        cin>>input;
        for(long i = input; i >= 0; i--) {
        	if(isTidy(i)) {
        		cout<<i<<endl;
        		break;
        	} else {
        		i = jump(i);
        	}
        }
    }

return 0;
}
