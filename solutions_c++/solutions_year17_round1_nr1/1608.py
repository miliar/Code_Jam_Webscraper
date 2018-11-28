#include <iostream>
#include <cstring>
using namespace std;

/*
G??A?
?C??B
?????
???J?

???A
???K
?Z?J
?Y??
*/

int main(){
	int tc;
	cin >> tc;
	for (int t=1;t<=tc;t++){
		int n, m; string s[30];
		cin >> n >> m;
		for (int i=0;i<n;i++) {
			cin >> s[i];
		}
		for (int i=0;i<n;i++){
			for (int j=0;j<m-1;j++){
				if (s[i][j+1] =='?'){
					s[i][j+1] = s[i][j];
				}
			}
			for (int j=m-1;j>=1;j--){
				if (s[i][j-1] =='?'){
					s[i][j-1] = s[i][j];
				}
			}
		}
		for (int i=0;i<m;i++){
			for (int j=0;j<n-1;j++){
				if (s[j+1][i] =='?'){
					s[j+1][i] = s[j][i];
				}
			}
			for (int j=n-1;j>=1;j--){
				if (s[j-1][i] =='?'){
					s[j-1][i] = s[j][i];
				}
			}
		}

		cout << "Case #" << t << ": "<< endl;
		for (int i=0;i<n;i++){
			cout << s[i]<< endl;
		}
	}
	return 0;
}
