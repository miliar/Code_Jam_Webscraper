#include<bits/stdc++.h>
using namespace std;
char func(char x){
	if(x!=0){
		x--;
	}

	//itoa(b,a,10);
	return x;
}
int main(){
	int t,k;
	//char s[1005];
	long long a, n,ans,w;
	char s[200];
	cin>>t;
	int x=0;
	int man=0;
	while(t--){
		man++;
		cin>>n;

		a=n;
		lltoa(a,s,10);
		//cout<<s<<endl;
		int l=strlen(s);
		//cout<<s<<" ";
		if(l==1){
			ans=n;
		}
		else{
			int f;
			for(int j=0;j<l;j++){

				for(int i=0;i<l-1;i++){


					if(s[i+1]<s[i]){
						char h=func(s[i]);

						s[i]=h;

						f=i;
						for(int z=f+1;z<l;z++){
				//cout<<'a';
								s[z]='9';
						}
						//cout<<s<<endl;
						break;
					}

				}
			}
			//cout<<f<<" ";
			w=atoll(s);

			ans=w;
		}
		cout<<"Case #"<<man<<": "<<ans<<endl;
	}


}
