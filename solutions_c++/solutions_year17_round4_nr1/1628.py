#include<bits/stdc++.h>
using namespace std;
int test;
int II()
{
int n;
scanf("%d",&n);
return n;
}
int main(){
	ifstream cin("A-small-attempt0 (2).in");
	ofstream cout("A-small-attempt0 (2).out");
cin>>test;
int cont=1;
while(test--){
	int n,p;
	cin>>n>>p;
	double freq[p];
	for(int i=0;i<p;i++)
	freq[i]=0;
	int a;
	for(int i=0;i<n;i++){
		cin>>a;
		//cout<<a%p<<endl;
		freq[a%p]++;
	}
	cout<<"Case #"<<cont<<": ";
	switch(p){
		case 2:
			//cout<<freq[1]<<" "<<freq[0]<<" ytf";
			cout<<freq[0]+ceil(freq[1]/2)<<endl;
			break;
		case 3:
			if(freq[1]>freq[2])
			cout<<freq[0]+freq[2]+ceil((freq[1]-freq[2])/3)<<endl;
			else{
				if(freq[1]<freq[2])
				cout<<freq[0]+freq[1]+ceil((freq[2]-freq[1])/3)<<endl;
				else
				cout<<freq[0]+freq[1]<<endl;
			}
			break;
		case 4:
			int ans=0;
		while(freq[1]&&freq[3]){
			ans++;
			freq[1]--;
			freq[3]--;
		}
		while(freq[2]>1){
			ans++;
			freq[2]-=2;
		}
		if(freq[2]&&freq[1]>1){
			freq[2]--;
			freq[1]-=2;
			ans++;
		}
		if(freq[2]&&freq[3]>1){
			freq[2]--;
			freq[3]-=2;
			ans++;
		}
		while(freq[3]>4){
		freq[3]-=4;
		ans++;	
		}		
		while(freq[1]>4){
		freq[1]-=4;
		ans++;	
		}
		cout<<freq[0]+ans<<endl;
	}
	cont++;
}
return 0;
}

