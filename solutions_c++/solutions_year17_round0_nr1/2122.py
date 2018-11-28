#include <iostream>

using namespace std;

int main() {
	
	int T,caseno=1;
	cin >> T;
	while (caseno<=T) {
		
		char s[1001];
		int k,n,i;
		cin >> s >> k;
		for (n=0;s[n]!='\0';n++);
		
		int flip=0,ans=0,t=0;
		int drop[1000]={0};
		
		for (i=n-1;i>=k-1;i--) {
			if (drop[i]) flip--;
			if (flip%2==1) s[i]= '+' + '-' - s[i];
			
			if (s[i]=='-') {
				s[i]='+';
				flip++;
				ans++;
				if (i!=k-1) drop[i-k]=1;
			}
		}
		for (;i>=0;i--) {
			if (drop[i]) flip--;
			if (flip%2==1) s[i]='+' + '-' -s[i];
			
			if (s[i]=='-') break;
		}
		
		//cout << s << ' ';
		cout << "Case #" << caseno << ": ";
		if (i<0) cout << ans << '\n';
		else cout << "IMPOSSIBLE\n";
		
		caseno++;
	}
	
	return 0;
}
