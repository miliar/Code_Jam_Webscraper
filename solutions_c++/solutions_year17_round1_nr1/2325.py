#include<bits/stdc++.h>

using namespace std;

int main(){
	int t,x,k,i,j,l,m,r,c;
	string str[25];
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin>>t;
	for(int x=1;x<=t;x++){
		cin>>r>>c;
		bool b[26]={0};
		for(i=0;i<r;i++){
			cin>>str[i];
			for(j=0;j<c;j++){
				if(str[i][j]!='?')b[str[i][j]-'A']=1;
			}

		}

		i=j=0;

		while(i<r){
			j=0;
			while(j<c){
				if(str[i][j]!='?'){
					k=j+1;
					while(str[i][k]=='?' && k<c){
						str[i][k]=str[i][j];
						k++;
					}
				}
				if(str[i][j-1]=='?'&& j>0){
					for(k=j-1;k>=0;k--){
						str[i][k]=str[i][j];
					}
				}
				j++;
			}


			if(i==r-1){
				bool flag=0;
				for(k=0;k<c;k++){
					if(str[i][k]!='?') flag=1;
				}
				if(flag==0){
					for(k=0;k<c;k++){
						str[i][k]=str[i-1][k];
					}	
				}
			}
			else if(i>0){
				bool flag=0;
				for(j=0;j<c;j++){
					if(str[i][j]!='?') flag=1;
				}

				if(flag==0){
					for(k=0;k<c;k++){
						str[i][k]=str[i-1][k];
					}	
				}
			}

			if(i>0 && str[i-1][0]=='?'){
				for(k=i-1;k>=0;k--){
					if(str[k][0]!='?') break;
				}
				for(l=k+1;l<i;l++){
					for(m=0;m<c;m++){
						str[l][m]=str[i][m];
					}
				}
			}

			i++;
		}


		cout<<"Case #"<<x<<": "<<endl;
		for(i=0;i<r;i++) cout<<str[i]<<endl;
	}
	return 0;
}