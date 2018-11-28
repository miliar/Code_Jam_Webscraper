#include<bits/stdc++.h>
using namespace std;
int main(){
	int size,k;
	string pan;
	cin>>size;
	for(int t=0;t<size;t++){
		int count=0;
		cin>>pan>>k;
		for(int i=0;i<pan.size();i++){
			if((pan.size()-i)==k){
				for(int j=i;j<pan.size();j++){
					if(pan[j]!=pan[i]){
						count=-1;
						break;
					}
				}
				if(pan[i]=='-' && count!=-1)
					count++;
				break;	
			}
			else if(pan[i]=='-'){
				count++;
				for(int j=i;j<i+k;j++){
					if(pan[j]=='+')
						pan[j]='-';
					else
						pan[j]='+';
				}
			}
		}
		if(count==-1)
			cout<<"Case #"<<(t+1)<<": IMPOSSIBLE\n";
		else
			cout<<"Case #"<<(t+1)<<": "<<count<<"\n";
	}
return 0;
}
