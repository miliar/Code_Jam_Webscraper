#include <iostream>
using namespace std;

int main(){
	int TestNum=0;
	cin>>TestNum;
	for( int i=0; i<TestNum; i++ ){
		string NumArray;
		cin>>NumArray;
		for( int j=NumArray.size()-1; j>=0; j-- ){
			if( j-1<0 )
				break;
			if( NumArray[j-1]>NumArray[j] ){
				NumArray[j-1]--;
				NumArray[j]='9';
				int k=j+1;
				for( ; k<NumArray.size(); k++ )
					if( NumArray[k] >= '9' )
						break;
					else
						NumArray[k] = '9';
			}
		}
		int PutDigital=0;
		int j=0;
		cout<<"Case #"<<i+1<<": ";
		for( ; j<NumArray.size(); j++ )
			if( NumArray[j]!='0' )
				break;
		for( ; j<NumArray.size(); j++ ){
			PutDigital++;
			cout<<NumArray[j];
		}
		if ( PutDigital == 0 )
			cout<<"0";
		cout<<endl;
	}
}