#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
 int t;
 double i,j,tim,max,d,n,res;
 float m;
 cin>>t;
 for(int l=0;l<t;l++)
 {
	 cin>>d>>n;
	 max=0;
	 for(i=0;i<n;i++)
	 {
		 cin>>j>>m;
	     tim=(d-j)/m;
	     if(tim>max)
	      max=tim;
	 }
	res=d/max;
	cout<<endl;
	cout<<fixed;
	cout<<setprecision(6);
	 cout<<"Case #"<<(int)(l+1)<<": "<<res; 
 }
 return 0;
}
