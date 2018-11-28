#include<bits/stdc++.h>

using namespace std;

int main(){

	int t, caso = 0;
	
	cin >> t;
	
	while(t--){
		caso++;
		
		string s;
		int k;
		
		cin >> s >> k;	
		
		int ans = 0;
		
		for(int i = 0; i < s.length(); i++)
			if (i < s.length() - k + 1){
				if (s[i] == '-'){
					ans++;
				
					for (int j = i; j < i + k; j++){
						if (string(1, s[j]) == "+")
							s[j] = '-';
						else
							s[j] = '+';	
					}	
				}	
			}else{
				if (s[i] == '-'){
					ans = -1;
					break;
				}	
			}
			
		printf("Case #%d: ", caso);	
		
		if (ans == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;	
	}

	return 0;
}
