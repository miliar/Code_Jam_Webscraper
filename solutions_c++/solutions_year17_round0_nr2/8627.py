#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

string remove_zero( string ss){
	int minus=0;
for( int k=(ss.size()-1); k >= 0 ; k--){
	if(ss[k]==48 && k!=0 ){
		for( int i = k ; i<ss.size() ; i++){
			ss[i]=57;
		}
		minus=1;	
	}else if( minus==1 ){
		if( ss[k] == 49 ){
			if( k != 0 ){
				for( int i = k ; i<ss.size() ; i++){
					ss[i]=57;
				}		
				minus=1;
			}else{
				ss.erase(0,1);
			}
		}else{
			ss[k] = ss[k]-1;
			minus = 0;
		}
	}
}
return ss;
}

int main( int argc, char** argv){


ofstream output;
ifstream input;
cout<< " start "<<endl;
input.open(argv[1]);
output.open("ans.txt");


if(input.fail()){
  cout<<" error opening file"<<endl;
  return -1;
}


int cases;
input >> cases;

string ss;

for(int i=0; i< cases ; i++){

ss.clear();

input >> ss;

cout<<"case "<<i+1<<" "<<ss<<endl;

ss = remove_zero(ss);

int limit=ss.front();
for( int k=0; k < ss.size() ; k++){
	if( ss[k] >= limit ){
		limit = ss[k];
	}else{
		ss[k-1]=ss[k-1]-1;
		for( int j = k ; j < ss.size() ; j++){
			ss[j]=57;
		}
		if( ss[k-1] == 48 ){
			ss = remove_zero(ss);
		}
		limit=ss.front();
		k=-1;
	}
//	cout<<" ss "<<ss<<" limit "<<limit<<endl;
}

output<<"Case #"<<i+1<<": "<<ss<<endl;  
cout<<"Case #"<<i+1<<": "<<ss<<endl;  

}

input.close();
output.close();
return 0;
}
