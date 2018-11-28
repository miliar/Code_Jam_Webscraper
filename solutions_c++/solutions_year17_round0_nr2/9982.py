#include <iostream>
#include <vector>

using namespace std;

int main(){
	int t;
	cin >> t;

	int n;
	for(int loop = 1; loop <= t; loop++){
		cin >> n;

		vector<int> l;
		while(n){
			l.push_back(n%10);
			n /= 10;
		} 

		cout << "Case #" << loop <<": ";
		bool change = false;
		int size = l.size();
		int i = size - 1;
		int changeIndex;
		while(i - 1 >= 0){
			if(l[i] > l[i-1]){
				change = true;
				changeIndex = i;
				break;
			}
			i--;
		}

		//cout << change << endl;
		i = size - 1;
		if(!change){
			while(i >= 0){
				cout << l[i];
				i--;
			}
		}
		else{
			bool flag = false;
			for(int j = changeIndex; j < size - 1; j++){
				if((l[changeIndex] - 1) >= l[changeIndex+1]){
					flag = true;
					break;
				}
			}
	
			l[changeIndex] -= 1; 	
			//cout << flag << ":" << l[changeIndex] << endl;
			if(flag){
				for(int k = size - 1; k >= changeIndex; k--)
					cout << l[k];

				for(int k = changeIndex - 1; k >= 0; k--)
					cout << "9";
			}
			else{
				if((l[changeIndex]) > 0)
				cout << l[changeIndex];	
				for(int k = 0; k < size - 1; k++)
					cout << "9";
			}	
		}
	
	
		cout << endl;
	}	
	return 0;
}
