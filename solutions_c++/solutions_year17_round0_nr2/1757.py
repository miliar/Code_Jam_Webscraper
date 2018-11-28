#include <iostream>
#include <cstring>
typedef unsigned long long LL;
using namespace std;
int sol();
string n;
int main()
{
int t,T;

cin>> T;
t=T;
while(T--)
{
  	cin>>n;
  	cout <<"Case #"<<t-T<<": ";
	sol();
	if(T>=1) cout<<endl;
	



}






}



int sol()
{
	
	if(n.length()==1) {cout <<n; return 0;}
	
	unsigned int i=0;
	while(i<n.length()-1 && n[i]<=n[i+1]) i++;

	if(i==n.length()-1) {
	for(int k=(n[0]=='0');k<n.length();k++)
	cout <<n[k];
	 return 0;}
	else {n[i]--;
	for(int j=i+1;j<n.length();j++) n[j]='9';
//cout <<n<<endl;
  sol();
    }
	
	
	
	
	
	
	
}
