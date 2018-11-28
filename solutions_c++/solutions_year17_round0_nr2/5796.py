#include <bits/stdc++.h>
using namespace std;

int T;

long long len;

int number[1000];

bool result;

long long nowans;

void getans(int place,int sam,int las){
	if (result) return;
	if (place==0) {
		cout<<nowans<<endl;
		result=1;
		return;
	}
	for(int i=9;i>=las;i--) {
		if (sam && number[place]<i) continue;
		nowans=nowans * 10+i;
		if (sam && number[place]==i) getans(place-1,1,i);
		else getans(place-1,0,i);
		nowans =nowans / 10;
	}
}

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>T;
	for(int t=1;t<=T;t++) {
		result=0;
		cin>>len;
		for(int i=1;i<=20;i++) {
			number[i]=len % 10;
			len=len / 10;
		}
		cout<<"Case #"<<t<<": ";
		getans(20,1,0);
	}
	return 0;
}
