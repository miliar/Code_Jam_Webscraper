#include <bits/stdc++.h>
using namespace std;
#define lln long long int

int main(){
	lln t;
	cin >> t;
	for(lln i=0;i<t;i++){
		string s;
		cin >> s;
		lln k;
		cin >> k;
		lln cou=0,flag=0;
		cout << "Case #" << i+1 << ": ";
		for(lln j=0;j<s.length();j++){
			if(s[j]=='-'){
				if((j+k-1)>=s.length()){
					cout << "IMPOSSIBLE" << endl;
					flag=1;
					break;
				}
				for(lln u=j;u<j+k;u++){
					if(s[u]=='-')
						s[u] = '+';
					else
						s[u] = '-';
				}
				cou++;
			}//cout << s << " ";
		}
		if(flag==0)
			cout << cou << endl;
	}
	return 0;
}