#include <iostream>
#include <string>
using namespace std;

int carr[2000], arr[2000];
int len, conut,T, K;
int toggle[100];

int check(){
	for(int i=0; i<len; i++){
		if(carr[i]==0) return 0;
	}
	return 1;
}

int checkend(){
	for(int i=0; i<len; i++) carr[i]=arr[i];
	
	//cout << "Checkend: ";
	for(int i=0; i<len-K+1; i++){
		//cout << toggle[i] << " ";
		if(toggle[i]){
			for(int j=i; j<i+K; j++){
				carr[j]=1-carr[j];
			}
		}
	}
	//cout << " carr:";
	//for(int i=0; i<len; i++) cout << carr[i];
	//cout << endl;
	if(check()==1) return 1;
	else return 0;
}

int dfs(int x){
	//cout << "DFSing " << x << endl;
	if(x==len-K+1){
		if(checkend()){
			//cout << "YES!";
			for(int i=0; i<len-K+1; i++){
				//cout << toggle[i] << " ";
				if(toggle[i]) conut++;
			}
			//cout << conut << endl;
		}
	}
	else{
		dfs(x+1);
		toggle[x]=1;
		dfs(x+1);
		toggle[x]=0;
	}
}

int main(){
	cin >> T;
	for (int t = 1; t<=T; t++){
		cout << "Case #" << t << ": ";
	
		string s;
		cin >> s >> K;
		len = s.length();
		for(int i=0; i<len; i++){
			if(s[i]=='+') arr[i]=1;
			else arr[i]=0;
			//cout << arr[i] << " ";
		}
		
		conut = 0;
		int done = 0;
		if (checkend()){
			cout << "0";
			done++;
		}
		else dfs(0);
		if(conut==0 && done == 0) cout << "IMPOSSIBLE";
		else if(conut!=0) cout << conut;
		
	
		cout << endl;
	}
	
}
