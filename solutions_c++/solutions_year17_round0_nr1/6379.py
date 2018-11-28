#include<bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define rep(i,a,b) for(i=a;i<=b;i++)
#define rep2(i,a,b,c) for(i=a;i<=b;i+=c)

string str;

int main(){
	freopen("AAAin.txt","r",stdin);
	freopen("AAAout.txt","w",stdout);
	int n,k,has=0;
	int tes,i,j,cas=0;
	cin>>tes;
	while(tes--){
		cas++;
		has=0;
		cin>>str>>k;
		has=0;
		rep(i,0,(int)str.size()-1){
			if(i+k-1 > (int)str.size()-1){
				break;
			}
			if(str[i]=='-'){
				has++;
				rep(j,i,i+k-1){
					if(str[j]=='+'){
						str[j]='-';
					}
					else{
						str[j]='+';
					}
				}
			}
		}
		rep(i,0,(int)str.size()-1){
			if(str[i]=='-'){
				has=-1;
			}
		}
		if(has >= 0){
			cout<<"Case #"<<cas<<": "<<has<<"\n";
		}
		else{
			cout<<"Case #"<<cas<<": IMPOSSIBLE\n";
		}
	}
}

