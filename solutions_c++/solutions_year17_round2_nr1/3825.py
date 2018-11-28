#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i = 0 ; i < T; i++){
		int Distance,N;
		cin >> Distance >> N;
		float MaxTime_StartPos = 0;
		float MaxTime_Speed = 0;
		float MaxTime_Hour = 0.0;
		for(int n = 0 ; n < N ; n++){
			int pos,spd;
			float hour;
			cin >> pos >> spd;
			hour = ((Distance - pos) / float(spd));
			//cout << " Distance : " << Distance << " - " << pos << " & Speed : "<< spd << endl;
			//cout << " Hour : " << hour << endl;
			//if(hour == 0)hour = 1;
			if(MaxTime_Hour - hour < 0)MaxTime_Hour = hour;
		}
		//cout << "This case , Hour : " << MaxTime_Hour << " , Speed must be " << Distance / MaxTime_Hour << endl;
		float rst = 0.0;
		if(MaxTime_Hour == 0){
			rst = Distance;
			//printf("Case #%d: %d\n",i+1,int(Distance));
			//cout << "Case #" << i+1 << ": " << Distance << endl;
		}else{
			rst = float(Distance/MaxTime_Hour);
			//printf("Case #%d: %6f\n",i+1,rst);
			//cout << "Case #" << i+1 << ": " << rst << endl;
		}

		printf("Case #%d: %6f\n",i+1,rst);
		
		//cout << "Case #" << i+1 << ": " << float(Distance/MaxTime_Hour) << endl;  
	}
	return 0;
} 