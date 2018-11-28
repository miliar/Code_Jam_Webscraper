#include<iostream>
#include<string>
using namespace std;
int main(){	
	int testCases;
	cin>>testCases;
	int c=0;
	while(testCases--){
		string refString;
		int count=0;
		int window;
		cin>>refString;
		cin>>window;
		for(int i=0;refString[i+window]!='\0';i++){
			if(refString[i]=='-'){
				for(int j=0;j<window;j++){
					if(refString[j+i]=='-')
						refString[j+i]='+';
					else
						refString[j+i]='-';
				}
				count++;
			}
		}
				
		c++;	
		int negatives=0;
		cout<<"Case #"<<c<<": ";
		for(int i=0;refString[i]!='\0';i++)
			if(refString[i]=='-')
				negatives++;
		if(negatives==0)
			cout<<count;
		else if(negatives==window)
			cout<<count+1;
		else
			cout<<"IMPOSSIBLE";
		cout<<endl;
	}
	return 0;
}
