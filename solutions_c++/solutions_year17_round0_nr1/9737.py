#include<iostream>
#include<cstdlib>
#include<climits>
using namespace std;
void bubbleSort(int* array,int size){
	for(int i=0;i<size;i++){
		for(int j=(size-1);j>i;j--){
			if(array[j-1] >  array[j]){
				int temp = array[j];
				array[j]=array[j-1];
				array[j-1]=temp;
			}
		}
	}
};
int flipCount(string s,int index,int k){
	//cout<<s<<" "<<index<<" "<<k<<"\n";
	bool tidy = true;
	for(int i=0;i<s.length();i++){
		if(s[i] != '+'){
			tidy = false;
			break;
		}
	}

	//cout<<s.length()<<" "<<index<<" "<<tidy<<"\n";
	if(tidy){
		return 0;
	}else{
		if(s.length() < index+k){
			return INT_MAX;
		}else{
			unsigned int x,y;
			x=0+flipCount(s,index+1,k);
			for(int i=index;i<(index+k);i++){
				if(s[i]=='+')
					s[i]='-';
				else if(s[i] == '-')
					s[i]='+';
			}
			y=1+flipCount(s,index+1,k);
			//cout<<x<<" "<<y<<"\n";
			return min(x,y);
		}
	}
};
int main(){
	int T,K;
	string s;
	cin>>T;
	int i=0;
	while(T-- >0){
		cin>>s;
		cin>>K;
		i++;
		unsigned int value = flipCount(s,0,K);

		if(value == INT_MAX)
			cout<<"Case #"<<i<<": IMPOSSIBLE"<<"\n";
		else 
			cout<<"Case #"<<i<<": "<<value<<"\n";
	}
}