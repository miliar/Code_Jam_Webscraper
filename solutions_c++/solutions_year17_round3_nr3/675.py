#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main(){
	int casei,ttt,i,j,l;
	ifstream in("CT.in");
	ofstream out("CT.out");
	in>>ttt;
	int n,k,x;
	double u,a[60],temp,remain,tot,ans;
	for (casei=1;casei<=ttt;casei++){
		in>>n;
		in>>k;
		x=n-k+1;
		in>>u;
		for (i=1;i<=n;i++){
			in>>a[i];
		}
		
		for (i=1;i<=n;i++){
			for (j=i+1;j<=n;j++){
				if (a[i]>a[j]){
					temp=a[i];
					a[i]=a[j];
					a[j]=temp;
				}
			}
		}
		
		tot=0;
		//remain=u;
		for (i=x+1;i<=n;i++){
			tot=tot+(a[i]-a[i-1])*(i-x);
			if (tot>u) {
				tot=tot-(a[i]-a[i-1])*(i-x);
				break;
			}
		}
		cout<<"l=";
		l=i-1;
		cout<<l<<endl;
		remain=a[i-1]+(u-tot)/(i-x);
		cout<<"remain="<<remain<<endl;
		for (i=x;i<=l;i++){
			a[i]=remain;
		}
		ans=1;
		for (i=x;i<=n;i++){
			ans=ans*a[i];
		}
		out<<"Case #"<<casei<<": "<<fixed<<setprecision(9)<<ans<<endl;
	}
}
