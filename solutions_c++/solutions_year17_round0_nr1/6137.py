#include<iostream>
#include<cstring>
using namespace std;

int main(){
int t;
cin >> t;
for(int l = 1;l<=t;l++){
char s[1001];
int k,ans = 0;
cin >> s;
cin >> k;
//cout << s;
for(int i = 0;i<=strlen(s) - k;i++){
	if(s[i] == '-'){
		ans ++;
		for(int j = 0;j<k;j++){
			s[i+j] = s[i+j] == '-'?'+':'-';
		}
	}
	
}

//cout << s << ans << endl;
for(int i = strlen(s) - k + 1;i<strlen(s);i++){
	if(s[i] == '-'){
		cout << "Case #"<<l<<": "<< "IMPOSSIBLE" << endl;
		ans = -1;
		break;
	}	
}
if(ans != -1)
cout << "Case #"<<l<<": "<<ans << endl;
}
}

