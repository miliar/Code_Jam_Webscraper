#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int main(){
	int t; cin >> t;
	for(int i = 0; i < t; i++){
		string s; int k; cin >> s >> k;
		string _s = s; reverse(_s.begin(), _s.end());
		int cnt = 0;
		for(int j = 0; j < s.size(); j++){
			if(j + k - 1 >= s.size()) break;
			if(s[j] == '-'){
				cnt++;
				for(int p = 0; p < k; p++){
					if(s[p + j] == '-') s[p + j] = '+';
					else s[p+j] = '-';
				}
			}
		}
		for(int j = 0; j < s.size(); j++) if(s[j] == '-') cnt = -1;
		s = _s;
		int cnt2 = 0;		
		for(int j = 0; j < s.size(); j++){
                        if(j + k - 1 >= s.size()) break;
                        if(s[j] == '-'){
                                cnt2++;
                                for(int p = 0; p < k; p++){
                                        if(s[p + j] == '-') s[p + j] = '+';
                                        else s[p+j] = '-';
                                }
                        }
                }
		for(int j = 0; j < s.size(); j++) if(s[j] == '-') cnt2 = -1;

		int ans = min(cnt, cnt2);
		if(ans == -1) cout << "Case #" << i+1 << ": " << "IMPOSSIBLE"<< endl;
		else
			cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}
			
		
