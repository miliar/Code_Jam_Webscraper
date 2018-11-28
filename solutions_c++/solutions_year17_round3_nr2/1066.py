
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int t[1440];
int no_cases;

class timeslot{
public:
	int start;
	int end;
	int cls;
};
vector<timeslot> arr;

bool cmp1(timeslot ts1, timeslot ts2){
	return ts1.start<ts2.start;
}


int main(){
	cin>>no_cases;
	for (int caseID=1; caseID<=no_cases; caseID++){
		arr.clear();
		int Ac, Aj;
		int Ci, Di, Ji, Ki;
		int remain1=720, remain2=720;
		memset(t, -1, sizeof(t));
		cin>>Ac>>Aj;

		for (int i=0; i<Ac; i++){
			cin>>Ci>>Di;
			remain1-=(Di-Ci);
			timeslot ts;
			ts.start=Ci;
			ts.end=Di;
			ts.cls=1;
			arr.push_back(ts);
			for (int j=Ci; j<Di; j++)
				t[j]=1;

		}
		for (int i=0; i<Aj; i++){
			cin>>Ji>>Ki;
			remain2-=(Ki-Ji);
			timeslot ts;
			ts.start=Ji;
			ts.end=Ki;
			ts.cls=2;
			arr.push_back(ts);
			for (int j=Ji; j<Ki; j++)
				t[j]=2;
		}
		sort(arr.begin(), arr.end(), cmp1);

		if ( (Ac==2 && Aj==0) || (Ac==0 && Aj==2) ){

			int start1=arr[0].start;
			int start2=arr[1].start;
			int end1=arr[0].end;
			int end2=arr[1].end;
			if ( (end2-start1)<=720)
				cout<<"Case #"<<caseID<<": "<<2<<endl;
			else if ( (end1+1440-start2) <=720)
				cout<<"Case #"<<caseID<<": "<<2<<endl;
			else
				cout<<"Case #"<<caseID<<": "<<4<<endl;


		}
		else if ( (Ac==1 && Aj==0) || (Ac==0 && Aj==1) ){
			cout<<"Case #"<<caseID<<": "<<2<<endl;
		}
		else if (Ac==1 && Aj==1){
			cout<<"Case #"<<caseID<<": "<<2<<endl;
		}
	}

}