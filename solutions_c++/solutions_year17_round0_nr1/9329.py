#include<iostream>
using namespace std;
#include<string>
int main(){

	int x,y;
	string p;
	cin>>x;
	int moves,z,check;
	for(int i=1;i<=x;i++){

		cin>>p>>y;
		moves=0;
		z= p.length();
		check=1;
		int finalcount=0;
		for(int j=1;j<=z;j++){
		
			if(j>(z-y+1)){
			
				for(int k=0;k<y;k++){
					if(p[j-1+k]=='-'){
					check=0;
					break;
					}
				}
				

			}
	                else{
			if(p[j-1]=='-'){

				for(int k=0;k<y;k++){
					if(p[j-1+k]=='-'){p[j-1+k]='+'; }
					else { p[j-1+k]='-';  }
				}
				
				moves=moves+1;
				
			}
		}

		}
		for(int h=0 ;h<z;h++){
		if(p[h]=='+'){finalcount=finalcount+1;}
		}
		
		if(finalcount==z){check=1;}
		if(check==1){
		cout<<"Case #"<<i<<": "<<moves<<endl;
		}
		else{
		cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		}
	



	}

}
