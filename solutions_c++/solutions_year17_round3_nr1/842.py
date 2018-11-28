#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main(){
	int casei,ttt,ans,i,n,k,j,l;
	ifstream in("AS.in");
	ofstream out("AS.out");
	in>>ttt;
	double a[1010],around[1010],r,h,maxa,temp,max;
	double** opt=new double*[1010]; 
	double pi=3.141592653589793238462643383279502884197169399375105820974944592307;
	for (i=0;i<1010;i++){
		opt[i]=new double[1010];
	}
	for (casei=1;casei<=ttt;casei++){
		in>>n;
		in>>k;
		maxa=0;
		for (i=1;i<=n;i++){
			in>>r;
			in>>h;
			a[i]=r*r*pi;
			around[i]=2*pi*r*h;
			if (a[i]>maxa){
				maxa=a[i];
			}
		}
		for (i=1;i<=n;i++){
			for (j=i+1;j<=n;j++){
				if (a[i]<a[j]){
					temp=a[i];
					a[i]=a[j];
					a[j]=temp;
					temp=around[i];
					around[i]=around[j];
					around[j]=temp;
				}
			}
		}
		/*opt[1]=around[1];
		for (i=2;i<=n;i++){
			max=0;
			for (j=1;j<i;j++){
				if (opt[j]>max){
					max=opt[j];
				}
			}
			opt[i]=max+around[i];
		}
		max=0;
		for (i=1;i<=n;i++){
			if (opt[i]>max) max=opt[i]
		}*/
		for (i=1;i<=n;i++){
			opt[i][1]=around[i]+a[i];
		}
		for (i=2;i<=k;i++){
			for (j=i;j<=n;j++){
				max=0;
				for (l=1;l<j;l++){
					if (opt[l][i-1]>max){
						max=opt[l][i-1];
					}
				}
				max=max+around[j];
				opt[j][i]=max;
			}
		}
		max=0;
		for (i=1;i<=n;i++){
			if (max<opt[i][k]){
				max=opt[i][k];
			}
		}
		//max=max+maxa;
		out<<"Case #"<<casei<<": "<<fixed<<setprecision(9)<<max<<endl;
		/*
		for (i=1;i<=n;i++){
			cout<<a[i]<<" ";
		}
		cout<<endl;
		for (i=1;i<=n;i++){
			cout<<around[i]<<" ";
		}
		cout<<endl;
		for (i=1;i<=k;i++){
			for (j=1;j<=n;j++){
				cout<<opt[j][i]<<" ";
			}
			cout<<endl;
		}
		*/
	}
}
