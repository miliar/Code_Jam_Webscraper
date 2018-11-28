#include<iostream>
#include<vector>
#include<algorithm>
#include<numeric>

using namespace std;

bool op_toggle (bool i) { return !i; }
int main(void){
	vector<bool> sb;
	int nflip=0;
	int T=0;
	cin >> T;
	
	string s;
	int k=0;
	
	for(int tt=0;tt<T;tt++){
		cin>>s;
		cin>>k;
		sb.clear();
		nflip=0;
		for(char tc : s){
			if(tc=='+')sb.push_back(true);
			else sb.push_back(false);
			}
		
		//cout<<"T: "<<T<<" s: "<<s<<" k: "<<k<<endl;
		for(int jj=0;jj<sb.size()-k+1;jj++){
			//cout<<"loop "<<jj<<endl;			
			if(!sb[jj]){
				nflip++;
				transform (sb.begin()+jj, sb.begin()+jj+k, sb.begin()+jj, op_toggle);
			}
			
		}
		
		/*cout<<"New vector: ";
		for(bool tb : sb){
			cout<<tb;
		}
		cout<<endl;		*/
		
		int ssum = accumulate(sb.begin(),sb.end(), 0);
		if(ssum<sb.size()){
			cout<<"Case #"<<tt+1<<": IMPOSSIBLE"<<endl;
		}else{
			cout<<"Case #"<<tt+1<<": "<<nflip<<endl;
		}
		
		
	}
		

		
	
	
	return 0;
}
