#include <iostream>

using namespace std;

int t;
int j;
string n;

void zmien(int a){
	n[a] = (char)((int)n[a]-1);
	for(int i=a+1; i<(int)n.size() && n[i]!='9'; i++)
		n[i] = '9';
}

int main(){
	cin>>t;
	for(int i=0; i<t; i++){
		cin>>n;
		for(j=n.size()-1; j>=0; j--){
			if((int)n[j-1] > (int)n[j]){
				zmien(j-1);
			}
		}
		j = 0;
		while(n[j] == '0')j++;
		cout<<"Case #"<<i+1<<": ";
		for(; j<(int)n.size(); j++)
			cout<<n[j];
		cout<<"\n";
		j = 0;
	}
	
	return 0;
}
