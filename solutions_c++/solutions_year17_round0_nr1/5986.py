#include<iostream>
#include<vector>
using namespace std;


bool isHappy(string pancakes){
	for(int i=0; i<pancakes.size(); i++){
		if( pancakes[i] == '-' ){
			return false;
		}
	}
	return true;
}

int getMinFlip(string p, int fSize){

	int c = 0;
	for( int i=0; i<p.size()-fSize+1; i++ ){
		if( p[i] == '+' ) {
			continue;
		}
		else {
			
			if( isHappy(p) ){
				return c;
			} else {
				//Check if flip is possible
				if ( p.size() - i < fSize ) return -1;

				for( int j=i; j<i+fSize; j++ ){
					if( p[j]=='+' ){
						p[j] = '-';
					} else {
						p[j] = '+';
					}
				}
				c++;
			}
		}
	}

	return (isHappy(p))?c:-1;
}


int main(){
	int n; 
	cin >> n;
	string pancakes;
	int flipperSize = 1;
	int results = 0;

	for( int i=0; i<n; i++ ){
		cin>>pancakes;
		cin>>flipperSize;
		results = getMinFlip(pancakes, flipperSize);
		if ( results >= 0 ){
			cout<<"Case #"<<(i+1)<<": "<<results<<endl;
		} else {
			cout<<"Case #"<<(i+1)<<": IMPOSSIBLE"<<endl;
		}
	}
}