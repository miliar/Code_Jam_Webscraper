#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;


int n;
int k;
bool ocp[1000];

int f_left( int l ){
	int score=0;
	for( int i=(l-1) ; i>=0; i--){
		if(ocp[i]==0)
			score++;
		else
			break;
	}
	return score;
}
int f_right( int l ){
	int score=0;
	for( int i=l+1 ; i<n; i++){
		if(ocp[i]==0)
			score++;
		else
			break;
	}
	return score;
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




for(int i=0; i< cases ; i++){


input >> n >> k;

cout<<"case "<<i+1<<" "<<n<<" "<<k<<endl;


for( int j=0 ; j<n; j++){
	ocp[j]=0;
}

int cleft=0;
int cright=0;
int cmin=0;
int cmax=0;
int bp=0;
int bmin=0;
int bmax=0;

while( k > 0 ){
	bp=0;
	bmin=-1;
	bmax=INT_MAX;
	for(int j=0; j<n; j++){
		if(ocp[j]==0){
			cleft=f_left(j);
			cright=f_right(j);
			cmin=min(cleft,cright);
			cmax=max(cleft,cright);

			if( cmin > bmin ){
				//cout<<" cleft "<<cleft<<" cright "<<cright<<endl;
				bp = j;
				bmin = cmin;
				bmax = cmax;
			}else if( (cmin == bmin) && (cmax > bmax) ){
				//cout<<" cleft "<<cleft<<" cright "<<cright<<endl;
				bp = j;
				bmin = cmin;
				bmax = cmax;
			}
		}
	}
	ocp[bp]=1;
	k--;
}


output<<"Case #"<<i+1<<": "<<bmax<<" "<<bmin<<endl;  
cout<<"Case #"<<i+1<<": "<<bmax<<" "<<bmin<<endl;  

}

input.close();
output.close();
return 0;
}
