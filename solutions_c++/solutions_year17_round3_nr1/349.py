#include<bits/stdc++.h>
using namespace std;
int n,k;
int test;
int II()
{
int n;
scanf("%d",&n);
return n;
}
int main(){
	ifstream cin("A-large (1).in");
	ofstream cout("A-large (1).out");
cin>>test;
int cont2=1;
while(test--){
	double pi = 3.1415926535897;
	cin>>n>>k;
	pair<double,double> pan[n];
	for(int i=0;i<n;i++)
	cin>>pan[i].first>>pan[i].second;
	
	sort(pan,pan+n);
	double ans=0;
	for(int i=n-1;i>=0;i--){
		double temp=pan[i].first*double(2)*pi*pan[i].second+pan[i].first*pan[i].first*pi;
	//	cout<<"temp= "<<pan[i].first<<" "<<temp<<endl;
		vector<double> height;
		for(int j=i-1;j>=0;j--){
			height.push_back(pan[j].first*double(2)*pi*pan[j].second);
		}
		sort(height.begin(),height.end());
		int cont=0;
		for(int j=height.size()-1;j>=0&&cont<k-1;j--){
	//		cout<<"agigungo "<<height[j]<<endl;
			temp+=height[j];
			cont++;
		}
		//cout<<"w"<<temp<<endl;
		ans=max(ans,temp);
	}
	cout<<"Case #"<<cont2<<": "<<setprecision(19)<<ans<<endl;
	cont2++;
	
}
return 0;
}

