#include <iostream>
#include <string>
#include <vector> 
#include <set>
using namespace std;

int main(){
	int testCase;
	int R,C;
	int walker;
	cin >> testCase;
	for(int t=1;t<=testCase;t++){

		cout << "Case #" << t << ":" << endl;
		cin >> R >> C;
		vector<string> board(R);
		std::set<int> undone;
		for(int r=0;r<R;r++){
			cin >> board[r];
			bool allQ = true;
			for(int i=0;i<C;i++){
				walker = 1;
				if(board[r][i] != '?'){
					allQ = false;
					while(i+walker<C && board[r][walker+i]=='?'){
						board[r][walker+i] = board[r][i];
						walker++;
					}
					walker = -1;
					while(i+walker>=0 && board[r][walker+i]=='?'){
						board[r][walker+i] = board[r][i];
						walker--;
					}
				}
			}
			if(allQ)
				undone.insert(r);
		}
		int counter = 1;
		int last=0;
		for(int i=0;i<R;i++){
			if(undone.find(i) != undone.end())
				counter++ ;
			else{
				last = i;
				for(int tmp=0;tmp<counter;tmp++)
					cout << board[i] << endl;
				counter=1;
			}
		}
		for(int tmp=1;tmp<counter;tmp++)
					cout << board[last] << endl;
	}
	return 0;
}