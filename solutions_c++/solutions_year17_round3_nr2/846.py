#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main(){
	int casei,ttt,ans,ac,aj,i,x,y,tot;
	int c[110],d[110],j[110],k[110];
	ifstream in("PP.in");
	ofstream out("PP.out");
	in>>ttt;
	for (casei=1;casei<=ttt;casei++){
		in>>ac;
		in>>aj;
		for (i=1;i<=ac;i++) {
			in>>c[i];
			in>>d[i];
		}
		for (i=1;i<=aj;i++) {
			in>>j[i];
			in>>k[i];
		}
		if (ac+aj==1){
			out<<"Case #"<<casei<<": "<<2<<endl;
			continue;
		}
		if (ac==2){
			if (c[2]>c[1]){
				x=c[2]-d[1];
				y=1440-d[2]+c[1];
			} else {
				x=c[1]-d[2];
				y=1440-d[1]+c[2];
			}
			tot=d[2]-c[2]+d[1]-c[1];
			//cout<<"tot="<<tot<<endl;
			//cout<<"x="<<x<<endl;
			//cout<<"y="<<y<<endl;
			if (x+tot<=720 || y+tot<=720){
				out<<"Case #"<<casei<<": "<<2<<endl;
				continue;
			} else {
				out<<"Case #"<<casei<<": "<<4<<endl;
				continue;
			}
		}
		if (aj==2){
			if (j[2]>j[1]){
				x=j[2]-k[1];
				y=1440-k[2]+j[1];
			} else {
				x=j[1]-k[2];
				y=1440-k[1]+j[2];
			}
			tot=k[2]-j[2]+k[1]-j[1];
			//cout<<"tot="<<tot<<endl;
			//cout<<"x="<<x<<endl;
			//cout<<"y="<<y<<endl;
			if (x+tot<=720 || y+tot<=720){
				out<<"Case #"<<casei<<": "<<2<<endl;
				continue;
			} else {
				out<<"Case #"<<casei<<": "<<4<<endl;
				continue;
			}
		}
		
		out<<"Case #"<<casei<<": "<<2<<endl;
	}
}
