using namespace std;
#include <stdio.h>

char GRID[25][25];
int Marcas[30];
int T,N,M;

inline bool estaVacia(const int& r);
inline void llena(const int& r);
inline void llenaUp(const int& r,const int& p);
inline void llenaDown(const int& r);

int main(){
	
	scanf("%d",&T);
	for(int c1=0;c1<T;++c1){
		scanf("%d %d",&N,&M);
		getchar();
		for(int c2=0;c2<N;++c2){
			for(int c3=0;c3<M;++c3){
				scanf("%c",&GRID[c2][c3]);
			}
			getchar();
		}
	
		for(int c2=0;c2<N;++c2){
			if(estaVacia(c2)){
				Marcas[c2]=1;
			}
			else{
				Marcas[c2]=0;
				llena(c2);
			}
		}
		
		int flag=-1,wea=-1;
		for(int c2=0;c2<N;++c2){
			if(Marcas[c2]!=0){
				flag=c2;
				while(Marcas[c2]!=0 && c2<N)++c2;
				if(c2==N)break;
				llenaUp(c2,flag);
				flag=-1;
				wea=c2;
			}
			else	wea=c2;
		}
		
		if(flag!=-1)llenaDown(wea);
		
		printf("Case #%d:\n",c1+1);
		for(int c2=0;c2<N;++c2){
			for(int c3=0;c3<M;++c3){
				printf("%c",GRID[c2][c3]);
			}
			puts("");
		}
		
	}
	return 0;
}

inline bool estaVacia(const int& r){
	for(int c1=0;c1<M;++c1){
		if(GRID[r][c1]!='?')return false;
	}
	return true;
}
inline void llena(const int& r){
	int flag=0;
	for(int c1=0;c1<M;++c1){
		char c=GRID[r][c1];
		if(c!='?'){
			if(flag==0){
				for(int c2=c1-1;c2>=0;--c2){
					GRID[r][c2]=c;
				}
				flag=1;
			}
			int c2=c1+1;
			while(GRID[r][c2]=='?' && c2<M){
				GRID[r][c2]=c;
				++c2;
			}
		}
	}
}
inline void llenaUp(const int& r,const int& p){
	for(int c1=0;c1<M;++c1){
		char c=GRID[r][c1];
		for(int c2=r-1;c2>=p;--c2){
			GRID[c2][c1]=c;
		}
	}
}
inline void llenaDown(const int& r){
	for(int c1=0;c1<M;++c1){
		char c=GRID[r][c1];
		for(int c2=r;c2<N;++c2){
			GRID[c2][c1]=c;
		}
	}
}
