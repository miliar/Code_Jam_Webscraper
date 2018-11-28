#include<bits/stdc++.h>
#define mp make_pair
#define fs first
#define sc second
#define pb push_back
using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("haha.txt","w",stdout);
	int t;
	cin>>t;
	for(int tmp=0;tmp<t;tmp++){
		printf("Case #%d: ",tmp+1);
		string baca; cin>>baca;
		int cnt = 0,ambil = 1000;
		for(int i=0;i<baca.length()-1;i++){
			if(baca[i] > baca[i+1]){
				ambil = i - cnt;
				break;
			}else if(baca[i] == baca[i+1]){
				cnt++;
			}else if(baca[i] < baca[i+1]){
				cnt = 0;
			}
		}
		if(ambil==1000){
			cout<<baca<<"\n";
		}else{
			for(int i=0;i<ambil;i++){
				cout<<baca[i];
			}
			baca[ambil]--;
			if(ambil != 0 || baca[ambil] != '0') cout<<baca[ambil];
			for(int i=ambil+1;i<baca.length();i++){
				cout<<"9";
			}  
			cout<<"\n";
		}
	}
}

