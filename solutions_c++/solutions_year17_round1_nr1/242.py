#include <bits/stdc++.h>

using namespace std;
#define pb push_back
typedef long long LL;

int r,c;
string s[30];
bool have[30];

void sl(int x){	
	int first = -1;
	for(int i=0; i<c; i++){
		if( s[x][i] !='?' ){	
			first = i;
			break;
		}
	}
//	cout << s[x] << " " << first << " " <<s[x][first] << endl;
	for(int i=0; i<first; i++){
		s[x][i] = s[x][first];
	}
	char cur = s[x][first];
	for(int i=first+1; i<c; i++){
		if(s[x][i] == '?') s[x][i] = cur;
		else cur = s[x][i];
	}	
}


void solve(int test){
	cout << "Case #" << test + 1 << ":" << endl;;
	cin >> r >> c ;
	memset(have,0,sizeof have);
	bool haverow = false;
	for(int i=0; i<r; i++){
		cin.ignore();
		cin >> s[i];	
		for(int j=0; j<c; j++){
			if(s[i][j]!='?') {			
				have[i] = true;
				sl(i);				
				haverow = true;
				break;
			}		
		}			
		
	}
	
	if(haverow){	
		int first = -1;
		for(int i=0; i<r; i++) {			
			if(have[i]) {			
				first = i; 
				break; 
			}
		}	
		for(int i=0; i<first; i++){
			s[i] = s[first];		
		}
		string cur = s[first];
		for(int i=first+1; i<r; i++){
			if(!have[i]) s[i] = cur;
			else cur = s[i];		
		}
		for(int i=0; i<r; i++){
			cout << s[i] << endl;
		}	
	}
	else{
		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++) s[i][j] = 'A';
		}
		for(int i=0; i<r; i++){
			cout << s[i] << endl;
		}
	}	
}


int ntest;
int main(){
	freopen("A-large.in","r",stdin);
	//freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	cin >> ntest;
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
