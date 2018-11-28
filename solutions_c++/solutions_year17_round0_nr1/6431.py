#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int t,i,j,k=1,count=0,length;
	bool imp=false;
	string s;
	int key;
	cin >> t;
	while(k <= t){
		count = 0;
		imp=false;
		cin >> s >> key;
		length = s.length();
		for(i= 0 ; i < length-key+1 ; i++){
			if(s[i] == '-'){
				++count;
				for(j=0;j<key;j++){
					if(s[j+i] == '-')s[j+i] = '+';	
					else{
						s[j+i] = '-';
					}
				} 
			}
		}

		for(i = 0; i <= length/2 ; i++){
			if(s[i] == '-' || s[length-i] == '-'){
				imp = true;
				break;
			}
		}
		cout << "Case #" << k << ": ";
		if(imp) cout << "IMPOSSIBLE";
		else cout << count;
		cout << endl;
		k++;
	}
	return 0;
}