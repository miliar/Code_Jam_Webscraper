#include<fstream>
#include<vector>
#include<math.h>
using namespace std;

ifstream cin ("C-small-1-attempt0.in");
ofstream cout ("ax.out");

int ca=0;
int  lefts[1000000];
int rights[1000000];
bool  pins[1000000];

void doit(){
	long n,k;
	cin>>n>>k;
	for(long i=0;i<n;i++){
		pins[i] = false;
	}
	//long left[n];//posa empty stalls iparxoun metaksi tou ifistamenou kai tou closest left
	//long right[n];
	long last = 0;
	long maxmin,maxmax;
	if(n%2==0){
		last = n/2 - 1;
		pins[n/2 - 1] = true;
		for(int i=0;i<n;i++){
			if(i<n/2 - 1){
			    lefts[i] = -1;
				rights[i] = n/2 - 1;
			}
			if(i==n/2 - 1){
				lefts[i] = -1;
				rights[i] = n;
			}
			if(i>n/2 - 1){
				lefts[i] = n/2 - 1;
				rights[i] = n;
			}
		}
	}
	else{
		//	0 1 2 
		// 3/2 -> 1 nice
		last = n/2;
		pins[n/2] = true;
		for(int i=0;i<n;i++){
			if(i<n/2){
				lefts[i] = -1;
				rights[i] = n/2;
			}
			if(i==n/2){
				lefts[i] = -1;
				rights[i] = n;
			}
			if(i>n/2){
				lefts[i] = n/2;
				rights[i] = n;
			}
		}
	}
	int bestindx=0;
	for(int i=1;i<k;i++){
		//kamno search pou en na to valo
		maxmin = -10;
		maxmax = -10;
		bestindx = -10;
		for(int j=0;j<n;j++){
			//	aman den exei atomo mesa
			if(!pins[j]){
				if(min(j-lefts[j]-1,rights[j]-j-1)>maxmin){
					maxmin = min(j-lefts[j]-1,rights[j]-j-1);
					maxmax = max(j-lefts[j]-1,rights[j]-j-1);
					bestindx = j;
				}
				else{
					if((min(j-lefts[j]-1,rights[j]-j-1)==maxmin)&&(max(j-lefts[j]-1,rights[j]-j-1)>maxmax)){
						maxmin = min(j-lefts[j]-1,rights[j]-j-1);
						maxmax = max(j-lefts[j]-1,rights[j]-j-1);
						bestindx = j;
					}
				}
			}
		}
		if(bestindx==-10){
			cout<<"to katalaves"<<endl;
		}
		last = bestindx;
		pins[last] = true;
		for(int j=last-1;j>=0;j--){
			if(pins[j]){
				break;
			}
			else{
				rights[j] = last;
			}
		}
		for(int j=last+1;j<n;j++){
			if(pins[j]){
				break;
			}
			else{
				lefts[j] = last;
			}
		}
	}
	cout<<"Case #"<<ca<<": "<<max(last-lefts[last]-1, rights[last]-last-1)<<" "<<min(last-lefts[last]-1, rights[last]-last-1)<<endl; 
}

int main(){
	int t;
	cin>>t;
	while(t--){
		ca++;
		doit();
	}
}
