#include<bits/stdc++.h>
#define mp make_pair
#define fs first
#define sc second
#define pb push_back
using namespace std;

pair<long long,long long> pecah(long long a){
	if(a%2==1){
		return mp(a/2,a/2);	
	}else{
		return mp(a/2,a/2-1);
	}
}


int main(){
	freopen("C-large.in","r",stdin);
	freopen("haha.txt","w",stdout);
	int t; cin>>t;
	for(int tmp=0;tmp<t;tmp++){
		printf("Case #%d: ",tmp+1);
		long long n,k; cin>>n>>k;
		pair<long long,long long> satu,dua;
		long long nyaka,nyakb;
		long long a,b;
		if(k==1){
			if(n%2==1){
				cout<<n/2<<" "<<n/2<<"\n";
			}else{
				cout<<n/2<<" "<<n/2-1<<"\n";
			}
		}else{
			if(n%2==1){
				a = n/2; b = a-1;
				satu = mp(a,a);
				dua = satu;
				nyaka = 1;
				nyakb = 0;
			}else{
				a = n/2; b = n/2-1;
				satu = mp(a,b);
				dua = satu;
				nyaka = 1;
				nyakb = 0;
			}
			long long besar = 2;
			for(long long i=2;i<70;i++){
				if(satu.fs == satu.sc){
					nyaka = 2*nyaka + nyakb;
				}else{
					nyakb = 2*nyakb + nyaka;
				}
				a = a/2; b = a-1;
				satu = pecah(satu.fs);
				dua = pecah(dua.sc);
				besar = besar*2;
				if(k < besar){
					k = k - besar/2 + 1;
					if(k <= nyaka){
						cout<<satu.fs<<" "<<satu.sc<<"\n";
					}else{
						cout<<dua.fs<<" "<<dua.sc<<"\n";
					}
					break;
				}
			}
		}
	}
}

