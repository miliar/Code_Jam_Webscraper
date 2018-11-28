#include <stdio.h>
#include <string>
using namespace std;

bool checkPos(string& val, int pos){
	int n = (int)val.size();
	for(int i=pos+1;i<n;++i){
		if(val[i] < val[pos]) return false;
		if(val[i] > val[pos]) return true;
	}
	return true;
}

string tostring(long long v){
	string ret;
	while(v > 0){
		int d = v%10;
		ret = (char)(d + '0') + ret;
		v /= 10LL;
	}
	return ret;
}

long long getAns(long long val){
	string str = tostring(val);
	int n = (int)str.size();
	if(n == 1) return val;

	long long ans = 0LL;
	bool fin = false;
	for(int i=0;i<str.size();++i){
		if(fin){
			ans = ans * 10LL;
		}else if(checkPos(str, i) == false){
			fin = true;
			ans = ans * 10LL + (long long)(str[i] - '0');
		}else{
			ans = ans * 10LL + (long long)(str[i] - '0');
		}
	}
	
	return ans - (fin?1LL:0LL);
}
int main(){
	int tests; scanf("%d\n", &tests);
	for(int t=1;t<=tests;++t){
		long long n; scanf("%lld", &n);
		printf("Case #%d: %lld\n", t, getAns(n));
	}
	return 0;
}
