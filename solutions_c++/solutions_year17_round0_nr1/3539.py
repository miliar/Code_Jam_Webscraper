#include<fstream>
using namespace std;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int t = 0;
	fin >> t;

	char s[1001];
	int k;
	for(int kk = 1; kk <= t; kk++){
		int ans = 0;
		fin >> s >> k;
		int l = strlen(s);
		for(int i = 0; i < l - k + 1; i++) {
			if(s[i] == '-') {
				ans++;
				for(int j = 0; j < k; j++) {
					s[i + j] = (s[i + j] == '-') ? '+' : '-';
				}
			}
		}
		bool mark = true;
		for(int i = l - k + 1; i < l; i++) {
			if(s[i] == '-') {
				mark = false;
			}
		}
		if(mark)
			fout << "Case #" << kk << ": " << ans << endl;
		else
			fout << "Case #" << kk << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}