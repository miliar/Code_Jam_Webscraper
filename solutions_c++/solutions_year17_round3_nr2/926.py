#include<cstdio>
using namespace std;

int main(){
    int T;
    scanf(" %d ", &T);
    char day[1440];
    for(int t=1; t<=T; ++t){
	int Ac, Aj;
	scanf(" %d %d ", &Ac, &Aj);
	int Cs[Ac+1];
	int Ce[Ac+1];
	int Js[Aj+1];
	int Je[Aj+1];
	for(int i=0; i<Ac; ++i){
	    scanf(" %d %d ", &Cs[i], &Ce[i]);
	}
	for(int i=0; i<Aj; ++i){
	    scanf(" %d %d ", &Js[i], &Je[i]);
	}

	if(Ac+Aj == 1){
	    printf("Case #%d: %d\n", t, 2);
	}else if(Ac == 2){
	    int time;
	    if(Cs[0] < Cs[1]){
		time = Ce[1] - Cs[0];
	    }else{
		time = Ce[0] - Cs[1];
	    }
	    time = (1440-time+Ce[0]-Cs[0]+Ce[1]-Cs[1] < time ? 1440-time+Ce[0]-Cs[0]+Ce[1]-Cs[1] : time);
	    if(time <= 720){
		printf("Case #%d: %d\n", t, 2);
	    }else{
		printf("Case #%d: %d\n", t, 4);
	    }
	}else if(Aj == 2){
	    int time;
	    if(Js[0] < Js[1]){
		time = Je[1] - Js[0];
	    }else{
		time = Je[0] - Js[1];
	    }
	    time = (1440-time+Je[0]-Js[0]+Je[1]-Js[1] < time ? 1440-time+Je[0]-Js[0]+Je[1]-Js[1] : time);
	    if(time <= 720){
		printf("Case #%d: %d\n", t, 2);
	    }else{
		printf("Case #%d: %d\n", t, 4);
	    }
	}else{
	    printf("Case #%d: %d\n", t, 2);
	}
    }
    return 0;
}
