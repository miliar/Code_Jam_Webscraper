#include <bits/stdc++.h>
using namespace std;
class initialStats{
	public:
		long starting;
		long speed;
};
int main(){
	int I,T;
	cin>>T;
	for(I=0;I<T;I++){
		int D,N,i,j;
		cin>>D>>N;
		initialStats input[N];
		for(i=0;i<N;i++){
			cin>>input[i].starting;
			cin>>input[i].speed;
		}
///////////////
		for(i=0;i<N;i++){
			for(j=N-1;j>i;j--){
				if(input[j].starting<input[j-1].starting){
					initialStats tmp=input[j];
					input[j]=input[j-1];
					input[j-1]=tmp;
				}
			}
		}
///////////////
		double test;
		double answer; 
		double time;
		int currentCase;
		currentCase=N-1;
		time=(static_cast<double>(D)-static_cast<double>(input[N-1].starting))/static_cast<double>(input[N-1].speed);
		for(i=N-2;i>=0;i--){
			test=static_cast<double>(input[currentCase].starting)-static_cast<double>(input[i].starting);
			if(input[i].speed==input[currentCase].speed){
				currentCase=i;
				time=(static_cast<double>(D)-static_cast<double>(input[currentCase].starting))/static_cast<double>(input[currentCase].speed);
				continue;
			}
			test=test/(static_cast<double>(input[i].speed)-static_cast<double>(input[currentCase].speed));
			if(test>time||test<0){
				currentCase=i;
				time=(static_cast<double>(D)-static_cast<double>(input[currentCase].starting))/static_cast<double>(input[currentCase].speed);
			}
		}
		answer=D/time;
		cout<<"Case #"<<I+1<<": ";
		printf("%f\n",answer);
		
	}
	return 0;
}