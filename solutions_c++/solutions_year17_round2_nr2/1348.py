#include <iostream>
using namespace std;
int main(){
	int zes;
	cin>>zes;
	for(int k = 1; k <= zes; k++){
		int N;
		cin>>N;
		char R[N];
		int r, o, y, g, b, v;
		cin>>r>>o>>y>>g>>b>>v;

		if(r >= y && r >= b){
			R[0] = 'R';
			r--;
		}else{
			if(y >= r && y >= b){
				R[0] = 'Y';
				y--;
			}
			else{
				R[0] = 'B';
				b--;
			}
		}
		bool lel = 1;
		int i;
		for(i = 1; i < N; i++){
			if(r == b && b == y) break;
			char last =  R[i - 1];
			if(last == 'B'){
				if(r== 0 && y == 0){
					lel = 0;
					break;
				}
				if(r >= y){
					R[i] = 'R';
					r--;
				}else{
					R[i] = 'Y';
					y--;
				}
			}
			if(last == 'R'){
				if(b== 0 && y == 0){
					lel = 0;
					break;
				}
				if(b >= y){
					R[i] = 'B';
					b--;
				}else{
					R[i] = 'Y';
					y--;
				}
			}
			if(last == 'Y'){
				if(r== 0 && b == 0){
					lel = 0;
					break;
				}
				if(r >= b){
					R[i] = 'R';
					r--;
				}else{
					R[i] = 'B';
					b--;
				}
			}
		}if(lel){
				char start = R[0];
				char last = R[i - 1];
				char x,yy,z;
				if(last != start){
					yy = start;
					z = last;
					if('B' != start && 'B' != last)
						x = 'B';
					if('Y' != start && 'Y' != last)
						x = 'Y';
					if('R' != start && 'R' != last)
						x = 'R';
				}else{
					yy = last;
					if('R' == last){
						x = 'Y';
						z = 'B';
					}
					if('B' == last){
						x = 'Y';
						z = 'R';
					}
					if('Y' == last){
						x = 'R';
						z = 'B';
					}
				}
				
				 
				while(i < N){
					R[i] = x;
					R[i+1] = yy;
					R[i+2] = z;
					i +=3;
				}
				bool ok = 1;
				for(int i = 0; i < N - 1; i++){
					if(R[i] == R[i + 1]) ok = 0;
				}
				if(R[N-1] == R[0]) ok = 0;
				cout<<"Case #"<<k<<": ";
				if(ok!=0){
					for(int i = 0; i < N; i++) cout<<R[i];
				}else{
					cout<<"IMPOSSIBLE";
				}
				cout<<endl;
			}else{
				cout<<"Case #"<<k<<": ";
				cout<<"IMPOSSIBLE";
				cout<<endl;
			}
	}
}
