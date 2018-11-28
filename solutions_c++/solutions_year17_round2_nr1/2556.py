#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
int main(){
	int ttt;
	ifstream in("CC.in");
	ofstream out("CC.out");
	in>>ttt;
	int casei,n,i;
	double max, temp, d;
	double k[1010],s[1010],a[1010];
	double ans;
	for (casei=1;casei<=ttt;casei++){
		in>>d;
		in>>n;
		for (i=0;i<n;i++){
			in>>k[i];
			in>>s[i];
		}
		max=0;
		for (i=0;i<n;i++){
			temp=(d-k[i])/s[i];
			if (temp>max){
				max=temp;
			}
		}
		ans=d/max;
		out<<"Case #"<<casei<<": "<<fixed<<setprecision(6)<<ans<<endl;
	}
} 
