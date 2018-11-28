#include <iostream>
#include <vector>

using namespace std;


int main(){
	
	int T;
	long long in, tmp;
	
	
	cin >> T; 
	
	for(int t = 1; t <= T; t++){
		
		cin >> in;
		tmp = in;
		vector<int> cal;
		
		if(in < 10){
			cout << "Case #" << t << ": ";
			cout << in << endl;
			continue;
		} 
		
		while(tmp != 0){
			int n = tmp % 10;
			cal.push_back(n);
			tmp /= 10;
		}
		
		for(int i = 0; i < cal.size() - 1; i++){
			if(cal[i] < cal[i + 1]){
				cal[i] = 9;
				cal[i + 1] = 0 ? 9 : cal[i + 1] - 1;
				
				int j = i;
				while(cal[j] > cal[j - 1]){
					cal[j - 1] = 9;
					j--;
				}
			}
		}
		
		cout << "Case #" << t << ": ";
		for(int i = cal.size() - 1, ch = 0; i >= 0; i--){
			if(cal[i] == 0 && !ch) continue;
			ch = 1;
			cout << cal[i];
		}
		cout << endl;
		
	}
	
	return 0;
}