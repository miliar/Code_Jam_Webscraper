#include<bits/stdc++.h>
using namespace std;

const double inf = 10000000000009;
double D, S, t, n;
double k[1005], s[1005];

int main(){
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
	
	cout<<setprecision(7)<<fixed;
	cin>>t;
	for(int tt=1; tt<=t; tt++){
		cin>>D>>n;
		
		for(int i=0; i<n; i++){
			cin>>k[i]>>s[i];
		}
		
		S=inf;
		for(int i=0; i<n; i++){
			if(s[i]<S){
				S = min(S, (s[i]*D)/(D-k[i]));
			}
		}
		
		cout<<"Case #"<<tt<<": "<<S<<"\n";
	}
	
}

