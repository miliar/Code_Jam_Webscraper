#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int main(){
	long int t,i,j;
	ifstream myfile("v.txt");
ofstream outFile("output.txt");
    long long int v;
    myfile >> v;
    t=v;
  // cout<<t<<"  ";
	long long int b[t],x,n;
	i=0;
	 while (myfile >> v)
    {
       b[i]=v;
      // cout<<v<<endl;
       i++;
    }	
	
	for(j=0;j<t;j++){
		
		x=0;
		n=b[j];
		vector<long long int> a;
	while(n!=0)	{
		a.push_back(n%10);
		n=n/10;
		
	}
	
	for(i=0;i<a.size()/2;i++) {
		int temp=a[a.size()-1-i];
		a[a.size()-1-i]=a[i];
		a[i]=temp;
	}
	
	i=0;
	
	while(i<a.size()-1){
		if(a[i]>a[i+1]){
			
			while(i>0&&a[i]==a[i-1]) {
				i--;
			}
			a[i]--;
			
			break;
		}
		i++;
	}
	i++;
	while(i<a.size()){
		a[i]=9;
		i++;
	}
i=0;
	while(a.size()>0){
		x=10*x+a[i];
	a.pop_back();
	i++;	
	}
	
	outFile <<"Case #"<<j+1<<": "<< x <<endl;
	}
	return 0;
}
