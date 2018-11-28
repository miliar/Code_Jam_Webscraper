#include <iostream>

using namespace std;

int T;
int Hd,Ad,Hk,Ak,B,D;

int main(){
	cin>>T;
	
	for(int cn=1;cn<=T;cn++){
		cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
		if((Ak-D>=Hd && Ad<Hk)){
			cout<<"Case #"<<cn<<": IMPOSSIBLE"<<'\n';
			continue;
		}
		//try d debuffs and b buffs
		
		int result=200;
		bool imp=false;
		
		for(int d=0;d<=(D==0?0:(Ak/D+1));d++){
			for(int b=0;b<=100;b++){
				imp=false;
				int count=0,countd=0,H=Hd,A1=Ad,A2=Ak;
				int lastcured=false;
				while(countd<d){
					if(H<=A2-D){//have to cure
						if(lastcured==true){
							imp=true;
							break;
						}else{
							lastcured=true;
							H=Hd-A2;
							count++;
						}	
					}else{
						lastcured=false;
						A2-=D;
						H=H-A2;
						countd++;
						count++;
					}
				}
				if(imp)
					continue;
				
				int countb=0;
				while(countb<b){
					if(H<=A2){//have to cure
						if(lastcured==true){
							imp=true;
							break;
						}else{
							lastcured=true;
							H=Hd-A2;
							count++;
						}	
					}else{
						lastcured=false;
						A1+=B;
						H=H-A2;
						countb++;
						count++;
					}
				
				}
				if(imp)
					continue;
				int H2=Hk;
				while(H2>0){
					if(H<=A2 && H2>A1){//have to cure
						if(lastcured==true){
							imp=true;
							break;
						}else{
							lastcured=true;
							H=Hd-A2;
							count++;
						}	
					}else{
						lastcured=false;
						H2-=A1;
						H=H-A2;
						count++;
					}				
				}
				if(imp)
					continue;
				if(count<result)
					result=count;
			}
		}
		
		cout<<"Case #"<<cn<<": ";
		if(result==200)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<result<<'\n';
	}
	
	return 0;
}