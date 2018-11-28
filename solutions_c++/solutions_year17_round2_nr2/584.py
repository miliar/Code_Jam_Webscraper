#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int N;
int color[6];

char ans[2000];
int stack[2000][3];

int trans(char c){
	switch(c){
		case 'R':return 0;
		case 'Y':return 1;
		case 'B':return 2;
	}return -1;
}

int search(int pos){
	int ptr=0;
	char seq[3];
	int R=stack[pos][0];
	int Y=stack[pos][1];
	int B=stack[pos][2];
	if(R<0)return 0;
	if(Y<0)return 0;
	if(B<0)return 0;

	if(R+Y+B==0){
		//seems success?
		if(ans[pos-1]==ans[0])return 0;
		//success!
		ans[pos]='\0';
		cout<<ans<<endl;
		return 1;
	}

	if(R>=Y){
		if(R>=B){
			if(Y>=B) strcpy(seq,"RYB");
			else strcpy(seq,"RBY");
		}else{
			strcpy(seq,"BRY");
		}
	}else{
		if(R>=B){
			strcpy(seq,"YRB");
		}else{ 
			if(Y>=B) strcpy(seq,"YBR");
			else strcpy(seq,"BYR");
		}
	}
	while(ptr<3){
		ans[pos]=seq[ptr];ptr++;
		if(pos>0 && ans[pos]==ans[pos-1])continue;
		for(int i=0;i<3;i++)
			stack[pos+1][i]=stack[pos][i];
		stack[pos+1][ trans(ans[pos]) ]--;
		int ret=search(pos+1);
		if(ret>0)return ret;
	}
	return 0;
}


int onecase(){
	cin>>N;
	for(int i=0;i<6;i++)
		cin>>color[i];
	//0R, 2Y, and 4B matters
	int R=color[0], Y=color[2], B=color[4];
	
	if(2*R>N || 2*Y>N || 2*B>N){
		cout<<"IMPOSSIBLE"<<endl;
		return 0;
	}

	memset(stack,0,sizeof(stack));
	memset(ans,0,sizeof(ans));

	stack[0][0]=R;
	stack[0][1]=Y;
	stack[0][2]=B;
	search(0);

	/*string ANS="";
	char last='-';
	char final='-';
	for(int i=0;i<N-1;i++){
		//choose the largest non-repetitive char!
		//printf("Remaining R%d Y%d B%d\n",R,Y,B);

		char next='_';int maxPresence=0;
		if(last!='R' && R>maxPresence){
			next='R';maxPresence=R;
		}
		if(last!='Y' && Y>maxPresence){
			next='Y';maxPresence=Y;
		}
		if(last!='B' && B>maxPresence){
			next='B';maxPresence=B;
		}
		switch(next){
			case 'R':R--;break;
			case 'Y':Y--;break;
			case 'B':B--;break;
		}
		if(i==0){
			//first char, need to choose the last one != first one
			switch(next){
				case 'R':if(B>Y){B--;final='B';}else{Y--;final='Y';}break;
				case 'Y':if(B>R){B--;final='B';}else{R--;final='R';}break;
				case 'B':if(R>Y){R--;final='R';}else{Y--;final='Y';}break;
			}
			//cerr<<"final="<<final<<endl;
		}
		//cout<<"adding:"<<next<<"  last="<<last<<endl;
		ANS+=next;last=next;
	}
	ANS+=final;
	cout<<ANS<<endl;*/


	return 0;
}

int main(){
	//onecase();return 0;

	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		onecase();
	}
	return 0;
}