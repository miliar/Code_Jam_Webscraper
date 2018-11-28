// Example program
#include <string>
#include <sstream>
#include<vector>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int N, K;

struct neigh{
	int L;
	int R;
	int index;
	bool empty;
	bool last;

	int getMin(){
		if(L > R){
			return R;
		}else{
			return L;
		}
	}
	int getMax(){
		if(L>R){
			return L;
		}else{
			return R;
		}
	}
};

void initializeArr(neigh* arr){
	for(int i = 0; i < N; i++){
		arr[i].L = i;
		arr[i].R = N-i-1;
		arr[i].index = i;
		arr[i].empty = true;
		arr[i].last = false;
	}
}

void updateNeighboors(neigh*arr){
	for(int i = 0; i < N; i++){
		int l_index = i-1;
		int r_index = i+1;
		while(l_index >= 0){
			if(arr[l_index].empty == false){
				arr[i].L =  arr[i].index - l_index-1;
				break;
			}
			l_index--;
		}
		while(r_index < N){
			if(arr[r_index].empty == false){
				arr[i].R = r_index - arr[i].index-1;
				break;
			}
			r_index++;
		}
	}
}
int main() {
	int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> N;  // read n and then m.
		cin >> K;
		vector<neigh> myvec;
		neigh max;
		neigh arr[N];
		initializeArr(arr);
	    neigh last;
		while(K > 0){
			int min = arr[0].getMin();
			int index = 0;
			for(int j = 0; j < N; j++){
				if(arr[j].empty == true){
					if(arr[j].getMin() > min){
					    index = j;
					    min = arr[j].getMin();
					}
				}
			}
			
			for(int j=0; j < N; j++){
				if(arr[j].getMin() == arr[index].getMin()){
				    if(arr[j].empty == true){
					    myvec.push_back(arr[j]);
				    }
				}				
			}
			
			int maxNum = myvec[0].getMax();
			max = myvec[0];
			for(int j = 0; j < myvec.size(); j++){
				if(myvec[j].getMax() > maxNum){
					max = myvec[j];
					maxNum = myvec[j].getMax();
				}
			}
			arr[max.index].empty = false;
			if(K==1){
			    last = max;
			}
			K--;
			updateNeighboors(arr);			
			myvec.clear();
		}
		cout << "Case #" << i << ": " << last.getMax() << " " << last.getMin() << endl;
	}
}
