#include <iostream>
#include <vector>

using namespace std;

int getLastDigit(int num){
	return num%10;
}

bool isTidy(int num){
	while(num!=0){
		int lastDigit=getLastDigit(num);
		if(lastDigit==0){return false;}
		num=num/10;
		int secondLastDigit=getLastDigit(num);
		if(secondLastDigit>lastDigit){return false;}
		
		
	}

return true;
}



int main(){
	freopen("B-small-attempt1.in","r",stdin);
        freopen("output3.out","w",stdout);
	
	int testCase;
	cin >> testCase;
	for(int i=0;i<testCase;i++){
		int n;
		cin >> n;
		int maxTidyNum;
		for(int j=1;j<=n;j++){
			if(isTidy(j)){
				maxTidyNum=j;
				
			}
			
		}
		cout << "Case #" << i+1 << ": " << maxTidyNum <<endl;
	}

}

