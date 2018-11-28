#include<iostream>
#include<math.h>
#include<vector>
#include<string>

using namespace std;

int main(){
	int T;
	cin >> T;
	int N;
	int R;
	int O;
	int Y;
	int G;
	int B;
	int V;
	for(int i = 0; i<T; i++){
		cout << "Case #" << i+1 << ": ";
		cin >> N >> R >> O >> Y >> G >> B >> V;
		R = R-G;
		Y = Y-V;
		B = B-O;
		if(R<=Y+B && Y<=R+B && B<=R+Y && !(R*Y*B==0 && O*G+G*V+V*O!=0)){
			string state = "";
			while(R+Y+B != 0){
				if(state.back() == 'R'){
					if(B>Y){
						state+='B';
						B--;
					}
					else{
						state+='Y';
						Y--;
					}
				}
				else if (state.back() == 'Y'){
					if(B>R){
						state+='B';
						B--;
					}
					else{
						state+='R';
						R--;
					}
				}
				else{
					if(Y>R){
						state+='Y';
						Y--;
					}
					else{
						state+='R';
						R--;
					}
				}
			}
			size_t firstR = state.find('R');
			while(G>0){
				state.insert(firstR+1,"GR");
				G--;
			}
			size_t firstY = state.find('Y');
			while(V>0){
				state.insert(firstY+1,"VY");
				V--;
			}
			size_t firstB = state.find('B');
			while(O>0){
				state.insert(firstB+1,"OB");
				O--;
			}
			
			cout << state << endl;
		}
		else{
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}