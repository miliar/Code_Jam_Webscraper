#include<cstdio>
#include<cstring>
using namespace std;

int treat(char *s){
    	int n = strlen(s);
    	bool det = false;
    	for(int i=0;i<n;i++){
    		if(det) s[i]='9';
    		else if(!det && i<n-1 && s[i] > s[i+1]){
    			det = true; s[i]--;
    		}
    	}
}

bool good(char *s){
	int n = strlen(s);
	for(int i=0;i<n-1;i++){
		if(s[i]>s[i+1]) return false;
	}
	return true;
}
    	
int main(){
	int T; scanf("%d",&T);
	for(int ti=1;ti<=T;ti++){
    	char s[22]; scanf("%s", s);
    	while(true){
    		if(good(s)) break;
    		treat(s);
    	}
    	char *t = s;
    	while(t[0] == '0') t++;
    	printf("Case #%d: %s\n", ti, t);
	}
	return 0;
}
