#include<iostream>
#include<cstring>

using namespace std;

int main() {
	int t, temp, k, next, curr, len;
	char s[20], result[20];
	cin >> t;
	temp = t;
	while(t--) {
		cin >> s;
		memset(result, 0, sizeof(result));
		len = strlen(s);
		for(int i = len-1; i > 0; i--){
			curr = s[i] - '0';
			next = s[i-1] - '0';
			//cout << "\n" << next << curr;
			if(next > curr){
				next = next - 1;
				for(int j = i; j < len; j++){
					s[j] = '9';
				}
				s[i-1] = (char)(next + '0');
			}
		}
		k = 0;
		while(s[k] == '0'){
			k++;
		}
		for(int i = k; i < len; i ++){
			result[i-k] = s[i];
		}
		cout << "Case #" << temp - t << ": " << result << endl;
	}	
	return 0;
}