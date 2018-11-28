#include <bits/stdc++.h>
using namespace std;
class bathrooms{
public:
	bool free;
	int L;
	int R;
	int min;
	int max;
};
void build(bathrooms& input[],int N);
int main(){
    int T,I;
    cin>>T;
    for(I=0;I<T;I++){
    	int N,K;
    	cin>>N>>K;
    	int i,j,iterations,caseWinner,minCheck,maxCheck;
    	bathrooms input[N];
    	for(i=0;i<N;i++){
    		input[i].free=true;
		}
		for(iterations=0;iterations<K;iterations++){
			build(input[N],N);
			minCheck=0;
			maxCheck=0;
			for(i=N-1;i>0;i--){
				if(input[i].free==true){
					if((input[i].min>minCheck)||(input[i].min=minCheck&&input[i].max>=maxCheck)){
						caseWinner=i;
						minCheck=input[i].min;
						maxCheck=input[i].max;
					}					
				}
			}
			input[caseWinner].free=false;
		}
		cout<<"Case #"<<I+1<<": "<<maxCheck<<minCheck;
	}
    return 0;
}

void build(bathrooms& input[],int N){
	int count,i;
	for(count=0;count<N;count++){
		if(input[count].free==false){
			continue;
		}
		int l=0,r=0;
		for(i=count-1;i>0;i--){
			if(input[i].free==true){
				l++;
			}else{
				break;
			}
		}
		for(i=count+1;i<N;i++){
			if(input[i].free==true){
				r++;
			}else{
				break;
			}
		}
		input[counter].L=l;
		input[counter].R=r;
		if(l>=r){
			input[counter].min=r;
			input[counter].max=l;
		}else{
			input[counter].min=l;
			input[counter].max=r;
		}
	}
}