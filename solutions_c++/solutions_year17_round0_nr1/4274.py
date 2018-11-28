#include <iostream>
using namespace std;

int main(){
	int TestNum=0;
	cin>>TestNum;
	for( int i=0; i<TestNum; i++ ){
		int FlipperSize;
		string CakeArray;
		cin>>CakeArray>>FlipperSize;
		if ( CakeArray.size() == 0 )
			cout<<"Case #"<<i+1<<": "<<0<<endl;
		//cout<<CakeArray<<":"<<FlipperSize<<endl;
		bool Done=false;
		int FlipCount = 0;
		for( int j=0; j<CakeArray.size(); j++ ){
			//Find next char needs flip.
			int k=j;
			for( ; k<CakeArray.size(); k++ )
				if ( CakeArray[k]=='-' )
					break;
			
			if( k == CakeArray.size() ){
				cout<<"Case #"<<i+1<<": "<<FlipCount<<endl;
				Done=true;
				break;
			}
			if( CakeArray.size()- k<FlipperSize ){
				cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
				Done=true;
				break;
			}
			FlipCount++;
			for( int z=0; z<FlipperSize; z++ )
				CakeArray[z+k]= (CakeArray[z+k]=='-')? '+': '-';
			j=k;
		}
		if( Done==false ){
			cout<<"Case #"<<i+1<<": "<<FlipCount<<endl;
		}
	}
}