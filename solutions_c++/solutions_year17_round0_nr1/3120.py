#include <iostream>
#include <string>
#include <sstream>

using namespace std;

//Global variables
int pancakes [1000];
string original;
int N,K;

//Function declarations
void flip(int start);
int optimal();

//////////////////////////////////////////////////
int main()
{
	int i,j,T,res;
	string KasStr;
	stringstream ss;
	
	getline(cin,KasStr);
	ss<<KasStr;
	ss>>T;
	ss.str(""); //clear the stringstream
	ss.clear();
  for (i=1; i<=T; i++){
  	getline(cin,original,' ');
  	N = original.size();
		getline(cin,KasStr);
		ss<<KasStr;
		ss>>K;
		ss.str(""); //clear the stringstream
		ss.clear();
  	
  	for(j=0; j<N; j++) {
    	if (original[j]=='+') pancakes[j]=1;
    	else pancakes[j]=0;
		}
		
		res = optimal();
		if (res==-1){
			cout << "Case #" << i << ": " << "IMPOSSIBLE" <<endl;
//			for(j=0; j<N; j++) {
//    		cout << pancakes[j]<<" ";
//			}
//			cout<<endl;
		}
		else cout << "Case #" << i << ": " << res <<endl;
  }
  return 0;
}//end main
//////////////////////////////////////////////////


void flip(int start){
	int i;
	for (i=start; i<start+K; i++){
		if (i>=N) cout<<"fubar"<<endl;
		pancakes[i] = 1 - pancakes[i];
	}
}

int optimal(){
	int i,count=0;
	for (i=0; i<=N-K; i++){
		if (pancakes[i]==0){
			flip(i);
			count+=1;
		}
	}
	for (i=N-K+1; i<N; i++){
		if (pancakes[i]==0){
			count=-1;
			break;
		}
	}
	return count;
}













