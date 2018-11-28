#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

void getDigits(int64_t n, vector<int> &l){
	while(n){
        	l.push_back(n%10);
                n /= 10;
        }
}


void isChange(int64_t i, vector<int> &l, bool &change, int64_t &changeIndex){
		while(i - 1 >= 0){
                        if(l[i] > l[i-1]){
                                change = true;
                                changeIndex = i;
                                break;
                        }
                        i--;
                }
}

void print9(int64_t count){
	for(int64_t i = 0; i < count; i++)
		cout << "9";
}

int main(){
	int t;
	cin >> t;

	int64_t n;
	for(int loop = 1; loop <= t; loop++){
		cin >> n;

		vector<int> l;
		getDigits(n, l);

		cout << "Case #" << loop <<": ";
		bool change = false;
		int64_t size = l.size();
		int64_t i = size - 1;
		int64_t changeIndex;

		isChange(i, l, change, changeIndex);

		i = size - 1;
		if(!change){
			while(i >= 0){
				cout << l[i];
				i--;
			}
		}
		else{
			bool flag = false;
			for(int64_t j = changeIndex; j < size - 1; j++){
				if((l[changeIndex] - 1) >= l[changeIndex+1]){
					flag = true;
					break;
				}
			}
	
			l[changeIndex] -= 1; 	
			if(flag){
				for(int64_t k = size - 1; k >= changeIndex; k--)
					cout << l[k];

				print9(changeIndex);
			}
			else{
				if((l[changeIndex]) > 0)
				cout << l[changeIndex];	
				print9(size-1);
			}	
		}
	
		cout << endl;
	}	
	return 0;
}
