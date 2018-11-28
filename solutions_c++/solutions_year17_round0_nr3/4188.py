#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
typedef vector<ll> vi;

ll T, N, K, ans1, ans2;
// gap1, gap2, num1, num2; // always gap1-1==gap2
vi newGapData, oldGapData;

void printdata(){
	cerr<<oldGapData[0]<<" "<<oldGapData[1]<<" "<<oldGapData[2]<<" "<<oldGapData[3]<<" with K="<<K<<endl;
}

void find_room(){
	//cerr<<"Looking for N:" << N << " and K:" << K << endl;
	newGapData.assign(4, N);
	newGapData[1]=N-1;
	newGapData[2]=1;
	newGapData[3]=0;
	while(true){
		oldGapData.assign(newGapData.begin(), newGapData.end());
		//printdata();
		if(K<=oldGapData[2]){
			ans2=(oldGapData[0]-1)/2;
			ans1=oldGapData[0]-ans2-1;
			return;
		}
		K-=oldGapData[2];
		if(K<=oldGapData[3]){
			ans2=(oldGapData[1]-1)/2;
			ans1=oldGapData[1]-ans2-1;
			return;
		}
		K-=oldGapData[3];
		
		if(oldGapData[0]%2==0){
			newGapData[0]=oldGapData[0]/2;
			newGapData[1]=oldGapData[1]/2;
			newGapData[2]=oldGapData[2];
			newGapData[3]=oldGapData[2]+2*oldGapData[3];
		} else {
			newGapData[0]=oldGapData[0]/2;
			newGapData[1]=oldGapData[1]/2 -1;
			newGapData[2]=2*oldGapData[2]+oldGapData[3];
			newGapData[3]=oldGapData[3];
		}
	}
}

int main(){
	cin>>T;
	for(int i=1; i<=T; i++){
		cin>>N>>K;
		find_room();
		cout << "Case #" << i << ": " << ans1 << " " << ans2 << endl;
	}
}