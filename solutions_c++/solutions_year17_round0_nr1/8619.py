#include<iostream>

using namespace std;
int main(){
	int testcase,t;
	string cakes;
	int flipper;
	int status[1002];
	memset(status,0,1002);
	cin>>testcase;
	t = testcase;
	while(testcase--){       
		cin>>cakes;
		cin>>flipper;
		int currentflip = 0;
		int total = 0;
		for(int i = 0; i <= cakes.size()-flipper;i++){
			if(i-flipper>=0){
				currentflip-=status[i-flipper];
			}
			if(currentflip%2 && cakes[i] == '+' || currentflip%2==0 && cakes[i]=='-'){ 
				currentflip++;
				status[i] = 1;
				total++;
			}
			else {
				status[i] = 0;
			}
			//cout<<currentflip<<endl;
		}
		for(int i = cakes.size()-flipper+1; i<cakes.size();i++){
            if(i-flipper>=0){
				currentflip-=status[i-flipper];
			}
			if(currentflip%2 && cakes[i] == '+' || currentflip%2==0 && cakes[i]=='-')currentflip = -1;
			//cout<<currentflip<<endl;
		}
		if(currentflip <= -1)cout<<"Case #"<<t-testcase<<": IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<t-testcase<<": "<<total<<endl;

	}

	return 0;

} 