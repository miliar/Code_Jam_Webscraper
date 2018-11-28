#include<iostream>
#include <fstream>
using namespace std;
int main(){

	int testcase, t;
	cin>>t;
	testcase = t;
	int number;
	//char changed[100];
	char result[100];
	//memset(changed,0,sizeof(changed));
	while(t--){
		cout<<"Case #"<<testcase-t<<": ";
		memset(result,0,sizeof(result));	
		cin>>result;
		//itoa(number,result,10);
		int s = strlen(result);
		int i = s-1;
		int position = 100;
		for(;i>0;i--){
			if(result[i-1]>result[i]){
				position = i;	
                			
			   result[i-1] = result[i-1]-1;
			}
		}
		for(i = position;i<s;i++){
			result[i] = 57;
		}
		char*end;
		//cout<<"r"<<result<<endl;
		if(result[0]!='0')
  cout<<result[0];
		for(int i = 1;i<s;i++)cout<<result[i];
		cout<<endl;

		
		
	}
	
	
	
	
	return 0;

} 