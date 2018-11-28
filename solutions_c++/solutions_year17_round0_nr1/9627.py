#include <bits/stdc++.h>
#include <iostream>
using namespace std;
char v[1123];
int main(){
	int n;
	cin>>n;
	int caso=1;

	for (int i=0;i<n;i++){
		cout<<"Case #"<<caso<<": ";
		string a;
		cin>>a;

		for (int j=0;j<a.size();j++){
			v[j]=a[j];
		}

		int of,counter=0,b=0;
		cin>>of;

		for (int j=0;j<a.size()-of+1;j++){

			if (v[j]=='-'){
				for (int k=0;k<of;k++){
					if (v[j+k]=='-'){
						v[j+k]='+';
					}
					else {
						v[j+k]='-';
					}
				}
				counter++;
			}
		}
		for (int j=0;j<a.size();j++){
			if (v[j]=='-'){
				b=1;
			}
		}
		if (b==1){
			cout<<"IMPOSSIBLE\n";
		}
		else {
			cout<<counter<<"\n";
		}
		caso++;

	}

	return 0;
}