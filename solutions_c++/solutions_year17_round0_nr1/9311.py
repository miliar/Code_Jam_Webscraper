#include<iostream>
#include<fstream>
#include<string.h>
//#include<conio.h>
using namespace std;

int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("firstpanoutreallarge","w",stdout);
	int i,j,t,l,p,count;
	cin>>t;
	for(i=1;i<=t;i++){
		char a[1005];
		int k;
		count=0;
		cin>>a;
		cin>>k;
		l=strlen(a);
		p=0;
		for(j=0;j<l-k+1;j++){
		//	cout<<"loop "<<i<<endl;
			if(a[j]=='-'){
				count++;
				a[j]='+';
				for(p=j+1;p<j+k;p++){
					if(a[p]=='-') a[p]='+';
					else a[p]='-';
				}
			}
		}	
		for(j=l-k+1;j<l;j++){
			if(a[j]=='-'){
				p=-1;
				break;
			}
		}	
		if(p==-1)
		cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<"\n";
		else
		cout<<"Case #"<<i<<": "<<count<<"\n";
	}
	return 0;
//	getch();
}
