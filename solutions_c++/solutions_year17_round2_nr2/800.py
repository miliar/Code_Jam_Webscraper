#include <iostream>
using namespace std;
typedef long long ll;

ll T, N, R, R1, O, Y, Y1, G, B, B1, V, last;

// R - (O) - Y - (G) - B - (V)

bool impossibleCont(){
	if(R1<0||Y1<0||B1<0)return true;
	if(R1+B1<Y1-1)return true;
	if(Y1+B1<R1-1)return true;
	if(R1+Y1<B1-1)return true;
	return false;
}

bool impossibleTest(){
	if(R1<0||Y1<0||B1<0)return true;
	if(R1==0&&Y+B+O+V>0&&G>0)return true;
	if(B1==0&&R+Y+G+V>0&&O>0)return true;
	if(Y1==0&&B+R+O+G>0&&V>0)return true;
	if(R1+B1<Y1)return true;
	if(Y1+B1<R1)return true;
	if(R1+Y1<B1)return true;
	return false;
}

string SpecialCase(){
	string ans;
	if(Y!=0){
		for(int i=0; i<N; i+=2){
			ans+="YV";
		}
	}
	if(R!=0){
		for(int i=0; i<N; i+=2){
			ans+="RG";
		}
	}
	if(B!=0){
		for(int i=0; i<N; i+=2){
			ans+="BO";
		}
	}
	return ans;
}

string Process_horses(){
	R1=R-G;
	Y1=Y-V;
	B1=B-O;
	if(impossibleTest())return "IMPOSSIBLE";
	string ans;
	last=0;
	if(R1==0 && Y1==0 && B1==0) return SpecialCase();
	while(N--){
		R1--;
		if(!impossibleCont() && last!=1){
			last = 1;
			ans+="R";
			if(G<=0)continue;
			while(G--){
				ans+="G";
				N--;
				if(N==0)break;
				ans+="R";
				N--;
			}
			continue;
		}
		R1++;
		Y1--;
		if(!impossibleCont() && last!=2){
			last = 2;
			ans+="Y";
			if(V<=0)continue;
			while(V--){
				ans+="V";
				N--;
				if(N==0)break;
				ans+="Y";
				N--;
			}
			continue;
		}
		Y1++;
		B1--;
		if(!impossibleCont() && last!=3){
			last = 3;
			ans+="B";
			if(O<=0)continue;
			while(O--){
				ans+="O";
				N--;
				if(N==0)continue;
				ans+="B";
				N--;
			}
			continue;
		}
		B1++;
	}
	return ans;
}

int main(){
	cin>>T;
	for(int i=1; i<=T; i++){
		cin>>N>>R>>O>>Y>>G>>B>>V;
		
		cout<<"Case #"<<i<<": "<<Process_horses()<<endl;
	}
}