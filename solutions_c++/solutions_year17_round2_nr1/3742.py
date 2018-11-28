#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int TestNum=0;
	cin>>TestNum;
	for( int i=0; i<TestNum; i++ ){
		int Dst,HorseNum;
		cin>>Dst>>HorseNum;
		double TimeMax = 0;
		for( int j=0; j<HorseNum; j++ ){
			int Loc, Speed;
			cin>>Loc>>Speed;
			double Time = double(Dst-Loc)/double(Speed);
			TimeMax = (Time>TimeMax)? Time: TimeMax;
		}
		double MySpeed = double(Dst)/TimeMax;
		printf("Case #%d: %f\n",i+1, MySpeed);
	}
}