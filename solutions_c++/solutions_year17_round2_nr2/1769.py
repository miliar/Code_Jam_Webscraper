#include <iostream>
#include <string>
using namespace std;

int n,r,o,y,g,b,v;


int main() {
	// your code goes here
	
	int t;
	int i,j,k;
	cin>>t;
	int check;
	char temp1,temp2;
	
	for(i=1;i<=t;i++)
	{	check=1;
		cin>>n>>r>>o>>y>>g>>b>>v;
		char output[n+1];
		output[n]='\0';
		if(r>0) {output[0]='R'; r--;}
		else if(y>0) {output[0]='Y'; y--;}
		else if(b>0) {output[0]='B'; b--;}
		else if(g>0) {output[0]='G'; g--;}
		else if(o>0) {output[0]='O'; o--;}
		else if(v>0) {output[0]='V'; v--;}
		else {check=0;}
		
		for(j=1;j<n&&check==1;j++)
		{
			if(output[j-1]=='O') {if(b>0){output[j]='B';b--;} else check=0; }
			else if(output[j-1]=='G') {if(r>0){output[j]='R';r--;} else check=0; }
			else if(output[j-1]=='V') {if(y>0){output[j]='Y';y--;} else check=0; }
			
			else if(output[j-1]=='R') 
				{	if(g>0){output[j]='G';g--;}
					else if(y>=b&&y>=g) {if(y>0){output[j]='Y';y--;} else check=0;}
					else if(b>=g&&b>=y) {if(b>0){output[j]='B';b--;} else check=0;}
					
				}
			
			else if(output[j-1]=='Y')
				{	if(v>0){output[j]='V';v--;}
					else if(r>=b&&r>=v) {if(r>0){output[j]='R';r--;} else check=0;}
					else if(b>=v&&b>=r) {if(b>0){output[j]='B';b--;} else check=0;}
					
				}
			
			else if(output[j-1]=='B')
				{	if(o>0){output[j]='O';o--;}
					else if(r>=y&&r>=o) {if(r>0){output[j]='R';r--;} else check=0;}
					else if(y>=o&&y>=r) {if(y>0){output[j]='Y';y--;} else check=0;}
				}
			
		}
		temp1=output[0];
		temp2=output[n-1];
		
		if(n>1)
		{
			if(temp1=='R') if(temp2=='O'||temp2=='R'||temp2=='V') check=0; 
			else if(temp1=='B') if(temp2=='G'||temp2=='B'||temp2=='V') check=0;
			else if(temp1=='Y') if(temp2=='G'||temp2=='Y'||temp2=='O') check=0;
		}
		
		
		if(check==0) cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl; 
		else cout<<"Case #"<<i<<": "<<output<<endl;
	}
	
	return 0;
}
