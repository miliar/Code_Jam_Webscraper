#include <bits/stdc++.h>

using namespace std;

int main(){
	int n;
	scanf("%d", &n);
	int f = 0;
	while(n--){
		string s;
		cin >> s;
		bool running = true;
		while(running){
			int index = -1;
			int lastnum = s[0] - '0';
			bool wrong = false;
			for(int i=0; i<s.size(); i++){
				int num = s[i] - '0';
				if(lastnum > num){
					index = i;
					wrong = true;
					break;
				}
				lastnum = num;
			}

			if(s[0] == '0'){
				s.erase(s.begin());
				break;
			}

			if(!wrong){
				break;
			}

			for(int i=index; i<s.size(); i++){
				s[i] = '9';
			}
			if(index > 0)
				s[index-1]--;
		}
		if(s[0] == '0')
			s.erase(0);
		cout <<"Case #" << ++f << ": " <<  s << endl;
	}
}
