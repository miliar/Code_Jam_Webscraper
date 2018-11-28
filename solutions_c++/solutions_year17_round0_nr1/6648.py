#include<iostream>
#include<string>

using namespace std;

int fryingPan; string pancakes;

string strSwap(int a, string currentPancake){
	string temp = currentPancake;
	for(int i = a; i < a + fryingPan; ++i){
		if(temp[i] == '-'){
			temp[i] = '+';
		} else if (temp[i] == '+'){
			temp[i] = '-';
		}
	} 
	return temp;
}

void panFlip(int a , string currentPancake, int flips, int &minFlips){
	if(a + fryingPan > pancakes.length()){
		bool event = true;
		for(int i = 0; i < pancakes.length(); ++i){
			if(currentPancake[i] == '-'){ 
				event = false;
				break;
			}
		}
		
		if(event){
			if((minFlips > flips) || (minFlips == -1)){
				minFlips = flips;
			}
		}
	} else {
		string b = strSwap(a, currentPancake);
		
		if(b[a] == '+'){
			panFlip(a+1,b,flips+1,minFlips);
		} else {
			panFlip(a+1,currentPancake,flips,minFlips);
		}
		

	}
}



int main(){
	int TC;
	cin >> TC;
	
	for(int iTC = 0; iTC < TC; iTC++){
		
		cin >> pancakes >> fryingPan;
		
		int result = -1;
		
		panFlip(0,pancakes,0,result);
		
		cout << "CASE #" <<  iTC+1 << ": ";
		
		if(result ==-1){
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << result << endl;
		}
	}
	
	return 0;
}
