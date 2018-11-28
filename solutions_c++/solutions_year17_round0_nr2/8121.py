#include<iostream>
#include<fstream>
using namespace std;
int main(){
	ofstream myfile;
  	myfile.open ("output.txt");
	int t,a[19],i,j,k,l,x,y;
	long long int n,o[100];
	cin>>t;
	for(k=0;k<t;k++){
		cin>>n;
		l=0;
		while(n!=0){
			a[l]=(n%10);
			n=(n/10);
			l++;
		}
		i=l-1;
		j=i-1;
		while(i!=0){
			if(a[i]>a[j]){
				a[i]=a[i]-1;
				x=i-1;
				while(x!=0){
					a[x]=9;
					x=x-1;
				}
				a[0]=9;
			}
			else if(a[i]==a[j]){
				if(j==0){
					break;
				}
				j=j-1;
			}
			else if(a[i]<a[j]){
				i=j;
				if(j==0){
					break;
				}
				j=j-1;
			}
		}
		
		if(a[l-1]==0){
			l=l-1;
		}
		o[k]=a[l-1];
		for(y=l-2;y>=0;y--){
			o[k]=(o[k]*10)+a[y];
		}
	}
	for(k=0;k<t;k++){
		cout<<"Case #"<<k+1<<": "<<o[k]<<endl;
	  	myfile <<"Case #"<<k+1<<": "<<o[k]<<endl;
	}
	 myfile.close();
}
