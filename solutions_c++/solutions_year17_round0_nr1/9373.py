#include <bits/stdc++.h>
using namespace std;

int main(){
	int test_cases;
	cin >> test_cases;
	int case_no = 0;
	while(test_cases--){
		case_no++;
		bool flag = false;
		int count = 0,i = 0,j,k;
		string pancake;
		cin >> pancake >> k;
		while(i<pancake.size()){
			while(pancake[i]=='+')
				i++;
			if(i>=pancake.size()-k+1){
				if(i==pancake.size())
					break;
				else
					flag = true;
					break;
			}
			else{
				for(j=i;j<i+k;j++){
					if(pancake[j]=='-')
						pancake[j] = '+';
					else
						pancake[j] = '-';
				}
				count++;
			}			
		}
		if(flag){
			cout << "Case #" << case_no << ": " << "IMPOSSIBLE" << endl;
		}
		else
			cout << "Case #" << case_no << ": " << count << endl;
	}
	return 0;
}