#include <iostream>

using namespace std;

int solve(string seq, int s){
	int l = seq.length();
	int i=0;

	int count=0,j;
//	cout <<"before flip"<< seq <<endl;	
	while  (i<l){ // still not all flipped{ 
		while (i<l &&seq.at(i)=='+'){i++;} // find next -
		// flip
		if (i<l&&seq.at(i)=='-'){
		for (j=i;j<i+s;j++){
			if (j >=l){return -1;} // we cannot flip here
			seq[j] = (seq.at(j) == '-'? '+':'-');
		}
		//flip was succesful
		count++;
		}
		i++;
		
//		 cout <<"flip"<< seq << " "<<count<< endl;	
	}
	return count;
}



int main (){
	int	test;
	int cur;
	string seq;
	cin >> test;
	
	for (int i =1;i<=test;i++){
		cin >> seq;
		cin >>cur;

		cur =solve(seq, cur);
		if (cur <0){
		cout << "Case #"<<i<<":"<< " "<<"IMPOSSIBLE"<<endl;
		}else{
		cout << "Case #"<<i<<":"<< " "<<cur<<endl;
		
		}
	};

}
