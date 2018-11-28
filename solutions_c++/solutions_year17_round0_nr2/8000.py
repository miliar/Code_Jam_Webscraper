#include <iostream>
#include <string>

using namespace std;

string s;
void solve(){
	static int caseNumber = 1;
	for(int i=0;i<s.size()-1;i++)
		if(s[i]>s[i+1]){
			int j = i;
			while(s[j] == '0' || (j>0 && s[j] == s[j-1]))
				j--;
			s[j++] -= 1;
			while(j < s.size())
				s[j++] = '9';
			break;
		}
	cout << "Case #" << caseNumber++ << ": ";
	int i = 0;
	while(s[i] == '0') i++;
	cout << s.substr(i) << endl;

}

int main(){

	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		cin >> s;
		solve();
	}

	return 0;
}