#include <bits/stdc++.h>
using namespace std;

int main(){
    int T,I;
    cin>>T;
    for(I=0;I<T;I++){
    	int input;
    	cin>>input;

    	int answer;
    	for(answer=input;answer>0;answer--){
			///////////////////////////
		    int i,length,remainder,quotient;
			for(i=0;;i++){
				if(answer/pow(10,i)==0){
					break;
				}
			}
			length=i;
			int testCase[length];
			for(i=0;i<length;i++){
				remainder=answer%static_cast<int>(pow(10,i+1));
				quotient=remainder/static_cast<int>(pow(10,i));
				testCase[length-1-i]=quotient;
			}
			///////////////////////////
			bool result=true;
    		int tester=testCase[0];
    		for(i=0;i<length;i++){
    			if(testCase[i]<tester){
    				result=false;
    				break;
    			}else{
    				tester=testCase[i];
    			}
    		}
    		if(result==true){
    			break;
    		}
    	}
    	cout<<"Case #"<<I+1<<": "<<answer<<endl;
    }
    return 0;
}
