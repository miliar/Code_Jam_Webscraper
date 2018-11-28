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
ifstream cin("B-small-attempt3.in");
	ofstream cout("B-small-attempt3.out");
cin>>test;
int cont=1;
while(test--){
	int n,m,c;
	cin>>n>>c>>m;
	vector<int> seatuno,seatdue;
	
	int us[1000];
	bool us2[1000];
	for(int i=0;i<m;i++){
		us[i]=-1;
		us2[i]=false;
		int a,b;
		cin>>a>>b;
		if(b==1)
		seatuno.push_back(a);
		else
		seatdue.push_back(a);
	}
	int temp=seatuno.size(),temp2=seatdue.size();
	int ans=0;
	bool fine=true;
	while(fine){
		fine=false;
	for(int i=0;i<seatuno.size();i++){
		//cout<<"Controllo seatuno "<<seatuno[i]<<endl;
		if(us[i]==-1){
		bool ok=false;
		for(int j=0;j<seatdue.size();j++){
			if(us2[j]==false&&seatdue[j]!=seatuno[i]){
				temp--;
				temp2--;
				ans++;
				us2[j]=true;
				us[i]=j;
				fine=true;
				ok=true;
			//	cout<<"abbino "<<seatuno[i]<<" "<<seatdue[j]<<endl;
				break;
			}
		}
		if(!ok){
			for(int j=0;j<seatuno.size();j++){
				if(us[j]!=-1&&seatdue[us[j]]!=seatuno[i]){
				//cout<<"riabbino "<<seatuno[i]<<" "<<seatdue[us[j]]<<endl;
					us[j]=us[i];
					us[i]=-1;
					fine=true;
					break;
				}
			}
		}
		}
	}
	}
	//cout<<ans<<endl;
	bool uno=false;
	for(int i=0;i<seatuno.size();i++){
		if(us[i]==-1&&seatuno[i]==1)
		uno=true;
	}
	if(uno){
		cout<<"Case #"<<cont<<": "<<ans+temp+temp2<<" "<<0<<endl;
	}
	else
		cout<<"Case #"<<cont<<": "<<ans+max(temp,temp2)<<" "<<min(temp,temp2)<<endl;
	cont++;
}
return 0;
}

