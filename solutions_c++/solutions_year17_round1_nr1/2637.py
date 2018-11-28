#include<iostream>
#include<string>
#include<vector>
using namespace std;
int start;
int M,N;
vector<vector<char> > matrix;
vector<vector<char> > dmatrix;
void parse(string s){
	for(int i=0;s[i]!='\0';i++){
		matrix[start][i]=s[i];
		dmatrix[start][i]=s[i];
	}
	start++;
}
void fill(){
	int pfilledrow=-1;
	char ch;
	bool tobreak;
	for(int i=0;i<M;i++){
		for(int j=0;j<N;j++){
			tobreak=true;
			if(dmatrix[i][j]!='?'){
				ch=dmatrix[i][j];
				for(int m=j-1;m>=0;m--)
					if(dmatrix[i][m]=='?')
						dmatrix[i][m]=ch;
					else{
						tobreak=false;	
						break;
					}
				for(int m=j+1;m<N;m++)
					if(dmatrix[i][m]=='?')
						dmatrix[i][m]=ch;
					else {
						tobreak=false;
						break;
					}
				pfilledrow=i;
				if(tobreak)
					break;
			}
						
		}
		if((pfilledrow!=-1)&&(pfilledrow<i)){
				for(int m=0;m<N;m++)
					dmatrix[i][m]=dmatrix[pfilledrow][m];
				pfilledrow=i;			
			}
	}
	pfilledrow=-1;
	for(int i=M-1;i>=0;i--){
		for(int j=0;j<N;j++){
			tobreak=true;
			if(dmatrix[i][j]!='?'){
				ch=dmatrix[i][j];
				for(int m=j-1;m>=0;m--)
					if(dmatrix[i][m]=='?')
						dmatrix[i][m]=ch;
					else{
						tobreak=false;
						break;
					}
				for(int m=j+1;m<N;m++)
					if(dmatrix[i][m]=='?')
						dmatrix[i][m]=ch;
					else{
						tobreak=false;
						break;
					}				
				pfilledrow=i;
				if(tobreak)
					break;
			}
						
		}
		if((pfilledrow!=-1)&&(pfilledrow>i)){
				for(int m=0;m<N;m++)
					dmatrix[i][m]=dmatrix[pfilledrow][m];
				pfilledrow=i;			
			}
	}					
	
}

int main(){
	int T;
	cin>>T;
	int c=0;
	while(T--){
		//int M,N
		cin>>M>>N;
		string s;
		vector<vector<char> > ref1(M,vector<char>(N,' '));
		matrix=ref1;		
		vector<vector<char> > ref2(M,vector<char>(N,' '));
		dmatrix=ref2;
		for(int i=0;i<M;i++){
			cin>>s;
			parse(s);
		}
		c++;
		start=0;
		fill();
		cout<<"Case #"<<c<<":\n";
		for(int i=0;i<M;i++){
			for(int j=0;j<N;j++)
				cout<<dmatrix[i][j];
			cout<<endl;
		}
	}
	return 0;
}
