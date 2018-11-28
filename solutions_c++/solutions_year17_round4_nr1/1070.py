#include <iostream>
#include <iomanip>
#include <cstdlib>
using namespace std;

int N, P;

int G[200];

int modular[5];
int onecase()
{
 	cin>>N>>P;

 	for(int i=0;i<N;i++)
 		cin>>G[i];

 	for(int i=0;i<N;i++)
 		G[i]%=P;
 	for(int i=0;i<P;i++)
 		modular[i]=0;
 	for(int i=0;i<N;i++)
 		modular[G[i]]++;

 	int ans=0;
 	if(P==2){
 		ans+=modular[0];
 		int rem=modular[1];
 		ans+=(rem+1)/2;
 	}else if(P==3){
 		ans+=modular[0];
 		int ra=modular[1];
 		int rb=modular[2];
 		int smaller=ra<rb?ra:rb;
 		ra-=smaller;rb-=smaller;
 		ans+=smaller;
 		int remain=ra+rb;
 		ans+=(remain+2)/3;
 		// 1, 2:
 		// aaabbbb: ab ab ab b
 		// ab ab ab... a: 1 aa: 1 aaa: 1 aaaa:2
 	}else if(P==4){
 		ans+=modular[0];
 		// a 2 b: ab ab ab 22 22 |2aaa
 		int r2=modular[2];
 		int ra=modular[1];
 		int rb=modular[3];

 		int smaller=ra<rb?ra:rb;
 		ra-=smaller;rb-=smaller;
 		ans+=smaller;

 		while(r2>=2){
 			r2-=2;ans+=1;
 		}
 		int remain=ra+rb;
 		while(remain>=4){
 			remain-=4;ans+=1;
 		}
 		if(remain+r2>=1)ans+=1;
 	}
 	//2:0,1.  
 	//3:0,1,2
 	cout<<ans<<endl;

	return 0;
}

int main(){
	//onecase();return 0;

	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		onecase();
	}
	return 0;
}