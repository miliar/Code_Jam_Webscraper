#include<bits/stdc++.h>
#define ll long long
using namespace std;
fstream out("tidy.out",ios::out);
void check(ll n,int i){
	int dig=0,r,r1=9,f=0;
	ll numb=n,j;
	while(numb){
		r=numb%10;
		numb/=10;
		dig++;
		if(r>r1){
			f=1;
			break;
		}
		r1=r;
	}
	if(dig==1 || f==0)
		out<<"Case #"<<i<<": "<<n<<endl;
	else{
		f=0;
		for(j=n;j>=1;j--){
			numb=j;
			r1=9;
			while(numb){
				r=numb%10;
				numb/=10;
				//dig++;
				if(r>r1){
					f=1;
					break;
				}
				r1=r;
			}
			if(f==1){
				f=0;
			}
			else{
				break;
			}
		}
		out<<"Case #"<<i<<": "<<j<<endl;
	}
}
		
int main(){
	std::ios::sync_with_stdio(false);
	fstream in("B-small-attempt0.in", ios::in);
	fstream out("tidy.out",ios::out);
	int tc;
	in>>tc;
	for(int i=1;i<=tc;i++){
		ll n;
		in>>n;
		check(n,i);
	}
	return(0);
}
		
	
