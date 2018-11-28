#include <iostream>
#include <sstream>
#include <string>

using namespace std;
int main()
{
	int n;
	cin >> n;
	for (int i=0; i < n; i++) {
		string s;
		int k;
		cin >> s >> k;
		int m = (int) s.size();
		int num = 0;
		int isPossible = -1;
		while (true){
			for(int j=0;j<m;j++){
				if(s[j] == '-'){
					if(j+k>m){
						isPossible = 0;
						break;
					}
					num++;
					for(int l=j;l<j+k;l++){
						if(s[l]=='-'){
							s[l]='+';
						}else{
							s[l]='-';
						}
					}
				}
				if(isPossible != 0 && j==m-1){
					isPossible = 1;
				}
			}
			cout << "Case #" << i+1 << ": ";
			if(isPossible==0){
				cout << "IMPOSSIBLE" << endl;
				break;
			}
			if(isPossible == 1){
				cout << num << endl;
				break;
			}
		}


	}
}


