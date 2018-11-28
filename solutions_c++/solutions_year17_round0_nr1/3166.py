#include<bits/stdc++.h>
#define mp make_pair
#define fs first
#define sc second
#define pb push_back
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("haha.txt","w",stdout);
	int t; cin>>t;
	for(int tmp=0;tmp<t;tmp++){
		string baca; int k; 
		cin>>baca>>k;
		int cnt = 0;
		for(int i=0;i<=baca.length()-k;i++){
			if(baca[i] == '-'){
				cnt++;
				for(int j=i;j<i+k;j++){
					if(baca[j] == '-'){
						baca[j] = '+';
					}else if(baca[j] == '+'){
						baca[j] = '-';
					}
				}
			}
		}
		bool bisa = true;
		for(int i=0;i<baca.length();i++){
			if(baca[i] == '-'){
				bisa = false;
				break;
			}
		}
		if(bisa) printf("Case #%d: %d\n",tmp+1,cnt);
		else printf("Case #%d: IMPOSSIBLE\n",tmp+1);
	}
}

