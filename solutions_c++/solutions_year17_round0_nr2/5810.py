#include <bits/stdc++.h>
#define lint unsigned long long int
using namespace std;

lint count(lint b){
	lint d=0;
	while(b>0){
		b/=10;
		d++;
	}
	return d;
}

vector<lint> chk(vector<lint> a){
    for(lint j=1;j<a.size();j++){
			if(a[j]<a[j-1]){
				a[j-1]--;
				for(lint h=j;h<a.size();h++){				
                    a[h]=9;
	            }
                a=chk(a);
				break;
			}
	}
    return a;
}
int main(){
	lint t;
	cin>>t;
	for(lint i=0;i<t;i++){
		vector <lint> a;
		lint b;
		cin>>b;
		lint k=count(b);
		while(b>0){
            lint t=b%10;
			a.push_back(t);
			b/=10;
		}
		reverse(a.begin(),a.end());
        a=chk(a);
        for(lint j=0;j<a.size();j++){
			if(a[j]==0){
                continue;
            }
            cout<<a[j];
		}
        cout<<endl;
	}
	return 0;
}
